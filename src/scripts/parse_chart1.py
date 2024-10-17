import numpy as np
import pandas as pd
import plotly.express as px
import requests
import geopandas as gpd
pd.options.mode.chained_assignment = None  # default='warn'

data = pd.read_csv("src/data/countypres_2000-2020.csv")
figs = {}

rust_belt = ['PA', 'OH', 'MI', 'WI']
rust_belt_names = ['Pennsylvania', 'Ohio', 'Michigan', 'Wisconsin']

data_total = data[data['mode'] == 'TOTAL']
data_total = data[data['state_po'].isin(rust_belt)]

pivot_data = data_total.pivot_table(
    index=['year', 'county_fips', 'state_po', 'county_name'],
    columns='party',
    values='candidatevotes',
    aggfunc='sum',
    fill_value=0
)

pivot_data = pivot_data.reindex(columns=['DEMOCRAT', 'REPUBLICAN'], fill_value=0)

pivot_data['vote_difference'] = pivot_data['DEMOCRAT'] - pivot_data['REPUBLICAN']
pivot_data['total_votes'] = data_total.groupby(['year', 'county_fips'])['totalvotes'].first()

pivot_data['percentage_margin'] = (pivot_data['vote_difference'] / pivot_data['total_votes'])

pivot_data = pivot_data.reset_index()

margin_df = pivot_data[['year', 'county_fips', 'county_name', 'percentage_margin']]

geojson_path = "https://gist.githubusercontent.com/sdwfrost/d1c73f91dd9d175998ed166eb216994a/raw/e89c35f308cee7e2e5a784e1d3afc5d449e9e4bb/counties.geojson"

geo_data = requests.get(geojson_path).json()

def plot_pres_vote_margin_diff():
    if len(figs) > 0:
        return
    
    for year in [2004, 2008, 2012, 2016, 2020]:

        # Calculate the previous election year
        previous_year = year - 4

        current_margin = margin_df[margin_df['year'] == year]
        previous_margin = margin_df[margin_df['year'] == previous_year]

        current_margin['percentage_margin_100'] = current_margin['percentage_margin'] * 100
        fig = px.choropleth(current_margin,
                            geojson=geo_data,
                            locations='county_fips',
                            color='percentage_margin_100',
                            color_continuous_scale='RdBu',
                            featureidkey="properties.GEOID",
                            range_color=(-50,50),
                            scope='usa',
                            labels={'percentage_margin_100': ''},
                            hover_name='county_name')
        fig.update_geos(fitbounds="locations",
                        visible=False)
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.update_layout(paper_bgcolor="#0E1117")
        fig.update_layout(geo_bgcolor="#0E1117")
        fig.update_xaxes(overwrite=True, fixedrange=True)
        fig.update_yaxes(overwrite=True, fixedrange=True)
        fig.update_layout(dragmode=False)
        figs.update({int(year/2): fig})

        merged_margins = pd.merge(
            current_margin,
            previous_margin,
            on='county_fips',
            suffixes=('_current','_previous')
        )
        merged_margins['margin_diff'] = (merged_margins['percentage_margin_current'] - merged_margins['percentage_margin_previous']) * 100

        fig = px.choropleth(merged_margins,
                        geojson=geo_data,
                        locations='county_fips',
                        color='margin_diff',
                        color_continuous_scale='RdBu',
                        featureidkey="properties.GEOID",
                        range_color=(-30,30),
                        scope='usa',
                        labels={'margin_diff': ''},
                        hover_name='county_name_current'
                        )
        fig.update_geos(fitbounds="locations",
                        visible=False)
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.update_layout(paper_bgcolor="#0E1117")
        fig.update_layout(geo_bgcolor="#0E1117")
        fig.update_xaxes(overwrite=True, fixedrange=True)
        fig.update_yaxes(overwrite=True, fixedrange=True)
        fig.update_layout(dragmode=False)
        figs.update({year: fig})

def get_vote_margin_diff(year):
    if len(figs) == 0:
        plot_pres_vote_margin_diff()
    return figs[year]

def get_vote_margin(year):
    if len(figs) == 0:
        plot_pres_vote_margin_diff()
    return figs[int(year/2)]