import glm
import random

lut = {
        1:{ 'f':[ glm.vec3(1, 9, 4)], 'n': [1,1,1] },
        2:{ 'f':[ glm.vec3(1, 2, 10)], 'n':[1,1,1]},
        4:{ 'f':[ glm.vec3(2, 3, 12)]},
        8:{ 'f': [glm.vec3(3, 4, 11)]},
        16:{ 'f': [glm.vec3(5, 8, 9)]},
        32:{ 'f': [glm.vec3(6,5,10)]},
        64:{ 'f': [glm.vec3(7,6,12)]},
        128:{ 'f': [glm.vec3(7,11,8)]},
        3:{'f':[glm.vec3(9,4,2),glm.vec3(10,9,2)]},
        6:{'f':[glm.vec3(1,3,10),glm.vec3(3,12,10)]},
        12:{'f':[glm.vec3(2,11,12),glm.vec3(2,4,11)]},
        9:{'f':[glm.vec3(11,3,9),glm.vec3(1,9,3)]},
        17:{'f':[glm.vec3(1,8,4),glm.vec3(1,5,8)]},
        34:{'f':[glm.vec3(1,2,5),glm.vec3(2,6,5)]},
        68:{'f':[glm.vec3(2,3,7),glm.vec3(2,7,6)]}, #v7 - v3
        #v4-v8
        136:{'f':[glm.vec3(8,7,3),glm.vec3(8,3,4)]},
        #v5-v6
        48:{'f':[glm.vec3(8,9,10),glm.vec3(8,10,6)]},
        #v6-v7
        96:{'f':[glm.vec3(5,10,12),glm.vec3(5,12,7)]},
        #v7-v8
        192:{'f':[glm.vec3(8,6,12),glm.vec3(8,12,11)]},
        #v8-v5
        144:{'f':[glm.vec3(9,5,7),glm.vec3(9,7,11)]},
        ## case 3
        #v1 - v3
        5:{'f':[glm.vec3(1,9,4),glm.vec3(2,3,12)]},



        #v1-v2-v6-v5
        51:{'f':[glm.vec3(4,2,6),glm.vec3(4,6,8)]},
        #v4-v3-v7-v8
        204:{'f':[glm.vec3(4,6,2),glm.vec3(4,8,6)]},
        #v1-v2-v3-v4
        15:{'f':[glm.vec3(9,11,12),glm.vec3(9,12,10)]},
        #v5-v6-v7-v8
        240:{'f':[glm.vec3(9,12,11),glm.vec3(9,10,12)]},
        #v1-v5-v8-v4
        153:{'f':[glm.vec3(1,5,7),glm.vec3(1,7,3)]},
        #v2-v6-v7-v3
        102:{'f':[glm.vec3(1,7,5),glm.vec3(1,3,7)]}
    }

