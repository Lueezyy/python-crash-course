import car
import electric_car as ec

my_lambo = car.Car('lamborghini', 'temerario', 2026)
print(my_lambo.descriptive_name())

my_rivac = ec.ElectricCar('rivac', 'nevera r', 2025)
my_rivac.battery.battery_size = 108
print(my_rivac.descriptive_name())