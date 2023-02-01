import dash
import dash_bootstrap_components as dbc


from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('clean_data.csv')
Pro_cam=df['Product Company'].value_counts()
Pro_cam_name=Pro_cam.keys()
Proccessor_com=df['Proccessor Company'].value_counts()
Proccessor_com_name=Proccessor_com.keys()


app.layout = html.Div([
    dbc.Row([
        dbc.Col(
            html.H1('Mobile Data Analysis'),
        )
    ]),
    dbc.Row([
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='pie-chart',
                        figure=px.pie(
                    
                            names=Pro_cam_name,
                            values=Pro_cam,
                            hole=.3,
                            title='"Which Product Company has No of Mobile',
                            template='plotly_dark'
                        )
                    )
                ]),
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='pie-chart2',
                        figure=px.pie(
                    
                            names=Proccessor_com_name,
                            values=Proccessor_com,
                            hole=.3,
                            title='Which Proccessor Company has No of Mobile',
                            template='plotly_dark'
                        )
                    )
                ]),
        
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='histogram',
                        figure=px.histogram(
                    
                            x=df['Product Price'],
                            color=df['Product Company'],
                            title="Price Range with Mobile Company",
                            histnorm='percent',
                            template='plotly_dark'
                        )
                    )
                ]),
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='histogram2',
                        figure=px.histogram(
                    
                            df['Product Price'],
                            color=df['Proccessor Company'],
                            title="Price Range with Proccessor",
                            
                            template='plotly_dark'
                        )
                    )
                ]),
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='histogram3',
                        figure=px.histogram(
                    
                            df['Proccessor Company'],
                            color=df['Product Company'],
                            title="Company Using most often Processors",
                            
                            template='plotly_dark'
                        )
                    )
                ]),
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='histogram4',
                        figure=px.histogram(
                    
                            df['Proccessor'],
                            color=df['Product Company'],
                            title="Which Proccessor Used mostly Times",
                            
                            template='plotly_dark'
                        )
                    )
                ])
        ,dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='histogram5',
                        figure=px.histogram(
                    
                            df['Ram'],
                            color=df['Ram'],
                            title="Which Ram Used Mostly",
                            nbins=40,
                            template='plotly_dark'
                        )
                    )
                ])
        ,dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='histogram6',
                        figure=px.histogram(
                    
                            df['Display'],
                            color=df['Display'],
                            title="Which Display Used Mostly",
                            
                            template='plotly_dark'
                        )
                    )
                ]),
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='histogram7',
                        figure=px.histogram(
                    
                            df['Cameras Main'],
                            color=df['Cameras Main'],
                            title="Which Cameras Main Used Mostly",
                            
                            template='plotly_dark'
                        )
                    )
                ]),
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='histogram8',
                        figure=px.histogram(
                    
                            df['Cameras Front'],
                            color=df['Cameras Front'],
                            title="Which Cameras Front Used Mostly",
                            
                            template='plotly_dark'
                        )
                    )
                ]),
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='histogram9',
                        figure=px.histogram(
                            df['Battery'],
                            color=df['Battery'],
                            title="Which Battery Used Mostly",
                            template='plotly_dark'
                        )
                    )
                ])
        ,dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='histogram10',
                        figure=px.histogram(
                    
                            df['Display'],
                            color=df['Display'],
                            title="Which Display Used Mostly",
                            
                            template='plotly_dark'
                        )
                    )
                ])
    ])
])

if __name__ == '__main__':
 app.run_server()