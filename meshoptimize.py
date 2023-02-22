import pymeshlab as ml
ms = ml.MeshSet()
ms.load_new_mesh('scene.obj')
m = ms.current_mesh()
print('input mesh has', m.vertex_number(), 'vertex and', m.face_number(), 'faces')

#Target number of vertex
TARGET=142520

#Estimate number of faces to have 100+10000 vertex using Euler
numFaces = 100 + 2*TARGET 
# numFaces = 170528


#Simplify the mesh. Only first simplification will be agressive
while (ms.current_mesh().vertex_number() > TARGET):
    ms.apply_filter('meshing_decimation_quadric_edge_collapse', targetfacenum=numFaces, preservenormal=True)
    print("Decimated to", numFaces, "faces mesh has", ms.current_mesh().vertex_number(), "vertex")
    #Refine our estimation to slowly converge to TARGET vertex number
    numFaces = numFaces - (ms.current_mesh().vertex_number() - TARGET)

m = ms.current_mesh()
print('output mesh has', m.vertex_number(), 'vertex and', m.face_number(), 'faces')
ms.save_current_mesh('output-small.obj')