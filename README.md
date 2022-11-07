#Scratch project tracker#
##About#
Scratch is a block-based programming site that is used to help children learn to
code, made by MIT. In scratch, a series of scripts is called a <u>project</u>.

Scratch project tracker is a set of scripts to track the trends and views of
scratch projects using the scratch API. A simple GUI using tkinter is available 
and so is a CLI interface. In both interfaces, the results from the API call are
stored so a line chart using plotly can be made.

##Requirements and dependencies##
* The default, built in requests module
* tkinter, also build-in
* plotly, install by using the command 'pip install plotly'
* pandas, a plotly dependency. Installed py using 'pip install pandas'
##Installation##
1. Download and unzip the repository
2. Run the setup.py script in scripts
3. Install plotly and pandas by typing in their commands into powershell/shell
##Usage##
To use the GUI, run the file main.py
To use the CLI, type in the command 'python cli.py <project id>' where
<projectn id> is replaced by the project id you wish to use