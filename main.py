import _tkinter
import tkinter as tk
from tkinter import ttk as ttk
from tkinter.messagebox import showerror as show_error

from webbrowser import open as open_tab

from api import make_call, save_call

from plot import plot_data


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
        super().__init__(master)
        self.grid()
        # initialize variables
        self.project_id = tk.IntVar()
        self.response = None
        # Make widgets
        self.status_label = ttk.Label(master=self, text="Project id")
        self.status_label.grid(row=0, column=0)
        self.action_button = ttk.Button(
            master=self,
            text='Go',
            command=self.call_api
        )
        self.project_id_input = ttk.Entry(master=self, textvariable=self.project_id)
        self.open_project_button = ttk.Button(
            master=self,
            text='Open project',
            command=self.open_project_in_browser
        )
        self.open_project_button.grid(row=3, column=0)
        self.open_trend_button = ttk.Button(
            master=self,
            text='Open graph',
            command=self.open_plot
        )
        self.open_trend_button.grid(row=4, column=0)
        self.reset()

    def call_api(self):
        """
        Calls the API and handles errors
        :return: None
        """
        try:
            self.response = make_call(self.project_id.get())
        except _tkinter.TclError:
            show_error(title='Error', message="Improper input for project id")
            self.reset()
        else:
            if self.response.get('code') == 'NotFound':
                show_error(title='Error', message='Project is non-existent')
                self.reset()
            else:
                save_call(self.project_id.get(), self.response)
                self.display_results()

    def display_results(self):
        """
        Displays the results of the API call
        Assumes that the API call is made successfully
        :return: None
        """
        self.action_button.destroy()
        self.project_id_input.destroy()
        self.status_label['text'] = f"Project title: {self.response['title']}"
        self.status_label['text'] += f"\nProject author: {self.response['author']['username']}"
        try:
            print(f"\nRemix: {self.response['remix']['author']}")
        except KeyError:
            self.status_label['text'] += "\nThis project is not a remix of another project."
        self.status_label['text'] += f"\nViews: {self.response['stats']['views']}"
        self.status_label['text'] += f"\nLoves: {self.response['stats']['loves']}"
        self.status_label['text'] += f"\nFavorites: {self.response['stats']['favorites']}"
        self.status_label['text'] += f"\nRemixes: {self.response['stats']['remixes']}"

    def open_plot(self):
        plot_data(self.project_id.get(), True)

    def open_project_in_browser(self):
        """
        Opens the project with the project ID in a browser
        :return: None
        """
        project_id = self.project_id.get()
        open_tab(f'https://scratch.mit.edu/projects/{project_id}', new=2)

    def reset(self):
        """Resets the project to the state it was as the beginning"""
        self.project_id.set(732702999)
        self.project_id_input.grid(row=1, column=0)
        self.action_button.grid(row=2, column=0)
        self.response = None


root = tk.Tk()
frame = ScratchProjectApp(root)
frame.mainloop()
