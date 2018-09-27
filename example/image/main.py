import sys
sys.path.append('../../') # https://stackoverflow.com/questions/15109548/set-pythonpath-before-import-statements
from marching_cubes import marching_cubes
from PIL import Image
import math

def generate_data(image_name,n):

    im = Image.open(image_name)
    im = im.resize((n,n))
    im = im.convert('L')

    t = []
    for i in range(n):
        r = [0]
        for j in range(n):
            c = im.getpixel((i,j))
            if c > 0:
                r.append(0)
            else:
                r.append(1)
        r.append(0)
        t.append(r)
    
    b = []
    for i in range(n):
        r = []
        for j in range(n):
            r.append(0)
        b.append(r)

    data = []

    data.append(b)
    for k in range(n):
        data.append(t)
    data.append(b)

    return data

def generate_data_rotate(image_name, n):
    im = Image.open(image_name)
    im = im.resize((n, n))
    im = im.convert('L')
    t = []
    for i in range(n):
        r = []
        for j in range(n):
            c = im.getpixel((i,j))
            print c
            if c > 128 :
                r.append(0)
            else:
                r.append(1)
        t.append(r)

    for r in t:
        print r

    data = []
    for j in range(n):
        plane = []
        for i in range(2*n):
            r = []
            for k in range(2*n):
                jj = j
                ii = int(math.sqrt((i-n)**2 + (k-n)**2))
                if ii>=0 and ii < n  and jj < n:
                    r.append(t[ii][jj])
                else:
                    r.append(0)
            plane.append(r)
        data.append(plane)

    return data
    
if __name__ == "__main__":
    data = generate_data_rotate('cup.png',30)
    marching_cubes(data,'cup.obj')
    