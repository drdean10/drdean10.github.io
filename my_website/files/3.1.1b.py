#name1 = 'Derek'
#name2 = 'Jacque'

# Get the directory name for data files
import os.path
directory = os.path.dirname(os.path.abspath(__file__)) 

#initialize the aggregators
years1=[]
number_of_people1=[]
years2=[]
number_of_people2=[]

# Prompt user for desired state
print ('This program helps you pick a baby name based on popularity data for the past 100+ years.')
print ('\nType first name you are interested in. \nBe sure to capitalize only the first letter.')
name1 = raw_input('Type a boys name: ')
name2 = raw_input('Type a girls name: ')

# Scan one year's file at a time
# for year in range(1880, 2012):
# Open the file
filename = os.path.join(directory, 'CA' + '.TXT')
datafile = open(filename, 'r')
# Go through all the names that year
for line in datafile:
    state, gender, year, name, number = line.split(',')
    # Aggregate based on name1
    if name == name1 and gender == 'M':
        years1.append(year)
        number_of_people1.append(number) 
    #Aggregate based on name2
    if name == name2 and gender == 'F':
        years2.append(year)
        number_of_people2.append(number) 
# Close that year's file
datafile.close()

# Plot on one set of axes.
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
ax.plot(years1, number_of_people1, '#0000FF')
ax.plot(years2, number_of_people2, '#FF0000')

graphtitle = 'U.S. Babies Named ' + name1 + ' (blue) or ' + name2 +' (red).'   
#ax.set_title("U.S. Babies Named %s (blue) or %s (red).") % (name1, name2)
ax.set_title(graphtitle)
fig.show()