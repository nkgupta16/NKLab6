class Employee:
    def __init__(self, working_hours, rate, bonus_coefficient):
        self.working_hours = working_hours
        self.rate = rate
        self.bonus_coefficient = bonus_coefficient

    def calculate_premium(self):
        return self.working_hours * self.rate * self.bonus_coefficient

    def salary_to_hours_ratio(self):
        total_salary = (self.working_hours * self.rate) + self.calculate_premium()
        return total_salary / self.working_hours


class SeniorEmployee(Employee):
    pass


class Director(Employee):
    pass


# Example usage:
senior_employee = SeniorEmployee(160, 30, 0.2)  # 160 hours, $30 per hour, 0.2 bonus coefficient
director = Director(160, 50, 0.3)  # 160 hours, $50 per hour, 0.3 bonus coefficient

senior_premium = senior_employee.calculate_premium()
senior_ratio = senior_employee.salary_to_hours_ratio()

director_premium = director.calculate_premium()
director_ratio = director.salary_to_hours_ratio()

print(f"The senior employee's premium is ${senior_premium:.2f}.")
print(f"The senior employee's salary to hours ratio is ${senior_ratio:.2f} per hour.")

print(f"The director's premium is ${director_premium:.2f}.")
print(f"The director's salary to hours ratio is ${director_ratio:.2f} per hour.")

