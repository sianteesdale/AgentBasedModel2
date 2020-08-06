# IMPORT LIBRARIES
import csv                      # Used to read in csv files and write them
import drunkframework           # Contains functions for the 'Agent' class
import matplotlib.pyplot as plt # Used for plotting


# CREATE VARIABLES
# With [] being empty lists that will be filled
density = []
town = []
drunks = []
num_of_drunks = 25 # defining the number of drunks in the simulation


# READ IN THE ENVIRONMENT
# Create a new text file to input the environment
f1 = open('drunk.txt', newline='')
# Read in the csv with environment data
reader = csv.reader(f1, quoting = csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []                # create an empty list for rowlist to enter information into
    for value in row:
        rowlist.append(value)   # add the value to a rowlist
    town.append(rowlist)        # append the rowlist to the town variable
# And close the text file
f1.close()

# CREATING THE NEW DENSITY LIST FROM THE ENVIRONMENT TEXT
# Create a new text file to input the environment
f2 = open('drunk.txt', newline='')
# Read in the csv with environment data
reader = csv.reader(f2, quoting = csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for value in row:
        # change the value to 0 for an empty 2d list, which the agents will change once they walk over the coordinate
        value = 0
        rowlist.append(value)
    density.append(rowlist)
# And close the text file
f2.close()

# FIND THE PUB LOCATION
# Pub are 1's in the environment
# As the environment is a 2d list, need to read each each row and values to find the 1's
# This will be used for the starting coordinates for the drunks
# For each row in the town list
for i, row in enumerate(town):
    # For each number in that row
    for j, num in enumerate(row):
        # If the number equals 1 (aka the pub)
        if num == 1:
            start_x, start_y = j, i # assign the numbers found to the starting coordinates


# CREATING THE DRUNKS
# Run the loop for all drunk people
for i in range(num_of_drunks):
    # Assign a unique ID, which will be used to find their home
    drunk_ID = ((i+1)*10)
    # Attach the drunks with the Class from drunkframework
    drunks.append(drunkframework.Drunk(density, drunk_ID, start_x, start_y))
    # While the coordinates of the drunks don't equal their home number
    while (town[drunks[i].y][drunks[i].x] != drunks[i].drunk_ID):
        drunks[i].move()        # make them move
        drunks[i].add_density() # add density to where they walk
        drunks[i].sick()        # make them sick
    # While loop will stop once the drunk has found their home (their coordinates matches their house number)
    print (town[drunks[i].y][drunks[i].x], drunks[i].drunk_ID)


# PLOTTING THE DENSITY MAP 
# Change the figure size
plt.figure(figsize=(14,14))
# Set the y and x-axis limits
plt.ylim(0, 300)
plt.xlim(0, 300)
# For the number of drunks, plot them on the density map
for i in range(num_of_drunks):
    plt.scatter(drunks[i].x,drunks[i].y, c="white", s=50)
# Show the density map
plt.imshow(density)


# WRITE THE DENSITY TEXT-FILE
# Save the density data as a text-file
with open('density.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    # For each row in the density list
    for row in density:
        # Write the row values into the density.txt file
        csvwriter.writerow(row)

