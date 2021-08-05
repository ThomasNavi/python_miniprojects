distance = input('Input total distance of the drive in kilometers: ')
fuelUsage = input('Input liters-per-kilometer usage for the car: ')
fuelPrice = input('Input price per liters of fuel: ')
print('the trip will cost:',int(fuelUsage)*int(fuelPrice)*int(distance),'USD')