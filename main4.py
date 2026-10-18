print("Welcome to the bus Fare Calculator!")

try:
    # Ask the user for distance
    distance = float(input("Enter the distance to your destination (in kilometers): "))

    #Check for negative distance
    if distance < 0:
        raise ValueError("Distance cannot be negative.")

    # Ask the user for fare per kilometer
    fare_per_km = float(input("Enter the fare per kilometer in USD: "))

    # Check for invalid fare
    if fare_per_km <= 0:
        raise ZeroDivisionError("Fare per kilometer must be greater than zero.")

    # Calculate taotal fare
    total_fare = distance * fare_per_km
    print("Your total fare is: ", total_fare, " USD.")

except ValueError as ve:
    # Handles invalid number input or negative values
    print("Error: ", ve)

except ZeroDivisionError as zde:
    # Handles fare per km being zero or negative
    print("Error: ", zde)

except KeyboardInterrupt:
    # Handles when the user presses Ctrl+C to stop the program
    print("\nProgram interrupted by user. Goodbye!")

except Exception as e:
    # Catches any other unexpected errors
    print("An unexpected error occurred:", e)

finally:
    # Always runs
    print("Thank you for using the Matatu Fare Calculator!")