import glm
import lookuptable 

def marching_cubes(data, objname="marching_cubes.obj"):
    vertices = []
    faces = []
    xDim = len(data)-1
    yDim = len(data[0]) - 1
    zDim = len(data[0][0]) - 1
    for j in range(yDim):
        for i in range(xDim):
            for k in range(zDim):
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
               
                base_face_index = len(vertices)
                # see marching cubes papers figure 4. cuber numbering
                e = []
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
                
                f = {}
                for face in lookuptable.lookuptable[index]:
                    x0 = int(face.x)-1
                    y0 = int(face.y)-1
                    z0 = int(face.z)-1
                    if x0 not in f.keys():
                        f[x0] = len(vertices)
                        vertices.append(e[x0])
                    if y0 not in f.keys():
                        f[y0] =  len(vertices)
                        vertices.append(e[y0])
                    if z0 not in f.keys():
                        f[z0] = len(vertices)
                        vertices.append(e[z0])
                
                for face in lookuptable.lookuptable[index]:
                    faces.append(glm.vec3(f[int(face.x)-1]+1,f[int(face.y)-1]+1,f[int(face.z)-1]+1))

    with open(objname, 'w') as of:
        for e0 in vertices:
            of.write('v ' + str(e0.x) + ' ' + str(e0.y) + ' ' + str(e0.z)+'\n')
        for f0 in faces:
            of.write('f ' + str(int(f0.x)) + ' ' + str(int(f0.y)) + ' ' + str(int(f0.z))+'\n')
                
