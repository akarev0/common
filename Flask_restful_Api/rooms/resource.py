class Rooms:
    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price


rooms = [Rooms("105", "first", "available", "150"), Rooms("232", "second", "closed", "250"),
         Rooms("311", "third", "closed", "300"), Rooms("422", "fourth", "available", "600")]
