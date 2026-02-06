# Shipping cost program
# Written by Wesley Greer on 2/6/2026

def weight_conversion(weight):
    # Calculate the shipping charge.
    shippingCost = 0.0
    ######################
if weight <= 2:
    print('Shipping will cost $1.50')
elif weight > 2 and weight <= 6:
    print('Shipping will cost $3.00')
elif weight > 6 and weight <= 10:
    print('Shipping will cost $4.00')
else:
    print('Shipping will cost $4.75')
    ######################
    
    return shippingCost

#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))
