import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['django', 'flask', 'requests']

plot_dicts = [
    {'value': 16101, 'label': 'Description of django.'},
    {'value': 15208, 'label': 'Description of flask.'},
    {'value': 14798, 'label': 'Description of requests.'},
]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
