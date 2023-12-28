# Overloading the addition operator add for Option 1
class Building:
    def __init__(self, area, cost_per_sq_meter, residents):
        self.area = area
        self.cost_per_sq_meter = cost_per_sq_meter
        self.residents = residents

    def calculate_total_cost(self):
        return self.area * self.cost_per_sq_meter

    def ratio_of_cost_to_residents(self):
        total_cost = self.calculate_total_cost()
        return total_cost / self.residents if self.residents != 0 else float('inf')

    def __add__(self, other):
        if isinstance(other, Building):
            combined_area = self.area + other.area
            combined_cost_per_sq_meter = (self.cost_per_sq_meter + other.cost_per_sq_meter) / 2
            combined_residents = self.residents + other.residents
            return Building(combined_area, combined_cost_per_sq_meter, combined_residents)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Building' and '{}'".format(type(other).__name__))


class VillageHouse(Building):
    def __init__(self, area, cost_per_sq_meter, residents, garden_area):
        super().__init__(area, cost_per_sq_meter, residents)
        self.garden_area = garden_area

    def ratio_of_cost_to_residents(self):
        total_value = self.calculate_total_cost() + self.garden_area
        return total_value / self.residents if self.residents != 0 else float('inf')


class MultiApartmentCityHouse(Building):
    def __init__(self, area, cost_per_sq_meter, residents, num_apartments):
        super().__init__(area, cost_per_sq_meter, residents)
        self.num_apartments = num_apartments

    def ratio_of_cost_to_residents(self):
        total_cost = self.calculate_total_cost()
        return total_cost / (self.residents * self.num_apartments) if self.residents != 0 else float('inf')


village_house = VillageHouse(150, 800, 5, 200)
city_house = MultiApartmentCityHouse(200, 1500, 20, 10)

# Example of adding a village house and a city house
combined_building = village_house + city_house
print(f"Combined Building total cost: {combined_building.calculate_total_cost()}")
print(f"Combined Building cost to residents ratio: {combined_building.ratio_of_cost_to_residents()}")
