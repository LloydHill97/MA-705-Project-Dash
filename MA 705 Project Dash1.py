# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 22:20:16 2021

@author: Lloyd Hill
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# pandas dataframe to html table
def generate_table(dataframe, max_rows=20):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app = dash.Dash(__name__, external_stylesheets=stylesheet)

df = pd.read_csv('Bentley Hitting Stats.csv')
dfp = pd.read_csv('Bentley Pitching Stats.csv')

fig = px.scatter(df, x="AB", y="H", size="SLG", color="NAME", hover_name="NAME", log_x=True, size_max=60)
fig1 = px.scatter(dfp, x="APP", y="IP", size="K/9", color="NAME", hover_name="NAME", log_x=True, size_max=60)
fig2 = px.bar(df, x = "NAME", y = "AVG")
fig3 = px.bar(dfp, x = "NAME", y = "K")

app.layout = html.Div([
    html.H1('Bentley Baseball Dashboard',
            style={'textAlign' : 'center'}),
    
    html.H3('About Bentley Baseball'),
    dcc.Markdown('''
    * Bentley University is located in Waltham, MA.
    * Bentley University's Baseball team has been around since 1969.
    * Since the program's beginning Coach Bob DeFelice has served as the program's only head coach.
    * This dashboard includes data on the seasons from 2019-2021.
    * All data from this dashboard was retrieved on April 20th, 2021.
                 '''),
    
    html.A("Click here to go to the Bentley Baseball Page" ,
            href='https://www.bentleyfalcons.com/sports/bsb/index',
            target='_blank'),
    html.Br(),
    html.H3('Bentley Baseball Offensive Statistics'),
    html.Label('Select Year'),
    dcc.Dropdown(
        options=[
            {'label': '2021', 'value': '2021'},
            {'label': '2020', 'value': '2020'},
            {'label': '2019', 'value': '2019'}],
        value='2021',
        id = 'year_dropdown',
        style={'width': '33%'}),
    html.Div(id='table_div'),
    html.H4('Bentley Baseball Offensive Visuals'),
    html.H6('Offensive Scatterplot Visual'),
      dcc.Markdown('''
    * This visual displays At Bats along the x-axis with Hits along the y-axis.
    * The size of each circle represent a player's Slugging Percentage.
    * As defined by mlb.com, Slugging percentage represents the total number of bases a player records per at-bat.
    * The visual is filtered by 'year' which can be selcted above the offensive data frame. 
                 '''),
    
    dcc.Graph(id = 'H v AB', figure = fig),
######################################################################################################
    html.Br(),
    html.H6('Offensive Bar Chart Visual'),
    html.Label('Select Year'),
    dcc.Dropdown(
        options=[
            {'label': '2021', 'value': '2021'},
            {'label': '2020', 'value': '2020'},
            {'label': '2019', 'value': '2019'}],
        value='2021',
        id = 'year_dropdown2',
        style={'width': '33%'}),
    html.Div(id='table_div2'),
    
    
    html.Label('Select Offensive Statistic'),
    dcc.Dropdown(
        options=[
            {'label': 'AVG', 'value': 'AVG'},
            {'label': 'OBP', 'value': 'OBP'},
            {'label': 'SLG', 'value': 'SLG'},
            {'label': 'G', 'value': 'G'},
            {'label': 'AB', 'value': 'AB'},
            {'label': 'R', 'value': 'R'},
            {'label': 'H', 'value': 'H'},
            {'label': '2B', 'value': '2B'},
            {'label': '3B', 'value': '3B'},
            {'label': 'HR', 'value': 'HR'},
            {'label': 'RBI', 'value': 'RBI'},
            {'label': 'BB', 'value': 'BB'},
            {'label': 'K', 'value': 'K'},
            {'label': 'SB', 'value': 'SB'},
            {'label': 'CS', 'value': 'CS'}],
        value='AVG',
        id = 'hitter_visual_dropdown',
        style={'width': '33%'}),
    dcc.Markdown('''
    * The visual below can be filtered by year as well as a hitting metric of choice.
                  '''),
    html.Div(id='table_div3'),
    
    dcc.Graph(id = 'Hitter_visual_2', figure = fig2),
    
    
######################################################################################################

 html.H6('Offensive Bar Chart Visual Dictionary'),
 dcc.Markdown('''
    * AVG: Batting Average
    * OBP: On Base Percentage
    * SLG: Slugging Percentage
    * G: Games
    * AB: At Bats
    * R: Runs
    * H: Hits
    * 2B: Double
    * 3B: Triple
    * HR: Home Run
    * RBI: Runs Batted In
    * BB: Walks
    * K: Strikeouts
    * SB: Stolen Bases
    * CS: Caught Stealing
    
                 '''),
                 
 html.H6('For further explanation on hitting statistics seek the link below:'),
 html.A("MLB Offensive Statistics Definition Glossary" ,
            href='https://www.mlb.com/glossary/standard-stats/batting-average#:~:text=One%20of%20the%20oldest%20and,)%20and%20one%20(1.000).&text=Batting%20average%20can%20also%20be%20applied%20in%20evaluating%20pitchers.',
            target='_blank'),

######################################################################################################

 html.Br(),
######################################################################################################

    
    html.H3('Bentley Baseball Pitching Statistics'),
    html.Label('Select Year'),
    dcc.Dropdown(
        options=[
            {'label': '2021', 'value': '2021'},
            {'label': '2020', 'value': '2020'},
            {'label': '2019', 'value': '2019'}],
        value='2021',
        id = 'year_dropdown1',
        style={'width': '33%'}),
    html.Div(id = 'table_div1'),
    html.H4('Bentley Baseball Pitching Visual'),
     dcc.Markdown('''
    * This visual displays appearences along the x-axis with innings pitched along the y-axis.
    * The size of each circle represent a player's strikeout per nine innings rate.
    * As defined by mlb.com, K/9 rate measures how many strikeouts a pitcher averages for every nine innings pitched.
    * The visual is filtered by 'year' which can be selcted above the pitching data frame. 
                 '''),
    dcc.Graph(id = 'APP v IP', figure = fig1),
    
######################################################################################################

 html.Br(),
    html.H6('Pitching Bar Chart Visual'),
    html.Label('Select Year'),
    dcc.Dropdown(
        options=[
            {'label': '2021', 'value': '2021'},
            {'label': '2020', 'value': '2020'},
            {'label': '2019', 'value': '2019'}],
        value='2021',
        id = 'year_dropdown3',
        style={'width': '33%'}),
    html.Div(id='table_div4'),
    
    
    html.Label('Select Pitching Statistic'),
    dcc.Dropdown(
        options=[
            {'label': 'APP', 'value': 'APP'},
            {'label': 'GS', 'value': 'GS'},
            {'label': 'W', 'value': 'W'},
            {'label': 'L', 'value': 'L'},
            {'label': 'SV', 'value': 'SV'},
            {'label': 'CG', 'value': 'CG'},
            {'label': 'IP', 'value': 'IP'},
            {'label': 'H', 'value': 'H'},
            {'label': 'ER', 'value': 'ER'},
            {'label': 'BB', 'value': 'BB'},
            {'label': 'K', 'value': 'K'},
            {'label': 'K/9', 'value': 'K/9'},
            {'label': 'HR', 'value': 'HR'},
            {'label': 'ERA', 'value': 'ERA'},
            ],
        value='K',
        id = 'pitcher_visual_dropdown',
        style={'width': '33%'}),
    dcc.Markdown('''
    * The visual below can be filtered by year as well as a pitching metric of choice.
                  '''),
    html.Div(id='table_div5'),
    
    
    dcc.Graph(id = 'pitcher_visual_2', figure = fig3),

######################################################################################################
 html.H6('Pitching Bar Chart Visual Dictionary'),
 dcc.Markdown('''
    * APP: Total Number of Appearences
    * GS: Games Started
    * W: Wins
    * L: Losses
    * SV: Saves
    * CG: Complete Game, occurs when a starting pitcher pitches the full length of the game.
    * IP: Innings Pitched
    * H: Hits
    * ER: Earned Runs
    * BB: Walk
    * K: Strikeout
    * K/9: The number of strikeouts a pitcher earns per nine innings. 
    * HR: The total number of Home Runs a pitched surrenders.
    * ERA: (Earned Runs / Innings Pitched)  x 9
    
                 '''),
 html.H6('For further explanation on pitching statistics seek the link below:'),
 html.A("MLB Pitching Definition Glossary" ,
            href='https://www.mlb.com/glossary/standard-stats/earned-run-average#:~:text=Earned%20run%20average%20represents%20the,error%20or%20a%20passed%20ball.&text=The%20formula%20for%20finding%20ERA,x%20earned%20runs%20%2F%20innings%20pitched.',
            target='_blank'),


    
     html.H4('About this Project'),
      dcc.Markdown('''
    * Project created by Lloyd Hill for a MA 705 Data Science course.
                 '''),
       ])

