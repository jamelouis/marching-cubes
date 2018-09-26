# lookuptable download from 
# http://users.polytech.unice.fr/~lingrand/MarchingCubes/applet.html

lookuptable = []

with open("TrianglesS.lut.txt","r") as f:
    content = f.read().split('\n')
    for index,line in enumerate(content):
        #print index, line.strip()
        line = line.strip()
        line = line.split(',')
        faces = []
        for n in line:
            if len(n)>0 and int(n) >= 0:
                faces.append(int(n)+1)
        lookuptable.append(faces)

with open("lookuptable.py","w") as f:
    f.write("import glm\n")
    f.write("lookuptable = [")
    for faces in lookuptable:
        line = '\t['
        for i in range(0,len(faces),3):
            line += 'glm.vec3('
            line += str(faces[i])
            line += ','
            line += str(faces[i+1])
            line += ','
            line += str(faces[i+2])
            line += '),'
        line+= '],'
        f.write(line)
        f.write('\n')
    f.write("]")
