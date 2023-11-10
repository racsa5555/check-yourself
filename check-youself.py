class Auto:
    def ride(self):
        print('Riding on a ground')

class Boat:
    def swim(self):
        print('Floating on water')

class Amphibian(Boat,Auto):
    pass

obj = Amphibian()
obj.ride()
obj.swim()


class ContactList(dict):

    def __init__(self,list_):
        self.list = list_
    def search_by_name(self,name):
        mas = []
        for x in self.list:
            if name in x:
                mas.append(x)
        return mas

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
print(all_contacts.search_by_name('Olya'))
