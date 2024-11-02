class Bicycle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_age(self):
        c_age = 2024
        return c_age - self.year


bicycle = Bicycle("Bugatti", "Divus", 2023)
print(f"Бренд: {bicycle.brand}, Модель: {bicycle.model}, Год выпуска: {bicycle.year}")
print(f"Возраст велосипеда: {bicycle.get_age()} лет")