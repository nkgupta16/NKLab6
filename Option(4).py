class Firearm:
    def __init__(self, rounds_in_magazine, rate_of_fire, firing_range):
        self.rounds_in_magazine = rounds_in_magazine  # Number of rounds
        self.rate_of_fire = rate_of_fire  # Rounds per minute
        self.firing_range = firing_range  # Meters

    def time_to_empty_magazine(self):
        # Calculating time (in seconds) to empty magazine.
        return self.rounds_in_magazine / (self.rate_of_fire / 60)

    def rate_of_fire_to_range_ratio(self):
        # Calculating the ratio of rate of fire to the firing range.
        return self.rate_of_fire / self.firing_range


class AssaultRifle(Firearm):
    pass


class SniperRifle(Firearm):
    pass


# Example usage:
ar = AssaultRifle(30, 800, 300)  # 30 rounds, 800 RPM, 300m range
sr = SniperRifle(5, 30, 1000)  # 5 rounds, 30 RPM, 1000m range

ar_time_to_empty = ar.time_to_empty_magazine()
ar_fire_range_ratio = ar.rate_of_fire_to_range_ratio()

sr_time_to_empty = sr.time_to_empty_magazine()
sr_fire_range_ratio = sr.rate_of_fire_to_range_ratio()

print(f"Assault Rifle will take {ar_time_to_empty:.2f} seconds to empty the magazine.")
print(f"Assault Rifle's rate of fire to range ratio is {ar_fire_range_ratio:.2f} RPM/m.")

print(f"Sniper Rifle will take {sr_time_to_empty:.2f} seconds to empty the magazine.")
print(f"Sniper Rifle's rate of fire to range ratio is {sr_fire_range_ratio:.2f} RPM/m.")
