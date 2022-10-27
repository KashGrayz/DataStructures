#Store the months of the year as strings. Determine the month in the data structure in which National Pi Day exists
#  and print that month to the console. 
# HINT: The number for Pi, when converted to an Integer, is related to the stored location of the correct month.

from implementation import months_in_year
from implementation import fav_fruits

# march = months_in_year[2]
# print(f"Pi day is the 14th of {march}")


# Store five fruits or vegetables.
# Add two of your favorite fruits and two of your favorite vegetables to the collection.
# Iterate over the collection and print each one to the console. 

fav_fruits.update(['Coconut','Passionfruit','Tomato','Cucumber']) #add veggies to set

for pulp in fav_fruits:  #iterate               
    print(pulp) 
