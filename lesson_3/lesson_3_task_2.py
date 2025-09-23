from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "S24", "89101726384"),
    Smartphone("IPhone", "17Pro", "89101726385"),
    Smartphone("Motorola", "Z3", "89101726386"),
    Smartphone("Sony", "248", "89101726387"),
    Smartphone("Xiaomi", "Pin", "89101726388"),
]

for smartphone in catalog:
    print(f"{smartphone.brand_phone} {smartphone.model_phone} {smartphone.number_phone}")