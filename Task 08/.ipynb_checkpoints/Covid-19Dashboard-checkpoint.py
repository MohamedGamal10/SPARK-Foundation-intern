#import libraries
import numpy as np                                                      #for fast operations on arrays    
import pandas as pd                                                     #for read & manipulate dataset
import plotly.graph_objs as go                                          #for Data visualization
import plotly.offline as pyo                                            #for Data visualization
import dash                                                             #for Dashboard visualization
from dash import dcc                                                    #for Dashboard visualization
from dash import html                                                   #for Dashboard visualization
from dash.dependencies import Input, Output                             #for Dashboard visualization
import warnings
warnings.filterwarnings('ignore')

#load dataset
dataset = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
df = dataset.copy()

df = df[['location','date','total_cases','new_cases','total_deaths','new_deaths','people_vaccinated',
        'people_fully_vaccinated','population','median_age','aged_65_older','aged_70_older',
        'diabetes_prevalence','female_smokers','male_smokers']]


#Dashboard
app = dash.Dash()

app.layout = html.Div([
                        html.Div(id = 'row1',children=[
                            
                            html.Div(id ='country-div',children=[
                                html.Div(id='country-name',style={'font-weight': 'bold','font-size':'60px'},children='Egypt'),
                                dcc.Dropdown(id='all-contries',value='Egypt',options=[{'label': i, 'value': i} for i in df['location'].unique().tolist()],style={'margin-top':'25px'})
                                                                ],style={'display':'inline-block','width':'15%','height':'15%'}),
                            html.Div(id = 'Fixed-Data-div',children=[
                                html.Div(children=['Date',html.Div(id='Date',children='20',style={'margin':'20px','font-weight': 'bold','font-size':'15px'})],style={'width':'15%','background-color':'#FAEEE7','border':'1px solid black','height':'80px','margin':'10px','border-radius': '25px','text-align': 'center','font-weight': 'bold','font-size':'15px'}),
                                html.Div(children=['Population',html.Div(id='Population',children='20',style={'margin':'20px','font-weight': 'bold','font-size':'15px'})],style={'width':'15%','background-color':'#FAEEE7','border':'1px solid black','height':'80px','margin':'10px','border-radius': '25px','text-align': 'center','font-weight': 'bold','font-size':'15px'}),
                                html.Div(children=['Median Age',html.Div(id='Median',children='20',style={'margin':'20px','font-weight': 'bold','font-size':'15px'})],style={'width':'15%','background-color':'#FAEEE7','border':'1px solid black','height':'80px','margin':'10px','border-radius': '25px','text-align': 'center','font-weight': 'bold','font-size':'15px'}),
                                html.Div(children=['Aged 65 Older',html.Div(id='Aged_65',children='20',style={'margin':'20px','font-weight': 'bold','font-size':'15px'})],style={'width':'15%','background-color':'#FAEEE7','border':'1px solid black','height':'80px','margin':'10px','border-radius': '25px','text-align': 'center','font-weight': 'bold','font-size':'15px'}),
                                html.Div(children=['Aged 70 Older',html.Div(id='Aged_70',children='20',style={'margin':'20px','font-weight': 'bold','font-size':'15px'})],style={'width':'15%','background-color':'#FAEEE7','border':'1px solid black','height':'80px','margin':'10px','border-radius': '25px','text-align': 'center','font-weight': 'bold','font-size':'15px'}),
                                html.Div(children=['Diabetes',html.Div(id='Diabetes',children='20',style={'margin':'20px','font-weight': 'bold','font-size':'15px'})],style={'width':'15%','background-color':'#FAEEE7','border':'1px solid black','height':'80px','margin':'10px','border-radius': '25px','text-align': 'center','font-weight': 'bold','font-size':'15px'}),
                                html.Div(children=['Female Smoker',html.Div(id='Female',children='20',style={'margin':'20px','font-weight': 'bold','font-size':'15px'})],style={'width':'15%','background-color':'#FAEEE7','border':'1px solid black','height':'80px','margin':'10px','border-radius': '25px','text-align': 'center','font-weight': 'bold','font-size':'15px'}),                                   
                                html.Div(children=['Male Smoker',html.Div(id='Male',children='20',style={'margin':'20px','font-weight': 'bold','font-size':'15px'})],style={'width':'15%','background-color':'#FAEEE7','border':'1px solid black','height':'80px','margin':'10px','border-radius': '25px','text-align': 'center','font-weight': 'bold','font-size':'15px'}),
                                
                                                                    ],style={'display':'inline-flex','width':'84%'})
                                                      ]),
                        
                        html.Div(id='row2',children=[
                            html.Div(children=[
                                html.Div(dcc.Graph(id='Pie1', config= {'displaylogo': False}),style={'border':'1px solid black','margin':'30px'}),
                                html.Div(dcc.Graph(id='Pie2', config= {'displaylogo': False}),style={'border':'1px solid black','margin':'30px'})

                            ],style={'display':'inline-flex'}),
                            html.Div(dcc.Graph(id='Scatter1', config= {'displaylogo': False}),style={'border':'1px solid black','margin-top':'20px'}),
                            html.Div(dcc.Graph(id='Bar1', config= {'displaylogo': False}),style={'border':'1px solid black','margin-top':'20px'})


                                                    ],style={'margin-top':'20px'})
                        
                       ],id='container',style={'background-color':'#24A19C','border-radius': '10px'})



