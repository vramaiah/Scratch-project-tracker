from sys import argv

from api_tools import make_call, save_call, plot_data, show_results

if __name__ == '__main__':
    results = make_call(argv[1])  # Makes API call
    save_call(project_id=argv[1], response=results)
    plot_data(argv[1])  # Plots the data from the calls
    show_results(results)  # Shows the results of the call