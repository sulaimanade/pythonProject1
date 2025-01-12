#Exponent function allows us to take a certain number and raise it to a specific power.

print(2**3) #this is similar to 2*2*2

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(20, 3))