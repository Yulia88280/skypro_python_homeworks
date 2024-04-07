from Address import Address

from Mailing import Mailing

# Создала экземпляры класса Address для адресов отправителя и получателя
to_address = Address("443031", "Самара", "Ташкентская", "238", "5")
from_address = Address("446600", "Нефтегорск", "Ленина", "10", "10")

# Создала экземпляр класса Mailing для почтового отправления
mail = Mailing(to_address, from_address, 250, "DSe456Y")

# Печать информации о почтовом отправлении
print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
      f"в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. "
      f"Стоимость {mail.cost} рублей.")