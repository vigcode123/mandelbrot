#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(c, max_iterations):
    z, n = 0, 0

    while abs(z) <= 2 and n < max_iterations:
        print(f"\n\n\nIteration {n}: z = {z}, c = {c}, |z| = {abs(z)}", file=open("logs.txt","a"))
        print(f"{z} = {z}^2+{c}", file=open("logs.txt","a"))
        z = z**2 + c
        print(f"= {z}", file=open("logs.txt","a"))
        n += 1

    if n == max_iterations:
        print("Reached maximum iterations.", file=open("logs.txt","a"))
    else:
        print(f"Converged in {n} iterations.", file=open("logs.txt","a"))
    
    return n


print("START", file=open("logs.txt","w+"))

#TODO: change this for tuning
x_start, x_end, y_start, y_end = -2.0, 1.0, -1.5, 1.5
image_width, image_height = 49, 49
#TODO: change this for more detail
iters = 1000

x_coords = np.linspace(x_start, x_end, image_width)
y_coords = np.linspace(y_start, y_end, image_height)
mandelbrotImg = np.zeros((image_width, image_height), dtype=int)


for i in range(image_width):
    for j in range(image_height):
        x = x_coords[i]
        y = y_coords[j]
        c = complex(x, y)
        mandelbrotImg[i, j] = mandelbrot(c, iters)

plt.imshow(mandelbrotImg.T, extent=(x_start, x_end, y_start, y_end))
plt.show()
