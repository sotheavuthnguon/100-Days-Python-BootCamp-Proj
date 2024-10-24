def greet():
    print("HELLo")
    print("HELLo")
    print("HELLo")

def greet_with_name(name):
    print(f"Hello {name}")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is the weather in {location}?")

greet()
greet_with_name("Edward")
greet_with_name("Angela")
greet_with("Edward", "Phnom Penh")

greet_with(location='London', name='Angela')