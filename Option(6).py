class Figure:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        return self.a * self.b * self.c


class BodyWithCavity(Figure):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def volume_minus_void(self):
        # Calculating the volume of the body minus the internal cavity.
        if self.d >= min(self.a, self.b, self.c):
            return 0  # The cavity cannot be larger than any dimension of the body!!!
        void_volume = (self.a - self.d) * (self.b - self.d) * (self.c - self.d)
        return self.volume() - void_volume


def total_volume_of_figures(figures):
    return sum(figure.volume() for figure in figures)


# Example usage:
figure = Figure(10, 20, 30)
body_with_cavity = BodyWithCavity(10, 20, 30, 2)

print(f"The volume of the figure is {figure.volume()} cubic units.")
print(f"The volume of the body minus the void is {body_with_cavity.volume_minus_void()} cubic units.")

# Assuming we have an array of 5 identical figures.
identical_figures = [Figure(10, 20, 30) for _ in range(5)]
total_volume = total_volume_of_figures(identical_figures)

print(f"The total volume of the identical figures is {total_volume} cubic units.")
