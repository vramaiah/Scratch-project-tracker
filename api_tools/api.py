import os

import requests


def make_call(project_id):
    """
    Makes an API call to the scratch API
    :param project_id: int
    :return: dict
    """
    url = f"https://api.scratch.mit.edu/projects/{project_id}"
    raw_response = requests.get(url)
    response = raw_response.json()
    return response


def show_results(response, command, from_cli=False):
    """
    Prints the results
    :param from_cli: bool
    :param command: function
    :param response: dict
    :return: None
    """
    stats = response['stats']
    command(f"Project title: {response['title']}")
    command(f"Project author: {response['author']['username']}")
    try:
        command("This project is a remix,"
                + f" originally made by {response['remix']['author']}")
    except KeyError:
        command("This project is not a remix of another project.")
    if from_cli:
        char = '\t'
        command("Stats:")
    else:
        char = ''
    command(f"{char}Views: {stats['views']}")
    command(f"{char}Loves: {stats['loves']}")
    command(f"{char}Favorites: {stats['favorites']}")
    command(f"{char}Remixes: {stats['remixes']}")


def save_call(project_id, response):
    """
    Saves the API call
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
