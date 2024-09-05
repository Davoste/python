class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Get user input
name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")

# Create an instance of the Person class using user input
person_instance = Person(name, age, gender)

# Call the introduce method
person_instance.introduce()
