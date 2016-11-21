
from __future__ import division
pixel = [
    [7, 7, 5],
    [3, 1, 3],
    [5, 8, 7]
]
new = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
def closest_palette_color(v):
    return v if v%2 == 0 else v-1


for x in range(0, 2):
    for y in range(0, 2):
        oldpixel = pixel[x][y]
        newpixel = closest_palette_color(oldpixel)
        pixel[x][y] = newpixel
        quant_error = oldpixel - newpixel
        print((oldpixel,newpixel, quant_error))
        new[x + 1][y    ] = pixel[x + 1][y    ] + quant_error * 3 / 8
        new[x    ][y + 1] = pixel[x    ][y + 1] + quant_error * 3 / 8
        new[x + 1][y + 1] = pixel[x + 1][y + 1] + quant_error * 2 / 8

print(pixel)
