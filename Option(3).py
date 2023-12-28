class Car:
    def __init__(self, tank_capacity, fuel_consumption, average_speed):
        self.tank_capacity = tank_capacity  # in liters
        self.fuel_consumption = fuel_consumption
        self.average_speed = average_speed  # km per hour

    def distance_until_empty(self):
        return (self.tank_capacity / self.fuel_consumption) * 100

    def efficiency_ratio_for_distance(self, weight_or_passengers, distance_km=250):
        fuel_needed = (self.fuel_consumption / 100) * distance_km
        return weight_or_passengers / fuel_needed


class Truck(Car):
    def __init__(self, tank_capacity, fuel_consumption, average_speed, cargo_weight):
        super().__init__(tank_capacity, fuel_consumption, average_speed)
        self.cargo_weight = cargo_weight  # in kilograms

    def cargo_to_fuel_ratio_for_distance(self, distance_km=250):
        return self.efficiency_ratio_for_distance(self.cargo_weight, distance_km)


class Bus(Car):
    def __init__(self, tank_capacity, fuel_consumption, average_speed, passenger_count):
        super().__init__(tank_capacity, fuel_consumption, average_speed)
        self.passenger_count = passenger_count  # number of passengers

    def passengers_to_fuel_ratio_for_distance(self, distance_km=250):
        return self.efficiency_ratio_for_distance(self.passenger_count, distance_km)


# Example usage:
truck = Truck(200, 30, 80, 15000)
bus = Bus(150, 20, 60, 50)

truck_distance = truck.distance_until_empty()
truck_ratio = truck.cargo_to_fuel_ratio_for_distance()

bus_distance = bus.distance_until_empty()
bus_ratio = bus.passengers_to_fuel_ratio_for_distance()

print(f"Truck can travel {truck_distance} km until the tank is empty.")
print(f"Truck's cargo to fuel ratio for 250 km: {truck_ratio:.2f} kg/L")

print(f"Bus can travel {bus_distance} km until the tank is empty.")
print(f"Bus's passengers to fuel ratio for 250 km: {bus_ratio:.2f} passengers/L")
