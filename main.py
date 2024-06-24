import matplotlib.pyplot as plt
import numpy as np
import time

# path where the player_coordinates.txt file is located.  Its either in `cmap/run` or where this mod's `.jar` file is located.
# path = r"C:\Users\yuane\Documents\cmap\run\player_coordinates.txt"
path = ""

start_time = time.time()
coordinates = [(0, 0)]
with open(path) as file:
    for line in file:
        x, y = map(float, line.strip().split(", "))
        coordinates.append((round(x), round(y)))

minecraft_coordinates = np.array(coordinates)

image_size = 2048
image = np.ones((image_size, image_size, 3), dtype=np.uint8) * 255

offset = image_size // 2

# fast af
image[minecraft_coordinates[:, 0] + offset, minecraft_coordinates[:, 1] + offset] = [0, 0, 0]

# slow mf
# for x, y in minecraft_coordinates:
#     image[x + offset, y + offset] = [0, 0, 0]

plt.imshow(image)
plt.axis('off')
plt.savefig('map.png', bbox_inches='tight', pad_inches=0)

end_time = time.time()
print("Time taken: {:.2f} seconds".format(end_time - start_time))
