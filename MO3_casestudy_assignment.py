# Super class for general vehicle types
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Subclass that inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # Initialize the super class attribute
        super().__init__(vehicle_type)
        # Initialize Automobile-specific attributes
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def main():
    # Application setup
    print("Welcome to the Vehicle Information App")
    print("-" * 30)

    # Accept user input for the vehicle details
    # Per requirements, vehicle_type is hardcoded to "car"
    vehicle_type = "car"
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    # Create an instance of Automobile
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    # Output the data in an easy-to-read format
    print("\nVehicle Information Details:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")

if __name__ == "__main__":
    main()