@app.callback(
    Output(component_id = "table_div", component_property = "children"),
    [Input(component_id = "year_dropdown", component_property = "value")]
)

def update_table(year):
    x = df.YEAR == int(year)
    return generate_table(df[x])

@app.callback(
    Output(component_id = "H v AB", component_property = "figure"),
    [Input(component_id = "year_dropdown", component_property = "value")]
)

def update_plot(year):
    df2 = pd.DataFrame(df, columns = ['YEAR', 'H', 'AB', 'SLG', 'NAME'])
    df2 = df2[df2.YEAR == int(year)]
    fig = px.scatter(df2, x="AB", y="H", size="SLG", color="NAME", hover_name="NAME", log_x=True, size_max=60)
    return fig



####################

@app.callback(
    Output(component_id = "Hitter_visual_2", component_property = "figure"),
    [Input(component_id = "year_dropdown2", component_property = "value"),
     Input(component_id = "hitter_visual_dropdown", component_property = "value")]
)

def update_plot(year2, stat):
    df4 = pd.DataFrame(df, columns = ['YEAR', 'H', 'G', 'AB', 'SLG', 'NAME', 'SB', 'R', '2B', '3B', 'HR', 'RBI', 'BB', 'AVG', 'OBP', 'SLG', 'K', 'SB', 'CS'])
    df4 = df4[df4.YEAR == int(year2)]
    fig2 = px.bar(df4, x="NAME", y=stat, hover_name = "YEAR")
    fig2.update_traces(marker_color= 'blue')
    return fig2
