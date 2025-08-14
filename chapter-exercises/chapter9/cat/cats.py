from cat import Cat

my_cat = Cat('Goose', 1)
your_cat = Cat('Grizz', 3)

print(f"My cat's name is {my_cat.name}.")
print(f'My cat is {my_cat.age} years old.')
my_cat.nap()

print(f"\nYour cat's name is {your_cat.name}.")
print(f'Your cat is {your_cat.age} years old.')
your_cat.nap()