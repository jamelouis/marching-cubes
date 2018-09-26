import sys
sys.path.append('../../') # https://stackoverflow.com/questions/15109548/set-pythonpath-before-import-statements
from marching_cubes import marching_cubes
import random
import glm


def generate_data(xDim,yDim,zDim):
    n = yDim
    data = []

    for j in range(yDim):
        rc = []
        for i in range(xDim):
            r = []
            for k in range(zDim):
                f = 0.0
                
                d = glm.length(glm.vec3(i,j,k) - glm.vec3(n/2,n/2,n/2)) 
                f = n / 3 - d
                    
                if f > 0.0:
                    r.append(1)
                else:
                    r.append(0)
            rc.append(r)
        data.append(rc)

    
    return data

test_data = generate_data(96, 96, 96)

if __name__ == "__main__":
    
    marching_cubes(test_data,'cascade.obj')
