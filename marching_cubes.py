import glm
import lookuptable 
import random

test_data0 = [
        [[1,0],[0,0]],
        [[0,1],[0,0]],
        ]





def generate_data(n,up,limit):
    data = []
    for k in range(n):
        rc = []
        for i in range(n):
            r = []
            for j in range(n):
                if random.randint(0,up) > limit:
                    r.append(1)
                else:
                    r.append(0)
            rc.append(r)
        data.append(rc)
    return data

def marching_cubes(data, objname="marching_cubes.obj"):
    e = []
    f = []
    n = len(data)-1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                v1 = data[i][j][k]
                v2 = data[i+1][j][k]
                v3 = data[i+1][j][k+1]
                v4 = data[i][j][k+1]
                v5 = data[i][j+1][k]
                v6 = data[i+1][j+1][k]
                v7 = data[i+1][j+1][k+1]
                v8 = data[i][j+1][k+1]

                index = v1 | v2 << 1 | v3 << 2 | v4 << 3 | v5 << 4 
                index = index | v6 << 5 | v7 << 6 | v8 << 7
               
                base_face_index = len(e)
                # see marching cubes papers figure 4. cuber numbering
                e.append(glm.vec3( (i+0.5),j,k))
                e.append(glm.vec3( i+1,j,k+0.5))
                e.append(glm.vec3( i+0.5, j, k+1))
                e.append(glm.vec3( i, j, k+0.5))

                e.append(glm.vec3( i+0.5, j+1, k))
                e.append(glm.vec3( i+1,   j+1, k+0.5))
                e.append(glm.vec3( i+0.5, j+1, k+1))
                e.append(glm.vec3( i,     j+1, k+0.5))

                e.append(glm.vec3(i, j+0.5, k))
                e.append(glm.vec3(i+1, j+0.5, k))
                e.append(glm.vec3(i, j+0.5, k+1))
                e.append(glm.vec3(i+1,j+0.5,k+1))
                
                for face in lookuptable.lookuptable[index]:
                    f.append(face + glm.vec3(base_face_index))

    with open(objname, 'w') as of:
        for e0 in e:
            of.write('v ' + str(e0.x) + ' ' + str(e0.y) + ' ' + str(e0.z)+'\n')
        for f0 in f:
            of.write('f ' + str(int(f0.x)) + ' ' + str(int(f0.y)) + ' ' + str(int(f0.z))+'\n')
                
