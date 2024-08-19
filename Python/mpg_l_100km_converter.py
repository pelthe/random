mile_in_meters = 1609.344
gallon_in_liters = 3.785411784
def liters_100km_to_miles_gallon(liters):
    gallons = liters / gallon_in_liters
    miles = 100000 / mile_in_meters
    miles_gallon = miles / gallons
    return miles_gallon
    
def miles_gallon_to_liters_100km(miles):
    liters = gallon_in_liters
    kilometers = miles * 1.609344
    km_100 = kilometers / 100
    kilometers_liters = liters / km_100
    return kilometers_liters
    

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
