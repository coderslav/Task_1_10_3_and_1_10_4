class Client:
    def __init__(self, first_name, last_name, balance=0.0, city="Не указан", status="Не указан"):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.balance = balance
        self.status = status

    def get_info(self):
        return f"Клиент <<{self.first_name} {self.last_name}>>. Баланс: {self.balance} руб."

    def get_name(self):
        return self.last_name


if __name__ == '__main__':
    client_1 = Client("Иван", "Петров", 50)
    print(client_1.get_info())
