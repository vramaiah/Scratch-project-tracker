import requests

from sys import argv

from os import path

def make_call(project_id):
    raw_response = requests.get(f"https://api.scratch.mit.edu/projects/{project_id}")
    response = raw_response.json()
    return response


def show_results(response):
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
    saves the API call
    :return: None
    """
    if not path.exists(f"data/project_{project_id}.txt"):
        with open(f"data/project_{project_id}.txt", 'w') as f:
            f.write(str(response['stats']['views']))
    else:
        with open(f"data/project_{project_id}.txt", 'a') as f:
            f.write(f"\n{response['stats']['views']}")


if __name__ == '__main__':
    results = make_call(argv[1])
    save_call(project_id=argv[1], response=results)
    show_results(results)
