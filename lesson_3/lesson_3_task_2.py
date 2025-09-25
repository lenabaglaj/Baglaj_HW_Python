from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13 Pro Max", "+79876543210"),
    Smartphone("Samsung", "Galaxy S22 Ultra", "+79123456789"),
    Smartphone("Xiaomi", "Redmi Note 10S", "+79012345678"),
    Smartphone("Huawei", "P40 Pro", "+79876543211"),
    Smartphone("Google", "Pixel 6a", "+79987654321")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. Номер телефона: {phone.phone_number}")