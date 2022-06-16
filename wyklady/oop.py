"""

void hello(Person p) {
    sprintf("Hello, %s", p.name);
}

type struct person {
    name *char,
    surname *char
}

person p = person{name: "", surname: ""};
hello(p)

"""
import json

# Класс
class Person:
    def __init__(self, name, surname):
        if type(name) is not str:
            raise Exception()

        if name == 'Свиня':
            raise Exception()

        self.name = name
        self.surname = surname

    def hello(self):
        print(f"Hello, {self.name}")

    # returns this person encoded as json
    def json(self):
        return json.dumps({
            "name": self.name,
            "surname": self.surname
        })

    # Определяет поведение str, print и иже с ними
    def __str__(self):
        return f"Person(name={self.name}, surname={self.surname})"


# Полиморфизм -позволяет задавать свои функции, которые в нашем коде будут перекрывать дефолтные/существующие
str(12)
str(Person("Artem", "K"))



# Instance - объект класса Person
p = Person("1", "1")
p2 = Person("2", "2")

p.hello()
p2.hello()


if type(p) == type(p2) == Person:
    print('Correct')

########

json_string = p.json()


#######

class PersonStorage:
    def __init__(self):
        self.person_list = []

    def add_person(self, person):
        self.person_list.append(person)

    def remove_person(self, i):
        self.person_list.pop(i)

    def get_person(self, i):
        person = self.person_list[i]
        return person


class FilePersonStorage:
    def __init__(self, filename):
        self.filename = filename
        f = open(self.filename, 'rw')

        f.write(json.dumps([]))

        f.close()

    def add_person(self, person):
        f = open(self.filename, 'rw')
        line = f.readline()

        data = json.loads(line)
        data.append(person)

        json_string = json.dumps(data) # flask jsonify()

        f.write(json_string)
        f.close()

    def remove_person(self, i):
        f = open(self.filename, 'rw')
        line = f.readline()

        data = json.loads(line)
        data.pop(i)

        json_string = json.dumps(data)

        f.write(json_string)
        f.close()

    def get_person(self, i):
        f = open(self.filename, 'rw')
        line = f.readline()

        data = json.loads(line)

        f.close()

        return data[i]
########


# Абстракция - возможность прятать сложное там, где нам это нужно
# Мы абстрагировались от списка с людьми
# Где именно хранятся люди нас не интересует
# PersonStorage использует список, но код ниже об этом ничего не знает и знать не должен
ps = FilePersonStorage("person.json")
# ps = PersonStorage()

ps.add_person(p)
ps.add_person(p2)
ps.remove_person(1)
print(ps.get_person(0))