# Simple Interest Calculator

def calculate_simple_interest(principal, rate, time):
    """
    Calculate the simple interest using the formula:
    Simple Interest = (P * R * T) / 100
    where:
    P = Principal amount
    R = Annual rate of interest
    T = Time period in years
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Input values
try:
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual rate of interest (in %): "))
    time = float(input("Enter the time period (in years): "))

    # Calculate simple interest
    interest = calculate_simple_interest(principal, rate, time)

    # Output the result
    print(f"\nSimple Interest = {interest}")
except ValueError:
    print("Please enter valid numeric values for principal, rate, and time.")
