from webbrowser import open as open_tab

import plotly.graph_objects as go


def plot_data(project_id, open_plot=False):
    """
    Makes a views plot for project with id project_id
    :param open_plot: bool
    :param project_id: int
    :return: str
    """
    # Gets the data from the file
    views, favorites, loves, remixes = ([], [], [], [])
    with open(f'data/project_{project_id}.txt') as file:
        for line in file:
            line_data = line.rstrip().split(',')
            views.append(line_data[0])
            favorites.append(line_data[1])
            loves.append(line_data[2])
            remixes.append(line_data[3])
    x_axis = list(range(1, len(views)))
    # Plots the data
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x_axis,
        y=remixes,
        name='Remixes',
        mode='lines+markers',
        marker={'color': 'rgb(66, 245, 105)'},
        hovertemplate='%{y} remixes'))
    fig.add_trace(go.Scatter(
        x=x_axis,
        y=favorites,
        name='Favorites',
        mode='lines+markers',
        marker={'color': 'rgb(245, 188, 66)'},
        hovertemplate='%{y} favorites'))
    fig.add_trace(go.Scatter(
        x=x_axis,
        y=loves,
        name='Loves',
        mode='lines+markers',
        marker={'color': 'rgb(245, 69, 66)'},
        hovertemplate='%{y} loves'))
    fig.add_trace(go.Scatter(
        x=x_axis,
        y=views,
        name='Views',
        mode='lines+markers',
        marker={'color': 'rgb(64, 139, 237)'},
        hovertemplate='%{y} views'))
    fig.update_layout(legend_title_text="Stat")
    fig.update_xaxes(title_text="Lookup number")
    fig.update_yaxes(title_text="Number")
    fig.update_layout(title=f'Stats for project {project_id}')
    fig.write_html('plot.html')  # Saves the plot
    # Opens the plot if specified
    if open_plot:
        open_tab('plot.html', new=2)
