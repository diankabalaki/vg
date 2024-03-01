import random

class MusicAlbum:
    def __init__(self, title, artist, release_year, genre, tracklist):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist
    
    def play_random_track(self):
        random_track_index = random.randint(0, len(self.tracklist) - 1)
        random_track_name = self.tracklist[random_track_index]
        print("Название:", self.title)
        print("Исполнитель:", self.artist)
        print("Год:", self.release_year)
        print("Жанр:", self.genre)
        print("Треки:", self.tracklist)
        print("Воспроизводится трек {}: {}".format(random_track_index + 1, random_track_name))

class Student:
    def __init__(self, name, age, grade, scores):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores
    
    def average_score(self):
        if self.scores:
            return sum(self.scores) / len(self.scores)
        else:
            return 0

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    
    def print_ingredients(self):
        print("Продукты для блюда", self.name + ":")
        for ingredient in self.ingredients:
            print("-", ingredient)
    
    def cook(self):
        print("Готовим блюдо", self.name + "!")
        print("Блюдо", self.name, "готово!")

# Пример использования классов:
tracklist = ['Deutschland', 'Radio', 'Zeig dich', 'Ausländer', 'Sex', 'Puppe', 'Was ich liebe', 'Diamant', 'Weit weg', 'Tattoo', 'Hallomann']
album = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte", tracklist)
album.play_random_track()

student = Student("John", 18, 12, [80, 85, 90])  # Создание объекта класса Student
print("Имя:", student.name)  # Вывод имени студента
print("Возраст:", student.age)  # Вывод возраста студента
print("Класс:", student.grade)  # Вывод класса студента
print("Оценки:", student.scores)  # Вывод списка оценок студента
print("Средний балл:", student.average_score())  # Вызов метода average_score и вывод среднего балла

recipe = Recipe("Пельмени", ["Мука", "Мясо", "Лук", "Соль", "Перец"])
recipe.print_ingredients()
recipe.cook()