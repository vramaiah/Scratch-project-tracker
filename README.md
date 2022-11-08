# Scratch project tracker
## About
Scratch is a language developed by MIT, use to teach children the basics of
computer programming. In Scratch, one can make a _project_, which is a 
self-contained set of scripts used to command entitles called sprites.

Scratch project tracker tracks the views pf a project over time through a CLI
and a GUI. It can also show the stats of a project at the time of viewing.

## Dependencies
Scratch project tracker was made with python 3.10.2. If you have an earlier
version, the project may not work correctly. This project depends on the
following packages:
* os, builtin
* tkinter, built in
* webbrowser, built in
* requests, built-in
* plotly (install using `pip install --user plotly`)
* pandas (needed for plotly, install using `pip install --user plotly`)

## Installation
Simply download the project as a .zip (click the code button and an option to
download as a .zip should appear), or if you have git installed, enter the
command `git clone https://github.com/vramaiah/Scratch-project-tracker.git` into
a terminal. If you want, you can delete the .gitignore files (usually hidden in
a file browser)

Then run the script in scripts called package_installer.py to install the
packages, or manually install them using `pip install --user <package name>`.
The script can be run by typing in `python scripts/package_installer.py` into a
terminal.

## Usage
The GUI can be accessed by running main.py, and the cli can be accessed by
typing `python cli.py <project id>` into a terminal