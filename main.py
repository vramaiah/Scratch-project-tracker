import _tkinter
import tkinter as tk
from tkinter import ttk as ttk
from tkinter.messagebox import showerror as show_error

from api import make_call


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
        self.reset()

    def call_api(self):
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

    def reset(self):
        self.project_id.set(732702999)
        self.project_id_input.grid(row=1, column=0)
        self.action_button.grid(row=2, column=0)


root = tk.Tk()
frame = ScratchProjectApp(root)
frame.mainloop()
