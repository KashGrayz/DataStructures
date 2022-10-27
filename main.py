    #  DATA STRUCTURES  #

#  // Task I \\

#Store the months of the year as strings. Determine the month in the data structure in which National Pi Day exists
#  and print that month to the console. 
# HINT: The number for Pi, when converted to an Integer, is related to the stored location of the correct month.

# from implementation import months_in_year
# from implementation import fav_fruits
# from implementation import user_profile
from implementation import close_family
# march = months_in_year[2]
# print(f"Pi day is the 14th of {march}")


# Store five fruits or vegetables.
# Add two of your favorite fruits and two of your favorite vegetables to the collection.
# Iterate over the collection and print each one to the console. 

# fav_fruits.update(['Coconut','Passionfruit','Tomato','Cucumber']) #add veggies to set

# for pulp in fav_fruits:  #iterate               
#     print(pulp) 


# Store information about a user profile. 
# Use literal string interpolation to print the user’s profile information to the console. 
# The profile should consist of the following information:
# First Name
# Last Name
# Email Address
# Phone Number

# print(f'''My name is {user_profile["first_name"]} {user_profile["last_name"]}, #interpolation for user profile
# you can contact me by {user_profile["email_addy"]} 
# or by phone {user_profile["phone_number"]}.''')

#  // Task II \\

#family =close_family(dict)

for dict_item in close_family:
    for key in dict_item:
        print(dict_item[key])
    
