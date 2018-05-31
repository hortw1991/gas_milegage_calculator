"""
Calculates the difference in cost for a full tank of gas for different MPGs.

Uses live data from the Marathon website.  Currently defaults to premium.
"""

import get_gas_cost

def main():
    """ Currently defaults only to Honda Civic Hatchback (Sport Touring) data. """
    gas_price = get_gas_cost.get_gas_cost()
    tank_size = 12.39 #gallons
    
    while True:
        mpg1 = float(input("Enter MPG1: "))
        mpg2 = float(input("Enter MPG2: "))

        # Calculate MPG costs for the full tank
        mpg1_rate = get_tank_cost(mpg1, gas_price, tank_size)
        mpg2_rate = get_tank_cost(mpg2, gas_price, tank_size)

        print(f"Effectiveness Per Tank at {mpg1}: {mpg1_rate}")
        print(f"Effectiveness Per Tank at {mpg2}: {mpg2_rate}\n")
        
        # Final calculation
        print(f"Cost Difference: ${round(mpg1_rate - mpg2_rate)}")


def get_tank_cost(mpg, gas_price, tank_size):
    """ Calculates the actual MPG cost. """
    miles_per_tank = mpg * tank_size
    miles_per_tank / gas_price

    return mpg * tank_size / gas_price


if __name__ == "__main__":
    main()