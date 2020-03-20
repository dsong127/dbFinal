import plotly.figure_factory as ff

fips = ['41029', '41033', '41051',
        '41017', '41039', '41019',
        '41043', '41011', '41003',
        '41035', '41071', '41031',
        '41015', '41047', '41005', '41037', '41067']
values = ['01.Jackson - 343', '02.Josephine - 81', '04.Multnomah - 29',
          '03.Deschutes - 24', '07.Lane - 23', '05.Douglas - 17',
          '08.Linn - 14', '06.Coos - 13', '12.Benton - 8',
          '11.Klamath - 8', '14.Yamhill - 7', '15.Jefferson - 6',
          '17.Curry - 3', '09.Marion - 3', '10.Clackamas - 8', '16.Lake - 2', '13.Washington- 1']

colorscale = ["#d12111", '#d15711', '#d19711', '#d19711','#d19711','#dec826','#dec826',
              '#dec826', '#c9e041', '#c9e041', '#c9e041', '#c9e041', '#9ee041', '#9ee041', '#9ee041', '#9ee041', '#9ee041']

fig = ff.create_choropleth(fips=fips, values=values, scope=['OR'],
                           colorscale=colorscale,
                           title='Felonies + Misdemeanors by county',
                           state_outline={'width': 1},
                           legend_title='Counties',
                            county_outline={'color': 'rgb(15, 15, 55)', 'width': 0.5,},
)
fig.layout.template = None
fig.show()


# import plotly.graph_objects as go
#
#
# labels = ['Felony','Misdemeanor','Infraction','Violation', 'Procedural Matters']
# values = [250, 147, 45, 129, 12]
#
# fig = go.Figure(data=[go.Pie(labels=labels, values=values, title="Violation types in Expunge Project Dataset")])
# fig.show()

