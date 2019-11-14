class Staff:
    def __init__(self, name, passport_id, position, salary):
        self.name = name
        self.passport_id = passport_id
        self.position = position
        self.salary = salary


staff = [Staff("James", "MR229561", "Director", 15000), Staff("Lars", "MR223561", "Manager", 13000),
         Staff("Kirk", "MR228745", "Cock", 11000), Staff("Robert", "MR123561", "Chambermaid", 9000)]
