import math
import matplotlib.pyplot as plt
import numpy as np


class oktagon: 
    def __init__(self,side):  
        self.side=side  
        self.angle=135 
        self.k=1+math.sqrt(2)


    def described_circle(self):
        radius_described = self.side * math.sqrt(( 4 + 2 * math.sqrt(2) ) / 4)
        square_described = math.pi * radius_described**2
        return radius_described, square_described


    def incribed_circle(self):
        radius_incribed = (( 1 + math.sqrt(2) ) / 2) * self.side
        square_incribed = radius_incribed**2 * math.pi
        return radius_incribed, square_incribed


    def Oktagon_data(self):
        perimeter = self.side * 8
        square_oktagon = 2 * (1 + math.sqrt(2)) * self.side**2
        return perimeter, square_oktagon


    def draw(self):
        radius_desc, _ = self.described_circle()
        radius_inc, _ = self.incribed_circle()
        figure, ax = plt.subplots(figsize=(10, 10))
        circle_desc = plt.Circle((0, 0), radius_desc, color="red", fill=False, label="Описанная окр.")
        ax.add_patch(circle_desc)
        circle_inc = plt.Circle((0, 0), radius_inc, color="blue", fill=False, label="Вписанная окр.")
        ax.add_patch(circle_inc)
        angles = np.linspace(0, 2 * np.pi, 8, endpoint=False) + np.pi / 8
        x = radius_desc * np.cos(angles)
        y = radius_desc * np.sin(angles)
        x = np.append(x, x[0])
        y = np.append(y, y[0])
        ax.plot(x, y, color="black", linewidth=2, label="Октагон")
        ax.set_aspect("equal")

        plt.show()