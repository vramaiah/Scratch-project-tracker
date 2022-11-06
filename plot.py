import plotly.express as pk

from webbrowser import open as open_tab

def plot_data(project_id, open_plot=False):
    """
    Makes a views plot for project with id project_id
    :param project_id: int
    :return: str
    """
    views = []
    with open(f'data/project_{project_id}.txt') as file:
        for line in file:
            views.append(line.rstrip())
    fig = pk.line(x=range(len(views)), y=views, markers=True)
    fig.write_html('plot.html')
    if open_plot:
        open_tab('plot.html', new=2)