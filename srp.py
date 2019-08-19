"""
Single Responsibility Principle: Each class should have only one job
"""

import uuid

class Person:
    def __init__(self, name, description):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description

    def get_name(self):
        return self.name


class PersonDB:
    def __init__(self):
        self._people = []
    
    def create(self, person):
        self._people.append(person)

    def person_count(self):
        return len(self._people)

person = Person("Dan", "Programmer")
print(person.get_name())

personDB = PersonDB()
personDB.create(person)
print(personDB.person_count())
