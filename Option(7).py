class Lamp:
    def __init__(self, radiation_power_w, energy_consumption, service_life_hours):
        self.radiation_power_w = radiation_power_w  # in Watts
        self.energy_consumption = energy_consumption  # in kWh
        self.service_life_hours = service_life_hours  # in hours

    def days_to_burn_out(self, hours_per_day=8):
        return self.service_life_hours / hours_per_day

    def radiation_power_to_energy_consumption_ratio(self):
        return self.radiation_power_w / self.energy_consumption


class FluorescentLamp(Lamp):
    pass


class Spotlight(Lamp):
    pass


# Example usage:
fluorescent_lamp = FluorescentLamp(30, 0.03, 8000)  # 30W, 0.03kWh, 8000 hours life
spotlight = Spotlight(150, 0.15, 2000)  # 150W, 0.15kWh, 2000 hours life

fluorescent_days_to_burn_out = fluorescent_lamp.days_to_burn_out()
spotlight_days_to_burn_out = spotlight.days_to_burn_out()

fluorescent_power_consumption_ratio = fluorescent_lamp.radiation_power_to_energy_consumption_ratio()
spotlight_power_consumption_ratio = spotlight.radiation_power_to_energy_consumption_ratio()

print(f"The fluorescent lamp will take {fluorescent_days_to_burn_out:.0f} days to burn out.")
print(
    f"The fluorescent lamp's radiation power to energy consumption ratio is {fluorescent_power_consumption_ratio:.2f} W/kWh.")

print(f"The spotlight will take {spotlight_days_to_burn_out:.0f} days to burn out.")
print(f"The spotlight's radiation power to energy consumption ratio is {spotlight_power_consumption_ratio:.2f} W/kWh.")
