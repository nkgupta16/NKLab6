class Machine:
    def __init__(self, productivity, cost, average_part_price):
        self.productivity = productivity
        self.cost = cost
        self.average_part_price = average_part_price

    def parts_to_pay_back(self):
        return self.cost / self.average_part_price


class MillingMachine(Machine):
    def __init__(self, productivity, cost, average_part_price, milling_speed):
        super().__init__(productivity, cost, average_part_price)
        self.milling_speed = milling_speed

    def payback_time(self, fixed_part_price):
        return (self.cost / (self.productivity * fixed_part_price)) * 60  # in minutes


class CNCMachine(Machine):
    def __init__(self, productivity, cost, average_part_price, precision):
        super().__init__(productivity, cost, average_part_price)
        self.precision = precision

    def payback_time(self, fixed_part_price):
        return (self.cost / (self.productivity * fixed_part_price)) * 60  # in minutes


# Example usage:
milling_machine = MillingMachine(100, 50000, 500, 200)
cnc_machine = CNCMachine(150, 75000, 1000, 0.01)

parts_needed_for_milling = milling_machine.parts_to_pay_back()
payback_time_for_milling = milling_machine.payback_time(500)

parts_needed_for_cnc = cnc_machine.parts_to_pay_back()
payback_time_for_cnc = cnc_machine.payback_time(1000)

print(f"Milling Machine needs to produce {parts_needed_for_milling} parts to pay back.")
print(f"Milling Machine's payback time is {payback_time_for_milling} minutes with a fixed part price.")

print(f"CNC Machine needs to produce {parts_needed_for_cnc} parts to pay back.")
print(f"CNC Machine's payback time is {payback_time_for_cnc} minutes with a fixed part price.")
