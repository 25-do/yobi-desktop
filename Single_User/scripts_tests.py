# print("\U0001F600")
# print("\U0001F601")
# print("\U0001F605")
# print("\U0001F923")
# print("\U0001F602")
# print("\U0001F642")
# print("\U0001F607")
# print("\U0001F60D")
# print("\U0001F612")
# print("\U0001F612")
# print("\U0001F595")

# from random import choices
# ch = choices(["Fully paid", "Installments", "Not Paid"])
# ch = (''.join(map(str, ch)))
# print(ch)

class MyClass:
    def __init__(self, name : str, bark) -> None:
        self.name = name
        self.bark = bark
    def dog_name(self):
        return print(f"dogs name is {self.name}")
    def __repr__(self):
         print(f"dogs name is {self.name}")

c = MyClass("Max", "WOOOO")
print(c.dog_name)