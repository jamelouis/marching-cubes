import sys
sys.path.append('../../') # https://stackoverflow.com/questions/15109548/set-pythonpath-before-import-statements
from marching_cubes import marching_cubes

test_data = [
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]],
        [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]],
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        ]

if __name__ == "__main__":
    marching_cubes(test_data,'fourpoint.obj')
