class Zoo:
    def __init__(self, name, location, area, exhibits):
        self.name = name
        self.location = location
        self.area = area
        self.exhibits = exhibits


class Exhibit:
    def __init__(self, name, location, animals):
        self.name = name
        self.location = location
        self.animals = animals


class Animal:
    def __init__(self, species, scientific_name, age, sex):
        self.species = species
        self.scientific_name = scientific_name
        self.age = age
        self.sex = sex


moscow_zoo = Zoo(
    name="Московский зоопарк",
    location="Москва, ВДНХ",
    area=100000,
    exhibits=[
        Exhibit(
            name="Старая территория",
            location="Центральная часть зоопарка",
            animals=[
                Animal("Слон", "Elephas maximus", 20, "самец"),
                Animal("Тигр", "Panthera tigris", 10, "самка"),
                Animal("Лев", "Panthera leo", 5, "самец"),
            ],
        ),
        Exhibit(
            name="Новая территория",
            location="Восточная часть зоопарка",
            animals=[
                Animal("Гималайский медведь", "Ursus thibetanus", 15, "самка"),
                Animal("Жираф", "Giraffa camelopardalis", 10, "самец"),
                Animal("Медведь-губач", "Melursus ursinus", 5, "самка"),
            ],
        ),
        Exhibit(
            name="Остров зверей",
            location="Центральная часть зоопарка",
            animals=[
                Animal("Манул", "Otocolobus manul", 10, "самец"),
                Animal("Барсук", "Meles meles", 5, "самка"),
                Animal("Крокодил", "Crocodylus niloticus", 10, "самец"),
            ],
        ),
    ],
)


def get_neighbors(animal_name):
    for exhibit in moscow_zoo.exhibits:
        for animal in exhibit.animals:
            if animal.species == animal_name:
                # Сначала создаём список соседей, в который будем добавлять животных того же вида.
                neighbors = []
                for other_animal in exhibit.animals:
                    # Затем добавляем в список соседей всех животных того же вида, что и запрашиваемое животное.
                    if animal.species == other_animal.species:
                        neighbors.append(other_animal)
                return neighbors
    return None


def get_animals_in_exhibit(exhibit_name):
    animals = []
    for exhibit in moscow_zoo.exhibits:
        if exhibit.name == exhibit_name:
            animals = exhibit.animals
            break
    return animals

def get_exhibit_and_neighbors(animal_name):
    exhibit = None
    neighbors = []
    for exhibit in moscow_zoo.exhibits:
        for animal in exhibit.animals:
            if animal.species == animal_name:
                exhibit = exhibit
                neighbors = [animal for animal in exhibit.animals if animal.species != animal_name]
                break

    if exhibit:
        print("Животное {} находится в экспозиции {}:".format(animal_name, exhibit.name))
        for neighbor in neighbors:
            print(neighbor.species)
    else:
        print("Животное {} не найдено".format(animal_name))

animal_name = input("Введите название животного: ")
get_exhibit_and_neighbors(animal_name)