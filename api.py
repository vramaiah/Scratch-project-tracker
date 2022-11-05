import requests
from sys import argv


def make_call(project_id):
    raw_response = requests.get(f"https://api.scratch.mit.edu/projects/{project_id}")
    response = raw_response.json()
    return response


def show_results(response, make_line=False):
    stats = response['stats']
    if make_line:
        print('-' * (len(response['title'])+14))
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


if __name__ == '__main__':
    results = make_call(argv[1])
    show_results(results)
