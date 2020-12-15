# Finding the Cheapest Shipping Method by comparing three shipping method
# premium ground shipping, ground shipping and drone shipping
premium_shipping = 125
def ground_shipping(weight):
    flat_charge = 20
    if weight <= 2:
        charge = flat_charge + weight * 1.50
    elif weight <= 6:
        charge = flat_charge + weight * 3.00
    elif weight <= 10:
        charge = flat_charge + weight * 4.00
    else:
        charge = flat_charge + weight * 4.75
    return charge
print(ground_shipping(41.5))

def drone_shipping(weight):
    flat_charge = 0.00
    if weight <= 2:
        charge = flat_charge + weight * 4.50
    elif weight <= 6:
        charge = flat_charge + weight * 9.00
    elif weight <= 10:
        charge = flat_charge + weight * 12.00
    else:
        charge = flat_charge + weight * 14.25
    return charge
print(drone_shipping(41.5))    

def cheapest_shipping(weight):
    ground = ground_shipping(weight)
    drone = drone_shipping(weight)
    premium = premium_shipping
    if ground < drone and ground < premium:
        return ground, "ground"
    elif drone < ground and drone < premium:
        return drone, "drone"
    else:
        return premium, "premium"

weight = 4.8
cost, method = cheapest_shipping(weight)
print(f"The {method} shipping method that is the cheapest and total cost will be ${cost} of {weight} lb package")

weight = 41.5
cost, method = cheapest_shipping(weight)
print(f"The {method} shipping method that is the cheapest and total cost will be ${cost} of {weight} lb package")
