def get_lollipop_graph (csv_europe_country_mean):

    return {'data': [
                {
                    'x': csv_europe_country_mean['Country'],
                    'y': csv_europe_country_mean['Year'],
                    'text': csv_europe_country_mean['Year'],
                    'hoverinfo': 'text',
                    'type': 'scatter',
                    'mode': 'markers',
                    'error_y': {
                        'type': 'data',
                        'symmetric': False,
                        'arrayminus': csv_europe_country_mean['Year'] ,
                        'array': [0] * len(csv_europe_country_mean['Year'] ),
                        'width': 0
                    },
                    'marker': {
                        'size': 8
                    }
                },
            ], 'layout': {'yaxis': {'title': 'Year sunshine average by Country'},'xaxis': {'title': 'Country'}}}