import tkinter as tk
import math as m
import os

absolute_path = os.path.dirname(__file__)
path = os.path.join(absolute_path, "readme.txt")

try:
    with open(path, 'r') as f:
        filelines = f.readlines()
except:     
    fname = input("Please enter filepath for config file: ")
    with open(fname, 'r') as f:
        filelines = f.readlines()

for i in filelines:
    if "side_length" in i:
        side_length = int(i.split()[-1])
    if "tiles" in i:
        tiles = int(i.split()[-1])
    if "rows" in i:
        rows = int(i.split()[-1])
    if "window_height" in i:
        globalheight = int(i.split()[-1])
    if "window_width" in i:
        globalwidth = int(i.split()[-1])


#apothem and tile height are derived from side length
apothem = (m.sqrt(3)*side_length)/(2)
'''n is the distance between the top left corner of the rectangle that
would touch the top and bottom as well as side points of the hexagon and the
first point of the hexagon. In other words, 2* the apothem - side length'''
n = m.sqrt((side_length**2)-(apothem**2))
#always default these values to zero
xoffset = 0
yoffset = 0

root = tk.Tk()
root.title("hex tiles")
root = tk.Canvas(root, width=globalwidth,height=globalwidth,bg='white')

root.pack()


currentrow = 0
for i in range(rows):
    if currentrow % 2 != 0:
        xoffset = n + side_length
    else:
        xoffset = 0
    for i in range(tiles):
        xA = n + i*2*(side_length + n) + xoffset
        yA = 0 + yoffset
        xF = (i*2*(side_length+n)) + xoffset
        yF = apothem + yoffset
        xB = xA + side_length
        yB = yA
        xC = xF + (side_length + (2*n))
        yC = apothem + yoffset
        xD = xB
        yD = yB + (2*apothem)
        xE = xA
        yE = yD
        root.create_polygon(xA,yA,xB,yB,xC,yC,xD,yD,xE,yE,xF,yF,fill='',outline='black')
    currentrow += 1
    yoffset += apothem
    
root.mainloop()
