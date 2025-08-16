from electric_car import ElectricCar

my_y = ElectricCar('tesla', 'model y', 2024)
print(my_y.descriptive_name())
my_y.battery.describe_battery()
my_y.battery.get_range()
my_y.battery.upgrade_battery()
my_y.battery.describe_battery()
my_y.battery.get_range()