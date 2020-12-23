from task_1_10_3 import Client


guests = []


class Guests(Client):

    def add_to_guests_list(self):
        guests.append(self.get_name())

    def get_guest_status(self):
        if self in guests:
            return f"<<{self.first_name} {self.last_name}>>, г. {self.city}, статус {self.status}"
        else:
            return f"<<{self.first_name} {self.last_name}>> не в списке приглашенных"


client_1 = Guests("Иван", "Петров", 50, "Москва", '"Наставник"')
client_1.add_to_guests_list()
client_2 = Guests("Петр", "Серебренников", city="Рязань")
client_3 = Guests("Гвидо", "Ван Россум", 1000000, "Калифорния", '"Cоздатель языка программирования Python"')
client_3.add_to_guests_list()
print(client_1.get_info(), client_2.get_info(), client_3.get_info(), sep="\n")
print("V●ᴥ●V V●ᴥ●V V●ᴥ●V V●ᴥ●V V●ᴥ●V V●ᴥ●V V●ᴥ●V V●ᴥ●V V●ᴥ●V V●ᴥ●V V●ᴥ●V V●ᴥ●V V●ᴥ●V V●ᴥ●V V●ᴥ●V V●ᴥ●V V●ᴥ●V V●ᴥ●V ")
print(client_1.get_guest_status(), client_2.get_guest_status(), client_3.get_guest_status(), sep="\n")
