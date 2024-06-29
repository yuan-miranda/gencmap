import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np

overworld_path = r"C:\Users\yuane\AppData\Roaming\.minecraft\minecraft_overworld_player_coordinates.txt"
# nether_path = r"C:\Users\yuane\AppData\Roaming\.minecraft\minecraft_the_nether_player_coordinates.txt"
# end_path = r"C:\Users\yuane\AppData\Roaming\.minecraft\minecraft_the_end_player_coordinates.txt"

resolution = 100000

def get_coordinates(file_path):
    coordinates = [(0, 0)]
    with open(file_path, "r") as file:
        if file.readline() == "": return np.array(coordinates)
        for line in file:
            x, z = map(float, line.strip().split(", "))
            coordinates.append((x, z))
    return np.array(coordinates)

def init():
    scatter.set_offsets(np.empty((0, 2)))
    return scatter,

def update(frame):
    coordinates = get_coordinates(overworld_path)
    scatter.set_offsets(coordinates)
    return scatter,

def loop():
    while True:
        yield

start_time = time.time()

fig, ax = plt.subplots()
ax.set_xlim(-resolution // 2, resolution // 2)
ax.set_ylim(-resolution // 2, resolution // 2)
ax.set_aspect("equal")
scatter = ax.scatter([], [], c="black", s=1)

ani = animation.FuncAnimation(fig, update, frames=loop(), init_func=init, blit=False)
plt.show()

end_time = time.time()
print("Time taken: {:.2f} seconds".format(end_time - start_time))