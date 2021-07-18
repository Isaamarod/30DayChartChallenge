import plotly.express as px
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc

import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

from lollipop_graphs import *
from tree_graphs import *


csv_europe=pd.read_csv('europe_sun_hours.csv')
csv_asia=pd.read_csv('asia_sun_hours.csv')
csv_africa=pd.read_csv('africa_sun_hours.csv')



csv_europe=pd.read_csv('europe_sun_hours.csv')
csv_asia=pd.read_csv('asia_sun_hours.csv')
csv_africa=pd.read_csv('africa_sun_hours.csv')
csv_south_america=pd.read_csv('south_america_sun_hours.csv')
csv_north_center_america=pd.read_csv('north_and_center_america_sun_hours.csv')
csv_oceania=pd.read_csv('oceania_sun_hours.csv')

###mean by year grouped by year
csv_europe_country_mean =csv_europe.groupby('Country', as_index=False)['Year'].mean()
csv_europe_country_mean = csv_europe_country_mean.sort_values(by='Year')

csv_asia_country_mean =csv_asia.groupby('Country', as_index=False)['Year'].mean()
csv_asia_country_mean = csv_asia_country_mean.sort_values(by='Year')


csv_africa_country_mean =csv_africa.groupby('Country', as_index=False)['Year'].mean()
csv_africa_country_mean = csv_africa_country_mean.sort_values(by='Year')

csv_south_america_country_mean =csv_south_america.groupby('Country', as_index=False)['Year'].mean()
csv_south_america_country_mean = csv_south_america_country_mean.sort_values(by='Year')

csv_north_center_america_country_mean =csv_north_center_america.groupby('Country', as_index=False)['Year'].mean()
csv_north_center_america_country_mean = csv_north_center_america_country_mean.sort_values(by='Year')

csv_oceania_country_mean =csv_oceania.groupby('Country', as_index=False)['Year'].mean()
csv_oceania_country_mean = csv_oceania_country_mean.sort_values(by='Year')



app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


navbar = dbc.NavbarSimple(
    brand="Year sunshine duration by continent and country Project #30DayChartChallenge",
    brand_href="#",
    color="dark",
    dark=True,
)




app.layout = html.Div([ navbar ,        html.Div("Day 11: Circle"),
html.Div([
    dbc.Row([dbc.Col( html.Label ("Please select a continent")), dbc.Col(dcc.Dropdown(
            id='continent',
            options=[
                {'label': 'EUROPE', 'value': 'EUR'},
                {'label': 'SOUTH AMERICA', 'value': 'SA'},
                {'label': 'ASIA', 'value': 'AS'},
                {'label': 'AFRICA', 'value': 'AF'},
                {'label': 'OCEANIA', 'value': 'OC'},
                {'label': 'NORTH-CENTER AMERICA', 'value': 'NCA'},
            ],
            value='EUR')),
dbc.Col( html.Label ("Please select a country")),
    dbc.Col(dcc.Dropdown(
                id='country'),
    )])], style={'width': '70%', 'display': 'inline-block','margin-top':'3%','margin-bottom':'3%'}),
   html.Div([

    html.Div([dcc.Graph(id="fig")],style={'display': 'inline-block'}),
    html.Div([dcc.Graph(id="figParallel")], style={'display': 'inline-block'}),
       html.Div("Day 16: Tree"),
       html.Div([dcc.Graph(id="figTree")]),
       html.Div("Day 12: Strips"),

       html.Div([dcc.Graph(id="figLollipop")]),


]) ])