#######################



@app.callback(
    Output(component_id = "table_div1", component_property = "children"),
    [Input(component_id = "year_dropdown1", component_property = "value")]
)

def update_table(year1):
    y = dfp.YEAR == int(year1)
    return generate_table(dfp[y])

@app.callback(
    Output(component_id = "APP v IP", component_property = "figure"),
    [Input(component_id = "year_dropdown1", component_property = "value")]
)

def update_plot(year1):
    df3 = pd.DataFrame(dfp, columns = ['APP', 'IP', 'K/9', 'YEAR', 'NAME'])
    df3 = df3[df3.YEAR == int(year1)]
    fig1 = px.scatter(df3, x="APP", y="IP", size="K/9", color="NAME", hover_name="NAME", log_x=True, size_max=60)
    return fig1

####################

@app.callback(
    Output(component_id = "pitcher_visual_2", component_property = "figure"),
    [Input(component_id = "year_dropdown3", component_property = "value"),
     Input(component_id = "pitcher_visual_dropdown", component_property = "value")]
)

def update_plot(year3, stat1):
    df5 = pd.DataFrame(dfp, columns = ['NAME','YEAR', 'APP', 'GS', 'W', 'L', 'SV', 'CG', 'IP', 'H', 'R', 'ER', 'BB', 'K', 'K/9', 'HR', 'ERA'])
    df5 = df5[df5.YEAR == int(year3)]
    fig3 = px.bar(df5, x="NAME", y=stat1, hover_name = "YEAR")
    fig3.update_traces(marker_color='blue')
    return fig3
#######################
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)


