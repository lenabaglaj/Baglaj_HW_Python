from mailing import Mailing
from address import Address

from_addr = Address(index="123456", city="Москва", street="Ленинградская улица", house="12", apartment="34")
to_addr = Address(index="654321", city="Санкт-Петербург", street="Невский проспект", house="56", apartment="78")


mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=500,
    track="TRACK-NUMBER-123"
)

print(f"""
Отправление {mailing.track}
из {mailing.from_address.index}, {mailing.from_address.city},
{mailing.from_address.street}, {mailing.from_address.house}-{mailing.from_address.apartment}
в {mailing.to_address.index}, {mailing.to_address.city},
{mailing.to_address.street}, {mailing.to_address.house}-{mailing.to_address.apartment}.
Стоимость {mailing.cost} рублей.
""")