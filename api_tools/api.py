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

