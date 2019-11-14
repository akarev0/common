class Tenants:
    def __init__(self, name, passport_id, age, sex, address, room_number):
        self.name = name
        self.passport_id = passport_id
        self.age = age
        self.sex = sex
        self.room_number = room_number
        self.address = {
            "city": "Dnipro",
            "street": "Polya"
        }


tenants = [Tenants("Arkadiy", "MM12312", 17, "male", "", 105), Tenants("Kolya", "MM13333", 17, "male", "", 422),
           Tenants("Stasik", "MN12312", 17, "male", "", 420), Tenants("akarev0", "MM12129", 18, "male", "", 311)]