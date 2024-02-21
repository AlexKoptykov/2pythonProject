def print_car_details(make: str = 'unknown', model: str = 'unknown', year: int = -1) -> None:
    print(f'Марка автомобиля: {make}')
    print(f'Модель автомобиля: {model}')
    print(f'Год выпуска: {year}')


print_car_details("Mazda", "6", 2020)
print()
print_car_details("LADA", "Granta")
print()
print_car_details(year=2023)
