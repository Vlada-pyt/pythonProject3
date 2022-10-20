class Person:
    def __init__(self, room, street, city, country, planet, population):
        self.room = room
        self.street = street
        self.city = city
        self.country = country
        self.planet = planet
        self.population = population

    def get_person_room(self):
        return self.room

    def get_city_population(self):
        return self.population


person = Person()