"""Set of scripts for handling storing and loading API calls"""
import os


def load_call(project_id):
    """
    Loads the data for project with ID project_id
    :param project_id: int
    :return: tuple
    """
    views, favorites, loves, remixes = ([], [], [], [])
    with open(f'data/project_{project_id}.txt') as file:
        for line in file:
            line_data = line.rstrip().split(',')
            views.append(line_data[0])
            favorites.append(line_data[1])
            loves.append(line_data[2])
            remixes.append(line_data[3])
    return views, favorites, loves, remixes

def save_call(project_id, response):
    """
    Saves the response, response in a file
    :param response: dict
    :param project_id: int
    :return: None
    """
    filename = f"data/project_{project_id}.txt"  # Sets the filename
    # Checks if the data file exists
    write_contents = str(response['stats']['views'])
    write_contents += ','
    write_contents += str(response['stats']['favorites'])
    write_contents += ','
    write_contents += str(response['stats']['loves'])
    write_contents += ','
    write_contents += str(response['stats']['remixes'])
    if not os.path.exists(filename):
        # If it does not, then create a new one
        with open(filename, 'w') as f:
            f.write(write_contents)
    else:
        # Otherwise, append the most recent number of views to it
        with open(filename, 'a') as f:
            f.write(f"\n{write_contents}")