@app.callback(
    Output(component_id='country-name', component_property='children'),
    Output(component_id='Date', component_property='children'),
    Output(component_id='Population', component_property='children'),
    Output(component_id='Median', component_property='children'),
    Output(component_id='Aged_65', component_property='children'),
    Output(component_id='Aged_70', component_property='children'),
    Output(component_id='Diabetes', component_property='children'),
    Output(component_id='Female', component_property='children'),
    Output(component_id='Male', component_property='children'),
    [Input(component_id='all-contries', component_property='value')]
)
def country_selection_Fixed(input_value):
    date = df[df['location']==input_value].tail(1)['date'].tolist()[0]
    try : 
        Population = df[df['location']==input_value].tail(1)['population'].tolist()[0] 
    except: 
        Population = '-'

    try : 
        Median = df[df['location']==input_value].tail(1)['median_age'].tolist()[0]
    except:
        Median='-'

    try : 
        persentage_aged_65 = df[df['location']==input_value].tail(1)['aged_65_older'].tolist()[0]/100
        population_aged_65 = int(df[df['location']==input_value].tail(1)['population'].tolist()[0]*persentage_aged_65)
    except: population_aged_65 = '-'
    
    try:
        persentage_aged_70 = df[df['location']==input_value].tail(1)['aged_70_older'].tolist()[0]/100
        population_aged_70 = int(df[df['location']==input_value].tail(1)['population'].tolist()[0]*persentage_aged_70)
    except:
        population_aged_70 = '-'
    
    try:

        persentage_Diabetes = df[df['location']==input_value].tail(1)['diabetes_prevalence'].tolist()[0]/100
        population_Diabetes = int(df[df['location']==input_value].tail(1)['population'].tolist()[0]*persentage_Diabetes)
    except:
        population_Diabetes = '-'

    try:
        persentage_Female = df[df['location']==input_value].tail(1)['female_smokers'].tolist()[0]/100
        population_Female = int(df[df['location']==input_value].tail(1)['population'].tolist()[0]*persentage_Female)
    except:
        population_Female = '-'

    try:
        persentage_Male = df[df['location']==input_value].tail(1)['male_smokers'].tolist()[0]/100
        population_Male = int(df[df['location']==input_value].tail(1)['population'].tolist()[0]*persentage_Male)
    except:
        population_Male='-'

    return input_value, date, Population, Median, population_aged_65, population_aged_70, population_Diabetes, population_Female, population_Male