# if country_value:
#     csv_europe = csv_europe.loc[csv_europe['Country']=='country_value']
@app.callback(
    Output(component_id='fig', component_property='figure'),Output(component_id='country', component_property='options'),
Output(component_id='figParallel', component_property='figure'),Output(component_id='figLollipop', component_property='figure'),
Output(component_id='figTree', component_property='figure'),
    Input(component_id='continent', component_property='value'),Input(component_id='country', component_property='value')
)
def update_output_div(continent,country_value):
    options_dict={}
    print(country_value)
    if continent == 'EUR' :
        options_dict= [{'label': x, 'value': x} for x in list(csv_europe['Country'].unique())]
        if country_value is not None and country_value in list(csv_europe['Country'].unique()):
            csv_europe_by_country_value = csv_europe.loc[csv_europe['Country'] == country_value]
            print(csv_europe_by_country_value)
            fig = px.sunburst(csv_europe_by_country_value, path=["Country", "City", "Year"])
            fig_2 = px.scatter_geo(csv_europe_by_country_value, locations="Country", locationmode='country names',
                                 color="Country",
                                 hover_name="City", size=csv_europe_by_country_value["Year"],
                                 projection="orthographic")

        else:
            fig = px.sunburst(csv_europe, path=["Country", "City", "Year"])
            grouped = csv_europe.groupby('Country', as_index=False)
            grouped_first = grouped.first()
            fig_2 = px.scatter_geo(grouped_first, locations="Country", locationmode='country names',
                                   color="Country",
                                   hover_name="City", size=grouped_first["Year"],
                                   projection="orthographic")

        # csv_europe_value_parallel = csv_europe[['Country', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
        # fig_3 = px.parallel_coordinates(csv_europe_value_parallel,dimensions=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug', 'Sep', 'Oct', 'Nov', 'Dec'],color_continuous_scale=px.colors.sequential.Cividis_r)
        fig_lollipop = get_lollipop_graph(csv_europe_country_mean)
        fig_tree=tree_graphs(csv_europe)
        return fig.update_layout(width=800,
                          height=800), options_dict,fig_2.update_layout(width=800,
                          height=800),fig_lollipop,fig_tree
    elif continent == 'AS' :
        options_dict= [{'label': x, 'value': x} for x in list(csv_asia['Country'].unique())]
        if country_value is not None and country_value in list(csv_asia['Country'].unique()):
            csv_asia_by_country_value = csv_asia.loc[csv_asia['Country'] == country_value]
            print(csv_asia_by_country_value)
            fig = px.sunburst(csv_asia_by_country_value, path=["Country", "City", "Year"])
            fig_2 = px.scatter_geo(csv_asia_by_country_value, locations="Country", locationmode='country names',
                               color="Country",
                               hover_name="City", size=csv_asia_by_country_value["Year"],
                               projection="orthographic")

        else:
            fig = px.sunburst(csv_asia, path=["Country", "City", "Year"])
            grouped = csv_asia.groupby('Country', as_index=False)
            grouped_first = grouped.first()
            fig_2 = px.scatter_geo(grouped_first, locations="Country", locationmode='country names',
                                   color="Country",
                                   hover_name="City", size=grouped_first["Year"],
                                   projection="orthographic")
        # csv_europe_value_parallel = csv_asia[
        #     ['Country', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
        # fig_3 = px.parallel_coordinates(csv_europe_value_parallel,
        #                                 dimensions=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
        #                                             'Oct', 'Nov', 'Dec'])
        fig_lollipop = get_lollipop_graph(csv_asia_country_mean)
        fig_tree=tree_graphs(csv_asia)
        return fig.update_layout(width=800,
                          height=800), options_dict, fig_2.update_layout(width=800,
                          height=800),fig_lollipop,fig_tree
    elif continent == 'AF':
        options_dict= [{'label': x, 'value': x} for x in list(csv_africa['Country'].unique())]
        if country_value is not None and country_value in list(csv_africa['Country'].unique()):
            csv_africa_by_country_value = csv_africa.loc[csv_africa['Country'] == country_value]
            print(csv_africa_by_country_value)
            fig = px.sunburst(csv_africa_by_country_value, path=["Country", "City", "Year"])
            fig_2 = px.scatter_geo(csv_africa_by_country_value, locations="Country", locationmode='country names',
                               color="Country",
                               hover_name="City", size=csv_africa_by_country_value["Year"],
                               projection="orthographic")

        else:
            fig = px.sunburst(csv_africa, path=["Country", "City", "Year"])
            grouped = csv_africa.groupby('Country', as_index=False)
            grouped_first = grouped.first()
            fig_2 = px.scatter_geo(grouped_first, locations="Country", locationmode='country names',
                                   color="Country",
                                   hover_name="City", size=grouped_first["Year"],
                                   projection="orthographic")
        # csv_europe_value_parallel = csv_europe[
        #     ['Country', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
        # fig_3 = px.parallel_coordinates(csv_europe_value_parallel,
        #                                 dimensions=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
        #                                             'Oct', 'Nov', 'Dec'])
        fig_lollipop = get_lollipop_graph(csv_africa_country_mean)
        fig_tree = tree_graphs(csv_africa)
        return fig.update_layout(width=800,
                          height=800),options_dict, fig_2.update_layout(width=800,
                          height=800),fig_lollipop,fig_tree
    elif continent == 'SA':
        options_dict= [{'label': x, 'value': x} for x in list(csv_south_america['Country'].unique())]
        if country_value is not None and country_value in list(csv_south_america['Country'].unique()):
            csv_southamerica_by_country_value = csv_south_america.loc[csv_south_america['Country'] == country_value]
            print(csv_southamerica_by_country_value)
            fig = px.sunburst(csv_southamerica_by_country_value, path=["Country", "City", "Year"])
            fig_2 = px.scatter_geo(csv_southamerica_by_country_value, locations="Country", locationmode='country names',
                               color="Country",
                               hover_name="City", size=csv_southamerica_by_country_value["Year"],
                               projection="orthographic")

        else:
            fig = px.sunburst(csv_south_america, path=["Country", "City", "Year"])
            grouped = csv_south_america.groupby('Country', as_index=False)
            grouped_first = grouped.first()
            fig_2 = px.scatter_geo(grouped_first, locations="Country", locationmode='country names',
                                   color="Country",
                                   hover_name="City", size=grouped_first["Year"],
                                   projection="orthographic")
        # csv_europe_value_parallel = csv_south_america[
        #     ['Country', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
        # fig_3 = px.parallel_coordinates(csv_europe_value_parallel,
        #                                 dimensions=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
        #                                             'Oct', 'Nov', 'Dec'])
        fig_lollipop = get_lollipop_graph(csv_south_america_country_mean)
        fig_tree = tree_graphs(csv_south_america)

        return fig.update_layout(width=800,
                          height=800),options_dict, fig_2.update_layout(width=800,
                          height=800),fig_lollipop,fig_tree
    elif continent == 'NCA':
        options_dict= [{'label': x, 'value': x} for x in list(csv_north_center_america['Country'].unique())]
        if country_value is not None and country_value in list(csv_north_center_america['Country'].unique()):
            csv_nca_by_country_value = csv_north_center_america.loc[csv_north_center_america['Country'] == country_value]
            print(csv_nca_by_country_value)
            fig = px.sunburst(csv_nca_by_country_value, path=["Country", "City", "Year"])
            fig_2 = px.scatter_geo(csv_nca_by_country_value, locations="Country", locationmode='country names',
                               color="Country",
                               hover_name="City", size=csv_nca_by_country_value["Year"],
                               projection="orthographic")

        else:
            fig = px.sunburst(csv_north_center_america, path=["Country", "City", "Year"])
            grouped = csv_north_center_america.groupby('Country', as_index=False)
            grouped_first = grouped.first()
            fig_2 = px.scatter_geo(grouped_first, locations="Country", locationmode='country names',
                                   color="Country",
                                   hover_name="City", size=grouped_first["Year"],
                                   projection="orthographic")
        # csv_europe_value_parallel = csv_north_center_america[
        #     ['Country', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
        # fig_3 = px.parallel_coordinates(csv_europe_value_parallel,
        #                                 dimensions=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
        #                                             'Oct', 'Nov', 'Dec'])
        fig_lollipop = get_lollipop_graph(csv_north_center_america_country_mean)
        fig_tree = tree_graphs(csv_north_center_america)

        return fig.update_layout(width=800,
                          height=800),options_dict, fig_2.update_layout(width=800,
                          height=800),fig_lollipop,fig_tree
    elif continent == 'OC':
        options_dict= [{'label': x, 'value': x} for x in list(csv_oceania['Country'].unique())]
        if country_value is not None and country_value in list(csv_oceania['Country'].unique()):
            csv_oc_by_country_value = csv_oceania.loc[csv_oceania['Country'] == country_value]
            print(csv_oc_by_country_value)
            fig = px.sunburst(csv_oc_by_country_value, path=["Country", "City", "Year"])
            fig_2 = px.scatter_geo(csv_oc_by_country_value, locations="Country", locationmode='country names',
                               color="Country",
                               hover_name="City", size=csv_oc_by_country_value["Year"],
                               projection="orthographic")

        else:
            fig = px.sunburst(csv_oceania, path=["Country", "City", "Year"])
            grouped = csv_oceania.groupby('Country', as_index=False)
            grouped_first = grouped.first()
            fig_2 = px.scatter_geo(grouped_first, locations="Country", locationmode='country names',
                                   color="Country",
                                   hover_name="City", size=grouped_first["Year"],
                                   projection="orthographic")
        # csv_europe_value_parallel = csv_oceania[
        #     ['Country', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
        # fig_3 = px.parallel_coordinates(csv_europe_value_parallel,
        #                                 dimensions=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
        #                                             'Oct', 'Nov', 'Dec'])
        fig_lollipop = get_lollipop_graph(csv_oceania_country_mean)
        fig_tree = tree_graphs(csv_oceania)
        return fig.update_layout(width=800,
                          height=800),options_dict, fig_2.update_layout(width=800,
                          height=800),fig_lollipop,fig_tree
app.run_server(debug=True, use_reloader=False)