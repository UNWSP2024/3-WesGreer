# Write a program that asks the user to enter a person's age.  The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult.  Following are the guidelines:

# Age Classification Program
# written by Wesley Greer on 2/6/2026

def categorize_age(age):
    ageCategory = "TBD"
# figure out what category the age falls in
if age >= 20:
    print('They are an adult.')
else:
    if age >= 13:
        print('They are a teenager.')
    else:
        if age > 1:
            print('They are a child.')
        else:
            print('They are an infant.')
  


    return ageCategory


#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    # Get age from the user.
    age = float(input("Enter the person's age: "))
    # Display the age
    ageBucket = categorize_age(age)
    print (ageBucket)
