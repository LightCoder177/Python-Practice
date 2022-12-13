#Dict within dict(Also know as complex data structure.)

#importing pprint module. 

import pprint

#dict

people = {'Ford': {'Name': "Ford Prefect",
                   'Gender': "Male",
                   'Occupation': "Researcher",
                   'Home Planet': "Betelgeuse Home"},

          'Arthur': {'Name': "Arthur Dent", 
                     'Gender': "Male", 
                     'Occupation': "Sandwich-Maker",
                     'Home Planet': "Earth"},
          
          'Trillian': {'Name': "Tricia McMillan",
                       'Gender': 'Female',
                       'Occupation': 'Mathematician',
                       'Home Planet': 'Earth'},

            'Robot': {'Name': "Marvin",
                      'Gender': "Unknown",
                      'Occupation': "Paranoid Android",
                      'Home Planet': "Unknown"}
}

#Execution

pprint.pprint(people)