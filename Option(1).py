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


# Example usage:
building = Building(100, 1000, 10)
village_house = VillageHouse(150, 800, 5, 200)
city_house = MultiApartmentCityHouse(200, 1500, 20, 10)

print(f"Building total cost: {building.calculate_total_cost()}")
print(f"Building cost to residents ratio: {building.ratio_of_cost_to_residents()}")

print(f"Village House total cost: {village_house.calculate_total_cost()}")
print(f"Village House cost to residents ratio: {village_house.ratio_of_cost_to_residents()}")

print(f"City House total cost: {city_house.calculate_total_cost()}")
print(f"City House cost to residents ratio: {city_house.ratio_of_cost_to_residents()}")
