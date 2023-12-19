class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"The dog's name is {self.name} and it is {self.age} years old.")

    def get_info(self):
        print(f"The dog's coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, playfulness_level):
        super().__init__(name, age, coat_color)
        self.playfulness_level = playfulness_level

    def playfulness(self):
        print(f"{self.name} the Jack Russell Terrier has a playfulness level of {self.playfulness_level}.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def show_strength(self):
        print(f"{self.name} the Bulldog has a strength level of {self.strength}.")


# Creating objects and using the functionalities
dog1 = JackRussellTerrier("Buddy", 3, "white and brown", "high")
dog1.description()
dog1.get_info()
dog1.playfulness()

dog2 = Bulldog("Spike", 5, "brown", "very strong")
dog2.description()
dog2.get_info()
dog2.show_strength()

