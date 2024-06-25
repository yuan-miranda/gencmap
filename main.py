import numpy as np
import time
from PIL import Image

# path where the player_coordinates.txt file is located.  Its either in `cmap/run` or where this mod's `.jar` file is located.
path = "player_coordinates.txt"

def generate_image(coordinates, resolution):
    image = np.ones((resolution, resolution, 3), dtype=np.uint8) * 255
    offset = resolution // 2
    image[coordinates[:, 0] + offset, coordinates[:, 1] + offset] = [0, 0, 0]

    image = Image.fromarray(image)
    image.save("map.png")

start_time = time.time()
coordinates = [(0, 0)]
with open(path) as file:
    for line in file:
        x, y = map(float, line.strip().split(", "))
        coordinates.append((round(x), round(y)))

minecraft_coordinates = np.array(coordinates)
resolution = 32768

generate_image(minecraft_coordinates, resolution)

end_time = time.time()
print("Time taken: {:.2f} seconds".format(end_time - start_time))