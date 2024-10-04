from decimal import Decimal, getcontext
import math


def generate_pi(decimal_places):
    # Set a limit for the maximum decimal places (e.g., 100)
    MAX_DECIMALS = 15

    # If the requested decimal places exceed the limit, raise an exception
    if decimal_places > MAX_DECIMALS:
        raise ValueError(f"Decimal places cannot exceed {MAX_DECIMALS}.")

    # Set the precision (we add 2 to ensure rounding is correct)
    getcontext().prec = decimal_places + 2

    # Calculate Pi using the arctangent series
    pi_value = Decimal(4) * (
        Decimal(4) * Decimal(math.atan(1 / 5)) - Decimal(math.atan(1 / 239))
    )

    # Format Pi to the correct number of decimal places and return
    return round(pi_value, decimal_places)


try:
    decimal_places = int(input("Enter the number of decimal places for Pi: "))
    pi_value = generate_pi(decimal_places)
    print(f"Pi to {decimal_places} decimal places: {pi_value}")
except ValueError as ve:
    print(ve)
