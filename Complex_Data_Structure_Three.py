#Complex data structure. 

#importing pprint submodule from pprint

from pprint import pprint

#dict

people = dict()

#Arthur details
people['Ford'] = dict(Name = "Ford Prefect", Gender = "Male", Occupation = "Researcher", Home_Planet = "Betelgeuse Seven")

#Ford details
people['Arthur'] = dict(Name = "Arthur Dent", Gender = "Male", Occupation = "Sandwich-Maker", Home_Planet = "Earth")

#Trillan details
people['Trillan'] = dict(Name = "Tricia Millan", Gender = "Female", Occupation = "Researcher", Home_Planet = "Earth")

#Robot details.

people['Robot'] = dict(Name = "Marvin", Gender = "Robot Male", Occupation = "Paranoid Android", Home_Planet = "Unknown")

pprint(people)

print(people['Arthur']['Home_Planet'])

print()

for repeat, count in people['Ford'].items():
    print(repeat,":", count)
    