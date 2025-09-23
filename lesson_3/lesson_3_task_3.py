from address import Address
from mailing import Mailing

to_address = Address("", "Moscow", "One", 5, 1)
from_address = Address("444444", "Sochi", "Two", 2, 5)

mailing = Mailing ("London", "Chita", "25000", 100)
print(mailing)