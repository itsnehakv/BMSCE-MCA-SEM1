capacity = float(input("Enter tank capacity in litres: "))
r = float(input("Enter rate of leakage in ml/sec: "))
d = int(input("Enter number of days of leakage: "))

'''
Since rate of water leakage is in ml/sec

1 litre = 1000 ml
1 day = 24 x 60 x 60 = 86400
'''

leaked_water = r * d * 86400
remaining_water = (capacity * 1000) - leaked_water

if remaining_water < 0:
    remaining_water = 0

print(f"Water left in the tank: {remaining_water / 1000} litres")