import requests

from sys import argv

from os import path

from plot import plot_data


def make_call(project_id):
    """
    Makes an API call to the scratch API
    :param project_id: int
    :return: dict
    """
    raw_response = requests.get(f"https://api.scratch.mit.edu/projects/{project_id}")
    response = raw_response.json()
    return response


def show_results(response):
    """
    Prints the results
    :param response: dict
    :return: None
    """
    stats = response['stats']
    print(f"Project title: {response['title']}")
    print(f"Project author: {response['author']['username']}")
    try:
        print(f"Remix: {response['remix']['author']}")
    except KeyError:
        print("This project is not a remix of another project.")
    print("Stats:")
    print(f"\tViews: {stats['views']}")
    print(f"\tLoves: {stats['loves']}")
    print(f"\tFavorites: {stats['favorites']}")
    print(f"\tRemixes: {stats['remixes']}")


def save_call(project_id, response):
    """
    Saves the API call
    :return: None
    """
    filename = f"data/project_{project_id}.txt"  # Sets the filename
    # Checks if the data file exists
    if not path.exists(filename):
        # If it does not, then create a new one
        with open(filename, 'w') as f:
            f.write(str(response['stats']['views']))
    else:
        # Otherwise, append the most recent number of views to it
        with open(filename, 'a') as f:
            f.write(f"\n{response['stats']['views']}")


if __name__ == '__main__':
    results = make_call(argv[1])  # Makes API call
    save_call(project_id=argv[1], response=results)
    plot_data(argv[1])  # Plots the data from the calls
    show_results(results)  # Shows the results of the call
