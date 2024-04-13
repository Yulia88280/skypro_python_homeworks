from smartphone import Smartphone

# Создадим список для каталога смартфонов
catalog = []

# Наполним список экземплярами класса Smartphone
catalog.append(Smartphone("Samsung", "Galaxy S", "+78887284181"))
catalog.append(Smartphone("Apple", "iPhone 15", "+78889285790"))
catalog.append(Smartphone("Xiaomi", "Redmi Note", "+78883560202"))
catalog.append(Smartphone("Soni", "1234", "+78886898386"))
catalog.append(Smartphone("Nokia", "3310", "+78884807774"))

# Печатаем каталог
for smartphone in catalog:
    print (f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")