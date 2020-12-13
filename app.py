import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div()
app.layout = html.Div(className="pokedex",
                      children=[
                          html.Div(className='left',
                                   children=[
                                       html.Div(className='logo'),
                                       html.Div(className='bg_curve1_left'),
                                       html.Div(className='bg_curve2_left'),
                                       html.Div(className='curve1_left',
                                                children=[
                                                    html.Div(className="buttonGlass",
                                                             children=[
                                                                 html.Div(className='reflect')
                                                             ]),
                                                    html.Div(className='miniButtonGlass1'),
                                                    html.Div(className='miniButtonGlass2'),
                                                    html.Div(className='miniButtonGlass3'),
                                                ]),
                                       html.Div(className='curve2_left',
                                                children=[
                                                    html.Div(className='junction',
                                                             children=[
                                                                 html.Div(className='junction1'),
                                                                 html.Div(className='junction2')
                                                             ])
                                                ]),
                                       html.Div(className='screen',
                                                children=[
                                                    html.Div(className='topPicture',
                                                             children=[
                                                                 html.Div(className='buttontopPicture1'),
                                                                 html.Div(className='buttontopPicture2')
                                                             ]),
                                                    html.Div(className='picture',
                                                             children=[
                                                                 html.P("<Pokemon picture>")
                                                             ]),
                                                    html.Div(className='buttonbottomPicture'),
                                                    html.Div(className='speakers',
                                                             children=[
                                                                 html.Div(className="sp"),
                                                                 html.Div(className="sp"),
                                                                 html.Div(className="sp"),
                                                                 html.Div(className="sp"),
                                                             ]),

                                                ])
                                   ]),
                          html.Div(className='right',
                                   children=[
                                       html.Div(className='stats',
                                                children=[
                                                    html.B("Nom:"),
                                                    html.Br(),
                                                    html.B("Type:"),
                                                    html.Br(),
                                                    html.B("Taille:"),
                                                    html.Br(),
                                                    html.B("Poids:"),
                                                ]),
                                       html.Div(className='blueButtons1',
                                                children=[
                                                    html.Div(className='blueButton'),
                                                    html.Div(className='blueButton'),
                                                    html.Div(className='blueButton'),
                                                    html.Div(className='blueButton'),
                                                    html.Div(className='blueButton'),
                                                ]),
                                       html.Div(className='blueButtons2',
                                                children=[
                                                    html.Div(className='blueButton'),
                                                    html.Div(className='blueButton'),
                                                    html.Div(className='blueButton'),
                                                    html.Div(className='blueButton'),
                                                    html.Div(className='blueButton'),
                                                ]),
                                       html.Div(className='miniButtonGlass4'),
                                       html.Div(className='miniButtonGlass5'),
                                       html.Div(className='barbutton3'),
                                       html.Div(className='barbutton4'),
                                       html.Div(className='cross',
                                                children=[
                                                    html.Div(className='leftcross',
                                                             children=[
                                                                 html.Div(className='leftT')
                                                             ]),
                                                    html.Div(className='topcross',
                                                             children=[
                                                                 html.Div(className='upT')
                                                             ]),
                                                    html.Div(className='rightcross',
                                                             children=[
                                                                 html.Div(className='rightT')
                                                             ]),
                                                    html.Div(className='midcross',
                                                             children=[
                                                                 html.Div(className='midCircle')
                                                             ]),
                                                    html.Div(className='botcross',
                                                             children=[
                                                                 html.Div(className='downT')
                                                             ]),
                                                ]),
                                       html.Div(className='bg_curve1_right'),
                                       html.Div(className='bg_curve2_right'),
                                       html.Div(className='curve1_right'),
                                       html.Div(className='curve2_right'),
                                   ])
                      ])

if __name__ == '__main__':
    app.run_server(debug=True)