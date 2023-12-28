import math

class OpticalDisk:
    def __init__(self, capacity, speed, laser_thickness_nm):
        self.capacity = capacity            # Capacity in bytes
        self.speed = speed                  # Speed in RPM
        self.laser_thickness_nm = laser_thickness_nm  # Laser thickness in nanometers

    def bytes_in_20_seconds(self, circumference_mm):
        # To Calculate how many bytes the laser travels in 20 seconds.
        # Converting speed from RPM to revolutions per second (div by 60)
        revs_per_second = self.speed / 60
        bytes_per_rev = self.capacity / (math.pi * 2 * circumference_mm)
        return bytes_per_rev * revs_per_second * 20

    def average_time_per_revolution(self):
        return 60 / self.speed

class CD(OpticalDisk):
    pass

class DVD(OpticalDisk):
    pass

# Example usage:
cd = CD(700 * 1024 * 1024, 200, 120)  # 700MB CD, 200 RPM, 120nm laser
dvd = DVD(4.7 * 1024 * 1024 * 1024, 570, 120)  # 4.7GB DVD, 570 RPM, 120nm laser

cd_bytes_in_20_sec = cd.bytes_in_20_seconds(120)
dvd_bytes_in_20_sec = dvd.bytes_in_20_seconds(120)

cd_avg_time_per_rev = cd.average_time_per_revolution()
dvd_avg_time_per_rev = dvd.average_time_per_revolution()

print(f"A CD's laser travels {cd_bytes_in_20_sec:.2f} bytes in 20 seconds.")
print(f"Average time per revolution for a CD: {cd_avg_time_per_rev:.2f} seconds.")

print(f"A DVD's laser travels {dvd_bytes_in_20_sec:.2f} bytes in 20 seconds.")
print(f"Average time per revolution for a DVD: {dvd_avg_time_per_rev:.2f} seconds.")