lookuptable = [
    [],
    [glm.vec3(1,9,4),],
    [glm.vec3(1,2,10),],
    [glm.vec3(2,9,4),glm.vec3(10,9,2),],
    [glm.vec3(2,3,12),],
    [glm.vec3(1,9,4),glm.vec3(2,3,12),],
    [glm.vec3(10,3,12),glm.vec3(1,3,10),],
    [glm.vec3(3,9,4),glm.vec3(3,12,9),glm.vec3(12,10,9),],
    [glm.vec3(4,11,3),],
    [glm.vec3(1,11,3),glm.vec3(9,11,1),],
    [glm.vec3(2,10,1),glm.vec3(3,4,11),],
    [glm.vec3(2,11,3),glm.vec3(2,10,11),glm.vec3(10,9,11),],
    [glm.vec3(4,12,2),glm.vec3(11,12,4),],
    [glm.vec3(1,12,2),glm.vec3(1,9,12),glm.vec3(9,11,12),],
    [glm.vec3(4,10,1),glm.vec3(4,11,10),glm.vec3(11,12,10),],
    [glm.vec3(10,9,12),glm.vec3(12,9,11),],
    [glm.vec3(5,8,9),],
    [glm.vec3(5,4,1),glm.vec3(8,4,5),],
    [glm.vec3(1,2,10),glm.vec3(9,5,8),],
    [glm.vec3(5,2,10),glm.vec3(5,8,2),glm.vec3(8,4,2),],
    [glm.vec3(2,3,12),glm.vec3(9,5,8),],
    [glm.vec3(4,5,8),glm.vec3(4,1,5),glm.vec3(2,3,12),],
    [glm.vec3(10,3,12),glm.vec3(10,1,3),glm.vec3(9,5,8),],
    [glm.vec3(3,12,10),glm.vec3(3,10,8),glm.vec3(3,8,4),glm.vec3(8,10,5),],
    [glm.vec3(9,5,8),glm.vec3(4,11,3),],
    [glm.vec3(11,5,8),glm.vec3(11,3,5),glm.vec3(3,1,5),],
    [glm.vec3(10,1,2),glm.vec3(9,5,8),glm.vec3(3,4,11),],
    [glm.vec3(5,8,11),glm.vec3(10,5,11),glm.vec3(10,11,3),glm.vec3(10,3,2),],
    [glm.vec3(4,12,2),glm.vec3(4,11,12),glm.vec3(8,9,5),],
    [glm.vec3(2,11,12),glm.vec3(2,5,11),glm.vec3(2,1,5),glm.vec3(8,11,5),],
    [glm.vec3(5,8,9),glm.vec3(10,1,11),glm.vec3(10,11,12),glm.vec3(11,1,4),],
    [glm.vec3(5,8,11),glm.vec3(5,11,10),glm.vec3(10,11,12),],
    [glm.vec3(10,6,5),],
    [glm.vec3(10,6,5),glm.vec3(1,9,4),],
    [glm.vec3(1,6,5),glm.vec3(2,6,1),],
    [glm.vec3(9,6,5),glm.vec3(9,4,6),glm.vec3(4,2,6),],
    [glm.vec3(2,3,12),glm.vec3(10,6,5),],
    [glm.vec3(4,1,9),glm.vec3(2,3,12),glm.vec3(5,10,6),],
    [glm.vec3(6,3,12),glm.vec3(6,5,3),glm.vec3(5,1,3),],
    [glm.vec3(3,12,6),glm.vec3(4,3,6),glm.vec3(4,6,5),glm.vec3(4,5,9),],
    [glm.vec3(10,6,5),glm.vec3(3,4,11),],
    [glm.vec3(1,11,3),glm.vec3(1,9,11),glm.vec3(5,10,6),],
    [glm.vec3(1,6,5),glm.vec3(1,2,6),glm.vec3(3,4,11),],
    [glm.vec3(3,2,6),glm.vec3(3,6,9),glm.vec3(3,9,11),glm.vec3(5,9,6),],
    [glm.vec3(12,4,11),glm.vec3(12,2,4),glm.vec3(10,6,5),],
    [glm.vec3(5,10,6),glm.vec3(1,9,2),glm.vec3(9,12,2),glm.vec3(9,11,12),],
    [glm.vec3(6,5,1),glm.vec3(6,1,11),glm.vec3(6,11,12),glm.vec3(11,1,4),],
    [glm.vec3(6,5,9),glm.vec3(6,9,12),glm.vec3(12,9,11),],
    [glm.vec3(10,8,9),glm.vec3(6,8,10),],
    [glm.vec3(10,4,1),glm.vec3(10,6,4),glm.vec3(6,8,4),],
    [glm.vec3(1,8,9),glm.vec3(1,2,8),glm.vec3(2,6,8),],
    [glm.vec3(2,6,4),glm.vec3(4,6,8),],
    [glm.vec3(10,8,9),glm.vec3(10,6,8),glm.vec3(12,2,3),],
    [glm.vec3(12,2,3),glm.vec3(10,6,1),glm.vec3(6,4,1),glm.vec3(6,8,4),],
    [glm.vec3(9,1,3),glm.vec3(9,3,6),glm.vec3(9,6,8),glm.vec3(12,6,3),],
    [glm.vec3(3,12,6),glm.vec3(3,6,4),glm.vec3(4,6,8),],
    [glm.vec3(8,10,6),glm.vec3(8,9,10),glm.vec3(4,11,3),],
    [glm.vec3(10,6,8),glm.vec3(10,8,3),glm.vec3(10,3,1),glm.vec3(3,8,11),],
    [glm.vec3(3,4,11),glm.vec3(1,2,9),glm.vec3(2,8,9),glm.vec3(2,6,8),],
    [glm.vec3(11,3,2),glm.vec3(11,2,8),glm.vec3(8,2,6),],
    [glm.vec3(10,6,9),glm.vec3(9,6,8),glm.vec3(12,2,4),glm.vec3(12,4,11),],
    [glm.vec3(6,8,11),glm.vec3(6,11,12),glm.vec3(2,1,10),],
    [glm.vec3(11,12,6),glm.vec3(11,6,8),glm.vec3(9,1,4),],
    [glm.vec3(11,12,6),glm.vec3(8,11,6),],
    [glm.vec3(12,7,6),],
    [glm.vec3(1,9,4),glm.vec3(6,12,7),],
    [glm.vec3(10,1,2),glm.vec3(6,12,7),],
    [glm.vec3(2,9,4),glm.vec3(2,10,9),glm.vec3(6,12,7),],
    [glm.vec3(2,7,6),glm.vec3(3,7,2),],
    [glm.vec3(2,7,6),glm.vec3(2,3,7),glm.vec3(4,1,9),],
    [glm.vec3(10,7,6),glm.vec3(10,1,7),glm.vec3(1,3,7),],
    [glm.vec3(6,10,9),glm.vec3(6,9,3),glm.vec3(6,3,7),glm.vec3(4,3,9),],
    [glm.vec3(3,4,11),glm.vec3(12,7,6),],
    [glm.vec3(11,1,9),glm.vec3(11,3,1),glm.vec3(12,7,6),],
    [glm.vec3(1,2,10),glm.vec3(3,4,11),glm.vec3(6,12,7),],
    [glm.vec3(6,12,7),glm.vec3(2,10,3),glm.vec3(10,11,3),glm.vec3(10,9,11),],
    [glm.vec3(7,4,11),glm.vec3(7,6,4),glm.vec3(6,2,4),],
    [glm.vec3(1,9,11),glm.vec3(1,11,6),glm.vec3(1,6,2),glm.vec3(6,11,7),],
    [glm.vec3(4,11,7),glm.vec3(1,4,7),glm.vec3(1,7,6),glm.vec3(1,6,10),],
    [glm.vec3(7,6,10),glm.vec3(7,10,11),glm.vec3(11,10,9),],
    [glm.vec3(6,12,7),glm.vec3(5,8,9),],
    [glm.vec3(5,4,1),glm.vec3(5,8,4),glm.vec3(7,6,12),],
    [glm.vec3(2,10,1),glm.vec3(6,12,7),glm.vec3(9,5,8),],
    [glm.vec3(12,7,6),glm.vec3(2,10,8),glm.vec3(2,8,4),glm.vec3(8,10,5),],
    [glm.vec3(7,2,3),glm.vec3(7,6,2),glm.vec3(5,8,9),],
    [glm.vec3(2,3,6),glm.vec3(6,3,7),glm.vec3(4,1,5),glm.vec3(4,5,8),],
    [glm.vec3(9,5,8),glm.vec3(10,1,6),glm.vec3(1,7,6),glm.vec3(1,3,7),],
    [glm.vec3(8,4,3),glm.vec3(8,3,7),glm.vec3(6,10,5),],
    [glm.vec3(4,11,3),glm.vec3(8,9,5),glm.vec3(12,7,6),],
    [glm.vec3(6,12,7),glm.vec3(5,8,3),glm.vec3(5,3,1),glm.vec3(3,8,11),],
    [glm.vec3(1,2,10),glm.vec3(5,8,9),glm.vec3(3,4,11),glm.vec3(6,12,7),],
    [glm.vec3(10,5,6),glm.vec3(12,3,2),glm.vec3(8,11,7),],
    [glm.vec3(9,5,8),glm.vec3(4,11,6),glm.vec3(4,6,2),glm.vec3(6,11,7),],
    [glm.vec3(6,2,1),glm.vec3(6,1,5),glm.vec3(8,11,7),],
    [glm.vec3(1,4,9),glm.vec3(5,6,10),glm.vec3(11,7,8),],
    [glm.vec3(5,6,10),glm.vec3(8,11,7),],
    [glm.vec3(12,5,10),glm.vec3(7,5,12),],
    [glm.vec3(5,12,7),glm.vec3(5,10,12),glm.vec3(1,9,4),],
    [glm.vec3(12,1,2),glm.vec3(12,7,1),glm.vec3(7,5,1),],
    [glm.vec3(9,4,2),glm.vec3(9,2,7),glm.vec3(9,7,5),glm.vec3(7,2,12),],
    [glm.vec3(2,5,10),glm.vec3(2,3,5),glm.vec3(3,7,5),],
    [glm.vec3(4,1,9),glm.vec3(2,3,10),glm.vec3(3,5,10),glm.vec3(3,7,5),],
    [glm.vec3(1,3,5),glm.vec3(5,3,7),],
    [glm.vec3(9,4,3),glm.vec3(9,3,5),glm.vec3(5,3,7),],
    [glm.vec3(12,5,10),glm.vec3(12,7,5),glm.vec3(11,3,4),],
    [glm.vec3(1,9,3),glm.vec3(3,9,11),glm.vec3(5,10,12),glm.vec3(5,12,7),],
    [glm.vec3(4,11,3),glm.vec3(1,2,7),glm.vec3(1,7,5),glm.vec3(7,2,12),],
    [glm.vec3(7,5,9),glm.vec3(7,9,11),glm.vec3(3,2,12),],
    [glm.vec3(10,7,5),glm.vec3(10,4,7),glm.vec3(10,2,4),glm.vec3(11,7,4),],
    [glm.vec3(9,11,7),glm.vec3(9,7,5),glm.vec3(10,2,1),],
    [glm.vec3(4,11,7),glm.vec3(4,7,1),glm.vec3(1,7,5),],
    [glm.vec3(7,5,9),glm.vec3(11,7,9),],
    [glm.vec3(8,12,7),glm.vec3(8,9,12),glm.vec3(9,10,12),],
    [glm.vec3(1,8,4),glm.vec3(1,12,8),glm.vec3(1,10,12),glm.vec3(7,8,12),],
    [glm.vec3(12,7,8),glm.vec3(2,12,8),glm.vec3(2,8,9),glm.vec3(2,9,1),],
    [glm.vec3(12,7,8),glm.vec3(12,8,2),glm.vec3(2,8,4),],
    [glm.vec3(2,3,7),glm.vec3(2,7,9),glm.vec3(2,9,10),glm.vec3(9,7,8),],
    [glm.vec3(3,7,8),glm.vec3(3,8,4),glm.vec3(1,10,2),],
    [glm.vec3(8,9,1),glm.vec3(8,1,7),glm.vec3(7,1,3),],
    [glm.vec3(8,4,3),glm.vec3(7,8,3),],
    [glm.vec3(3,4,11),glm.vec3(12,7,9),glm.vec3(12,9,10),glm.vec3(9,7,8),],
    [glm.vec3(3,1,10),glm.vec3(3,10,12),glm.vec3(7,8,11),],
    [glm.vec3(2,12,3),glm.vec3(4,9,1),glm.vec3(7,8,11),],
    [glm.vec3(12,3,2),glm.vec3(7,8,11),],
    [glm.vec3(9,10,2),glm.vec3(9,2,4),glm.vec3(11,7,8),],
    [glm.vec3(1,10,2),glm.vec3(11,7,8),],
    [glm.vec3(4,9,1),glm.vec3(11,7,8),],
    [glm.vec3(8,11,7),],
    [glm.vec3(8,7,11),],
    [glm.vec3(4,1,9),glm.vec3(11,8,7),],
    [glm.vec3(1,2,10),glm.vec3(11,8,7),],
    [glm.vec3(9,2,10),glm.vec3(9,4,2),glm.vec3(11,8,7),],
    [glm.vec3(12,2,3),glm.vec3(7,11,8),],
    [glm.vec3(2,3,12),glm.vec3(4,1,9),glm.vec3(7,11,8),],
    [glm.vec3(3,10,1),glm.vec3(3,12,10),glm.vec3(7,11,8),],
    [glm.vec3(3,11,4),glm.vec3(12,9,7),glm.vec3(12,10,9),glm.vec3(9,8,7),],
    [glm.vec3(8,3,4),glm.vec3(7,3,8),],
    [glm.vec3(8,1,9),glm.vec3(8,7,1),glm.vec3(7,3,1),],
    [glm.vec3(3,8,7),glm.vec3(3,4,8),glm.vec3(1,2,10),],
    [glm.vec3(2,7,3),glm.vec3(2,9,7),glm.vec3(2,10,9),glm.vec3(9,8,7),],
    [glm.vec3(12,8,7),glm.vec3(12,2,8),glm.vec3(2,4,8),],
    [glm.vec3(12,8,7),glm.vec3(2,8,12),glm.vec3(2,9,8),glm.vec3(2,1,9),],
    [glm.vec3(1,4,8),glm.vec3(1,8,12),glm.vec3(1,12,10),glm.vec3(7,12,8),],
    [glm.vec3(8,7,12),glm.vec3(8,12,9),glm.vec3(9,12,10),],
    [glm.vec3(7,9,5),glm.vec3(11,9,7),],
    [glm.vec3(4,7,11),glm.vec3(4,1,7),glm.vec3(1,5,7),],
    [glm.vec3(9,7,11),glm.vec3(9,5,7),glm.vec3(10,1,2),],
    [glm.vec3(10,5,7),glm.vec3(10,7,4),glm.vec3(10,4,2),glm.vec3(11,4,7),],
    [glm.vec3(7,9,5),glm.vec3(7,11,9),glm.vec3(3,12,2),],
    [glm.vec3(4,3,11),glm.vec3(1,7,2),glm.vec3(1,5,7),glm.vec3(7,12,2),],
    [glm.vec3(1,3,9),glm.vec3(3,11,9),glm.vec3(5,12,10),glm.vec3(5,7,12),],
    [glm.vec3(12,10,5),glm.vec3(12,5,7),glm.vec3(11,4,3),],
    [glm.vec3(9,3,4),glm.vec3(9,5,3),glm.vec3(5,7,3),],
    [glm.vec3(1,5,3),glm.vec3(5,7,3),],
    [glm.vec3(4,9,1),glm.vec3(2,10,3),glm.vec3(3,10,5),glm.vec3(3,5,7),],
    [glm.vec3(2,10,5),glm.vec3(2,5,3),glm.vec3(3,5,7),],
    [glm.vec3(9,2,4),glm.vec3(9,7,2),glm.vec3(9,5,7),glm.vec3(7,12,2),],
    [glm.vec3(12,2,1),glm.vec3(12,1,7),glm.vec3(7,1,5),],
    [glm.vec3(5,7,12),glm.vec3(5,12,10),glm.vec3(1,4,9),],
    [glm.vec3(12,10,5),glm.vec3(7,12,5),],
    [glm.vec3(5,10,6),glm.vec3(8,7,11),],
    [glm.vec3(1,9,4),glm.vec3(5,10,6),glm.vec3(11,8,7),],
    [glm.vec3(6,1,2),glm.vec3(6,5,1),glm.vec3(8,7,11),],
    [glm.vec3(9,8,5),glm.vec3(4,6,11),glm.vec3(4,2,6),glm.vec3(6,7,11),],
    [glm.vec3(10,6,5),glm.vec3(12,2,3),glm.vec3(8,7,11),],
    [glm.vec3(1,10,2),glm.vec3(5,9,8),glm.vec3(3,11,4),glm.vec3(6,7,12),],
    [glm.vec3(6,7,12),glm.vec3(5,3,8),glm.vec3(5,1,3),glm.vec3(3,11,8),],
    [glm.vec3(4,3,11),glm.vec3(8,5,9),glm.vec3(12,6,7),],
    [glm.vec3(8,3,4),glm.vec3(8,7,3),glm.vec3(6,5,10),],
    [glm.vec3(9,8,5),glm.vec3(10,6,1),glm.vec3(1,6,7),glm.vec3(1,7,3),],
    [glm.vec3(2,6,3),glm.vec3(6,7,3),glm.vec3(4,5,1),glm.vec3(4,8,5),],
    [glm.vec3(7,3,2),glm.vec3(7,2,6),glm.vec3(5,9,8),],
    [glm.vec3(12,6,7),glm.vec3(2,8,10),glm.vec3(2,4,8),glm.vec3(8,5,10),],
    [glm.vec3(2,1,10),glm.vec3(6,7,12),glm.vec3(9,8,5),],
    [glm.vec3(5,1,4),glm.vec3(5,4,8),glm.vec3(7,12,6),],
    [glm.vec3(6,7,12),glm.vec3(5,9,8),],
    [glm.vec3(7,10,6),glm.vec3(7,11,10),glm.vec3(11,9,10),],
    [glm.vec3(4,7,11),glm.vec3(1,7,4),glm.vec3(1,6,7),glm.vec3(1,10,6),],
    [glm.vec3(1,11,9),glm.vec3(1,6,11),glm.vec3(1,2,6),glm.vec3(6,7,11),],
    [glm.vec3(7,11,4),glm.vec3(7,4,6),glm.vec3(6,4,2),],
    [glm.vec3(6,7,12),glm.vec3(2,3,10),glm.vec3(10,3,11),glm.vec3(10,11,9),],
    [glm.vec3(1,10,2),glm.vec3(3,11,4),glm.vec3(6,7,12),],
    [glm.vec3(11,9,1),glm.vec3(11,1,3),glm.vec3(12,6,7),],
    [glm.vec3(3,11,4),glm.vec3(12,6,7),],
    [glm.vec3(6,9,10),glm.vec3(6,3,9),glm.vec3(6,7,3),glm.vec3(4,9,3),],
    [glm.vec3(10,6,7),glm.vec3(10,7,1),glm.vec3(1,7,3),],
    [glm.vec3(2,6,7),glm.vec3(2,7,3),glm.vec3(4,9,1),],
    [glm.vec3(2,6,7),glm.vec3(3,2,7),],
    [glm.vec3(2,4,9),glm.vec3(2,9,10),glm.vec3(6,7,12),],
    [glm.vec3(10,2,1),glm.vec3(6,7,12),],
    [glm.vec3(1,4,9),glm.vec3(6,7,12),],
    [glm.vec3(12,6,7),],
    [glm.vec3(11,6,12),glm.vec3(8,6,11),],
    [glm.vec3(11,6,12),glm.vec3(11,8,6),glm.vec3(9,4,1),],
    [glm.vec3(6,11,8),glm.vec3(6,12,11),glm.vec3(2,10,1),],
    [glm.vec3(10,9,6),glm.vec3(9,8,6),glm.vec3(12,4,2),glm.vec3(12,11,4),],
    [glm.vec3(11,2,3),glm.vec3(11,8,2),glm.vec3(8,6,2),],
    [glm.vec3(3,11,4),glm.vec3(1,9,2),glm.vec3(2,9,8),glm.vec3(2,8,6),],
    [glm.vec3(10,8,6),glm.vec3(10,3,8),glm.vec3(10,1,3),glm.vec3(3,11,8),],
    [glm.vec3(8,6,10),glm.vec3(8,10,9),glm.vec3(4,3,11),],
    [glm.vec3(3,6,12),glm.vec3(3,4,6),glm.vec3(4,8,6),],
    [glm.vec3(9,3,1),glm.vec3(9,6,3),glm.vec3(9,8,6),glm.vec3(12,3,6),],
    [glm.vec3(12,3,2),glm.vec3(10,1,6),glm.vec3(6,1,4),glm.vec3(6,4,8),],
    [glm.vec3(10,9,8),glm.vec3(10,8,6),glm.vec3(12,3,2),],
    [glm.vec3(2,4,6),glm.vec3(4,8,6),],
    [glm.vec3(1,9,8),glm.vec3(1,8,2),glm.vec3(2,8,6),],
    [glm.vec3(10,1,4),glm.vec3(10,4,6),glm.vec3(6,4,8),],
    [glm.vec3(10,9,8),glm.vec3(6,10,8),],
    [glm.vec3(6,9,5),glm.vec3(6,12,9),glm.vec3(12,11,9),],
    [glm.vec3(6,1,5),glm.vec3(6,11,1),glm.vec3(6,12,11),glm.vec3(11,4,1),],
    [glm.vec3(5,6,10),glm.vec3(1,2,9),glm.vec3(9,2,12),glm.vec3(9,12,11),],
    [glm.vec3(12,11,4),glm.vec3(12,4,2),glm.vec3(10,5,6),],
    [glm.vec3(3,6,2),glm.vec3(3,9,6),glm.vec3(3,11,9),glm.vec3(5,6,9),],
    [glm.vec3(1,5,6),glm.vec3(1,6,2),glm.vec3(3,11,4),],
    [glm.vec3(1,3,11),glm.vec3(1,11,9),glm.vec3(5,6,10),],
    [glm.vec3(10,5,6),glm.vec3(3,11,4),],
    [glm.vec3(3,6,12),glm.vec3(4,6,3),glm.vec3(4,5,6),glm.vec3(4,9,5),],
    [glm.vec3(6,12,3),glm.vec3(6,3,5),glm.vec3(5,3,1),],
    [glm.vec3(4,9,1),glm.vec3(2,12,3),glm.vec3(5,6,10),],
    [glm.vec3(2,12,3),glm.vec3(10,5,6),],
    [glm.vec3(9,5,6),glm.vec3(9,6,4),glm.vec3(4,6,2),],
    [glm.vec3(1,5,6),glm.vec3(2,1,6),],
    [glm.vec3(10,5,6),glm.vec3(1,4,9),],
    [glm.vec3(10,5,6),],
    [glm.vec3(5,11,8),glm.vec3(5,10,11),glm.vec3(10,12,11),],
    [glm.vec3(5,9,8),glm.vec3(10,11,1),glm.vec3(10,12,11),glm.vec3(11,4,1),],
    [glm.vec3(2,12,11),glm.vec3(2,11,5),glm.vec3(2,5,1),glm.vec3(8,5,11),],
    [glm.vec3(4,2,12),glm.vec3(4,12,11),glm.vec3(8,5,9),],
    [glm.vec3(5,11,8),glm.vec3(10,11,5),glm.vec3(10,3,11),glm.vec3(10,2,3),],
    [glm.vec3(10,2,1),glm.vec3(9,8,5),glm.vec3(3,11,4),],
    [glm.vec3(11,8,5),glm.vec3(11,5,3),glm.vec3(3,5,1),],
    [glm.vec3(9,8,5),glm.vec3(4,3,11),],
    [glm.vec3(3,10,12),glm.vec3(3,8,10),glm.vec3(3,4,8),glm.vec3(8,5,10),],
    [glm.vec3(10,12,3),glm.vec3(10,3,1),glm.vec3(9,8,5),],
    [glm.vec3(4,8,5),glm.vec3(4,5,1),glm.vec3(2,12,3),],
    [glm.vec3(2,12,3),glm.vec3(9,8,5),],
    [glm.vec3(5,10,2),glm.vec3(5,2,8),glm.vec3(8,2,4),],
    [glm.vec3(1,10,2),glm.vec3(9,8,5),],
    [glm.vec3(5,1,4),glm.vec3(8,5,4),],
    [glm.vec3(5,9,8),],
    [glm.vec3(10,12,9),glm.vec3(12,11,9),],
    [glm.vec3(4,1,10),glm.vec3(4,10,11),glm.vec3(11,10,12),],
    [glm.vec3(1,2,12),glm.vec3(1,12,9),glm.vec3(9,12,11),],
    [glm.vec3(4,2,12),glm.vec3(11,4,12),],
    [glm.vec3(2,3,11),glm.vec3(2,11,10),glm.vec3(10,11,9),],
    [glm.vec3(2,1,10),glm.vec3(3,11,4),],
    [glm.vec3(1,3,11),glm.vec3(9,1,11),],
    [glm.vec3(4,3,11),],
    [glm.vec3(3,4,9),glm.vec3(3,9,12),glm.vec3(12,9,10),],
    [glm.vec3(10,12,3),glm.vec3(1,10,3),],
    [glm.vec3(1,4,9),glm.vec3(2,12,3),],
    [glm.vec3(2,12,3),],
    [glm.vec3(2,4,9),glm.vec3(10,2,9),],
    [glm.vec3(1,10,2),],
    [glm.vec3(1,4,9),],
    [],
    [],
]
test_data0 = [
        [[1,0],[0,0]],
        [[0,1],[0,0]],
        ]

test_data = [
        [[0,0,0],[0,0,0],[0,0,0]],
        [[0,0,0],[0,1,0],[0,0,0]],
        [[0,0,0],[0,0,0],[0,0,0]]
        ]

test_data2 = [
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]],
        [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]],
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
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

def marching_cubes(data):
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
                
                for face in lookuptable[index]:
                    f.append(face + glm.vec3(base_face_index))

    with open('test.obj', 'w') as of:
        for e0 in e:
            of.write('v ' + str(e0.x) + ' ' + str(e0.y) + ' ' + str(e0.z)+'\n')
        for f0 in f:
            of.write('f ' + str(int(f0.x)) + ' ' + str(int(f0.y)) + ' ' + str(int(f0.z))+'\n')
                
if __name__ == '__main__':
    data = generate_data(20, 10, 2)
    marching_cubes(data)
