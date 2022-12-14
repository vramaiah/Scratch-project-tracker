from tkinter import TclError
import tkinter as tk
from tkinter import ttk as ttk
from tkinter.messagebox import showerror as show_error

from webbrowser import open as open_tab

from api_tools import make_call, save_call, plot_data, show_results


class ScratchProjectApp(tk.Frame):
    """
    A frame class for our scratch app
    """

    def __init__(self, master):
        """
        ScratchProjectApp(master) --> ScratchProjectApp
        Makes the frame of the scratch project tracker
        :param master: tk.Tk
        """
        # Sets up the window
        super().__init__(master)
        self.grid()
        # initialize variables
        self.project_id = tk.IntVar()
        self.response = None
        # Make widgets
        # Make status label
        self.status_label = ttk.Label(master=self, text="Project id")
        self.status_label.grid(row=0, column=0)
        # Makes button to call API
        self.action_button = ttk.Button(
            master=self,
            text='Go',
            command=self.call_api
        )
        # Makes an input for the project ID
        self.project_id_input = ttk.Entry(
            master=self,
            textvariable=self.project_id)
        self.open_project_button = ttk.Button(
            master=self,
            text='Open project',
            command=self.open_project_in_browser
        )
        self.open_project_button.grid(row=3, column=0)
        # Makes a button to open the graph of the project's views
        self.open_trend_button = ttk.Button(
            master=self,
            text='Open graph',
            command=self.open_plot
        )
        self.open_trend_button.grid(row=4, column=0)
        # Resets the window
        self.reset()

    def call_api(self):
        """
        Calls the API and handles errors
        :return: None
        """
        # Checks to see if the project ID is a number
        try:
            self.response = make_call(self.project_id.get())
        except TclError:
            show_error(title='Error', message="Improper input for project id")
            self.reset()
        else:
            # Checks if the project exists
            if self.response.get('code') == 'NotFound':
                # if id doesn't, user is shown an error and the window is reset.
                show_error(title='Error', message='Project is non-existent')
                self.reset()
            else:
                # Otherwise, the call is saves and the results displayed
                save_call(self.project_id.get(), self.response)
                self.display_results()

    def display_results(self):
        """
        Displays the results of the API call
        Assumes that the API call is made successfully
        :return: None
        """
        # Removes extra widgets
        self.action_button.destroy()
        self.project_id_input.destroy()
        # Shows project information
        self.status_label['text'] = ''
        show_results(self.response, command=self.add_line)

    def add_line(self, text):
        """
        Adds line text to output
        :param text: str
        :return: None
        """
        self.status_label['text'] += text + '\n'

    def open_plot(self):
        """
        Opens the plot in a new web browser tab
        :return:
        """
        try:
            plot_data(self.project_id.get(), True)
        except FileNotFoundError:
            show_error(
                'Error',
                'The project you are looking for has no associated data\n' +
                'Make an API call by clicking [go]')

    def open_project_in_browser(self):
        """
        Opens the project with the project ID in a browser
        :return: None
        """
        project_id = self.project_id.get()
        open_tab(f'https://scratch.mit.edu/projects/{project_id}', new=2)

    def reset(self):
        """
        Resets the project to the state it was at the beginning
        :return: None
        """
        self.project_id.set(732702999)
        self.project_id_input.grid(row=1, column=0)
        self.action_button.grid(row=2, column=0)
        self.response = None


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Scratch project tracker")
    frame = ScratchProjectApp(root)
    frame.mainloop()
