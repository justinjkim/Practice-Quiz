from __future__ import division
capitals_dict = {
'Alabama' : 'Montgomery',
'Alaska' : 'Juneau',
'Arizona' : 'Phoenix',
'Arkansas' : 'Little Rock',
'California' : 'Sacramento',
'Colorado' : 'Denver',
'Connecticut' : 'Hartford',
'Delaware' : 'Dover',
'Florida' : 'Tallahassee',
'Georgia' : 'Atlanta',
'Hawaii' : 'Honolulu',
'Idaho' : 'Boise',
'Illinois' : 'Springfield',
'Indiana' : 'Indianapolis',
'Iowa' : 'Des Moines',
'Kansas' : 'Topeka',
'Kentucky' : 'Frankfort',
'Louisiana' : 'Baton Rouge',
'Maine' : 'Augusta',
'Maryland' : 'Annapolis',
'Massachusetts' : 'Boston',
'Michigan' : 'Lansing',
'Minnesota' : 'Saint Paul',
'Mississippi' : 'Jackson',
'Missouri' : 'Jefferson City',
'Montana' : 'Helena',
'Nebraska' : 'Lincoln',
'Nevada' : 'Carson City',
'New Hampshire' : 'Concord',
'New Jersey' : 'Trenton',
'New Mexico' : 'Santa Fe',
'New York' : 'Albany',
'North Carolina' : 'Raleigh',
'North Dakota' : 'Bismarck',
'Ohio' : 'Columbus',
'Oklahoma' : 'Oklahoma City',
'Oregon' : 'Salem',
'Pennsylvania' : 'Harrisburg',
'Rhode Island' : 'Providence',
'South Carolina' : 'Columbia',
'South Dakota' : 'Pierre',
'Tennessee' : 'Nashville',
'Texas' : 'Austin',
'Utah' : 'Salt Lake City',
'Vermont' : 'Montpelier',
'Virginia' : 'Richmond',
'Washington' : 'Olympia',
'West Virginia' : 'Charleston',
'Wisconsin' : 'Madison',
'Wyoming' : 'Cheyenne',
}

import random

capitals = list(capitals_dict.keys())
print("To quit playing, please type 'quit'.")
user_score = 0
total = 0
while True:
       	state = random.choice(capitals)
       	capital = capitals_dict[state]
       	user = raw_input("What is the capital of " + state + " ? > ")

       	if user == "quit":
       		print("Quitting...")
       		break
       	elif user == capital:
       		print("That's correct!")
       		user_score += 1
       		total += 1
       	else:
       		print("Not quite. The capital of " + state + " is " + capital + " .")
       		total += 1
final_score = user_score/total
print("You scored a " + str(user_score) + " out of " + str(total) + ". That's a " + str(final_score * 100) + "%.")
if (final_score * 100) > 85:
       	print("Great job! You really know your US history.")
elif (final_score * 100) <= 85 and (final_score*100) > 50:
       	print("Gotta study harder for next time!")
else:
       	print("Hmm...you're not very good at this.")
