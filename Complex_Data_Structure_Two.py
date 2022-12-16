#Complex data structure aka dict within a dict.

#importing pprint submodule from pprint module.

from pprint import pprint

#dict

people = dict()

people['Ford'] = {'Name': "Ford Prefect", 'Gender': "Male", 'Occupation': "Researcher", 'Home Planet': "Betelguese Seven"}
people['Arthur'] = {'Name': "Arthur Dent", 'Gender': "Male", 'Occupation': "Sandwich-Maker", 'Home Planet': "Earth"}
people['Trillan'] = {'Name': "Tricia Millan", 'Gender': "Female", 'Occupation': "Mathematician", 'Home Planet': "Earth"}
people['Robot'] = {'Name': "Marvin", 'Gender': "Robot Male", 'Occupation': "Paranoid Android", 'Home Planet': "Unknown"}

pprint(people)

print(people['Robot']['Occupation'])