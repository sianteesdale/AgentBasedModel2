# ABM-Assignment-2
ABM Assignment 2 for Leeds Module: Programming for Social Sciences

This repository contains all of the relevant information for the ‘Planning for Drunks’ agent-based model (ABM). This model simulates the movement of drunks from the pub (in the centre of the town) to their homes. Each drunk person is given a unique ID, which they have to match to their house number (e.g., drunk person number 10 has to find house number 10), this causes the drunk person to stop walking.  This simulation will continue to loop until all 25 drunk people find their homes from the pub.


The model is written using a Python script, therefore, an appropriate Python software must be used, e.g. Spyder, which was used to develop this ABM. Spyder can be used via downloading the [Anaconda Navigator](https://www.anaconda.com/download/), where you can select the correct operating system for your PC and download.

To run the model, all Python scripts within this folder must be opened on Spyder. These are ‘model.py’ and ‘drunkframework.py’, with the latter involving the relevant Class code for the drunks that will be used in the model. 
Once both scripts are open, run the ‘model.py’ code (in Spyder this is done by pressing F5) and the code will output a text file called ‘density.txt’ in the folder, and also a picture - this picture shows the movements of the drunk people across town before they reach their homes, with the lighter colours showing the most walked areas. This image is normally defaulted to show in the console of Spyder; to make it display on a pop-out window, run the following code in the console: 

%matplotlib qt

Also within this folder is ‘drunk.txt’ which has all of the environment data required for the town, with 1’s denoting the pub, denominations of 10’s denoting the houses in which the drunks have to find, and 0’s representing empty space. Additionally, ‘UML.png’ shows a UML of the Class ‘Drunk’, illustrating the different methods and variables used to create ‘Drunk’.
