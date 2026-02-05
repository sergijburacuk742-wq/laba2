class Humanity:
    def __init__(self, population, average_age, countries_count, languages_count):
        self.population = population
        self.average_age = average_age
        self.countries_count = countries_count
        self.languages_count = languages_count

    def show_info(self):
        print(f"Населення людства: {self.population} осіб")
        print(f"Середній вік: {self.average_age} років")
        print(f"Кількість країн: {self.countries_count}")
        print(f"Кількість мов: {self.languages_count}")

    def increase_population(self, amount):
        self.population += amount
        print(f"Населення збільшилось на {amount} осіб.")

    def decrease_population(self, amount):
        self.population -= amount
        print(f"Населення зменшилось на {amount} осіб.")

    def is_aging(self):
        return self.average_age > 35

    def develop(self, new_countries, new_languages):
        self.countries_count += new_countries
        self.languages_count += new_languages
        print("Людство розвивається 🌍")

if __name__ == "__main__":
    humanity = Humanity(8_000_000_000, 30, 195, 7000)

    humanity.show_info()
    humanity.increase_population(1_000_000)
    humanity.decrease_population(500_000)

    print("Чи старіє людство?", humanity.is_aging())

    humanity.develop(1, 5)
    humanity.show_info()