@app.callback(
    Output(component_id='Scatter1', component_property='figure'),
    [Input(component_id='all-contries', component_property='value')])

def country_selection_Scatter(input_value):
    snap = df[df['location']==input_value]
    trace0 = go.Scatter(x=snap['date'], y=snap['total_cases'],
                        mode='lines+markers',name='Total Cases')

    trace1 = go.Scatter(x=snap['date'], y=snap['new_cases'],
                        mode='lines+markers',name='New Cases')

    trace2 = go.Scatter(x=snap['date'], y=snap['total_deaths'],
                        mode='lines+markers',name='Total Deaths')

    trace3 = go.Scatter(x=snap['date'], y=snap['new_deaths'],
                        mode='lines+markers',name='New_Deaths')

    data = [trace0,trace1,trace2,trace3]

    return{
        'data': data,
        'layout': go.Layout(
            title='Time Series',
            xaxis={'title': 'Date'},
            yaxis={'title': 'Cases'},
            hovermode='closest',
            paper_bgcolor='#FFFDDE' 
        )
    }

@app.callback(
    Output(component_id='Bar1', component_property='figure'),
    [Input(component_id='all-contries', component_property='value')])

def country_selection_Bar(input_value):
    snap = df[df['location']==input_value]
    first = int(snap['people_vaccinated'].dropna().tail(1).tolist()[0])
    second = int(snap['people_fully_vaccinated'].dropna().tail(1).tolist()[0])
    trace0 = go.Bar(x=['People Vaccinated'], y=[first],name='Vaccinated')
    trace1 = go.Bar(x=['People Fully Vaccinated'], y=[second],name='Fully Vaccinated')
    data = [trace0,trace1]
    return{
        'data': data,
        'layout': go.Layout(
            title='Total vaccine',
            xaxis={'title': 'Category'},
            yaxis={'title': 'Total Numbers'},
            hovermode='closest',
            paper_bgcolor='#FFFDDE' 
        )
    }

@app.callback(
    Output(component_id='Pie1', component_property='figure'),
    [Input(component_id='all-contries', component_property='value')])

def country_selection_Pie1(input_value):
    snap = df[df['location']==input_value]
    persentage_aged_65 = snap.tail(1)['aged_65_older'].tolist()[0]/100
    population_aged_65 = int(snap.tail(1)['population'].tolist()[0]*persentage_aged_65)

    persentage_aged_70 = snap.tail(1)['aged_70_older'].tolist()[0]/100
    population_aged_70 = int(snap.tail(1)['population'].tolist()[0]*persentage_aged_70)

    remain_median = int(snap.tail(1)['population'].tolist()[0])-population_aged_65-population_aged_70

    trace0 = go.Pie(labels=['65 older','70 Older','Remain Median Age'], values=[population_aged_65,population_aged_70,remain_median])
    data = [trace0]
    return{
        'data': data,
        'layout': go.Layout(
            title='Ages',
            hovermode='closest',
            paper_bgcolor='#FFFDDE' 
        )
    }

@app.callback(
    Output(component_id='Pie2', component_property='figure'),
    [Input(component_id='all-contries', component_property='value')])

def country_selection_Pie2(input_value):
    snap = df[df['location']==input_value]
    persentage_Diabetes = snap.tail(1)['diabetes_prevalence'].tolist()[0]/100
    population_Diabetes = int(snap.tail(1)['population'].tolist()[0]*persentage_Diabetes)
    population_non_Diabetes = int(snap.tail(1)['population'].tolist()[0]) - population_Diabetes

    trace0 = go.Pie(labels=['Diabetes','Non Diabetes'], values=[population_Diabetes,population_non_Diabetes])
    data = [trace0]
    return{
        'data': data,
        'layout': go.Layout(
            title='Diabetes',
            hovermode='closest',
            paper_bgcolor='#FFFDDE' 
            
            
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)