
import pyvista as pv

# Load the first OBJ file
mesh1 = pv.read('scene.glb')
# mesh1 = pv.read('output-small.obj')

# Load the second OBJ file
mesh2 = pv.read('duck.obj')

# add two meshes
plotter = pv.Plotter()
plotter.add_mesh(mesh1, color='red')
plotter.add_mesh(mesh2, color='blue')

# camera
plotter.camera_position = 'xy'

# Enable shadows
plotter.enable_shadows()

# control second mesh
def update_mesh(scale_factor, x_offset, y_offset, z_offset):
    mesh2_transform = pv.Transforms.scale(scale_factor)
    mesh2_transform.translate(x_offset, y_offset, z_offset)
    plotter.update_coordinates(mesh2_transform.apply(mesh2.points), mesh2)

# plotter.add_slider_widget(update_mesh, [0.1, 2.0], value=1.0, title='Scale Factor', pointa=(0.05, 0.1), pointb=(0.95, 0.1))
# plotter.add_slider_widget(update_mesh, [-10, 10], value=0, title='X Offset', pointa=(0.05, 0.2), pointb=(0.95, 0.2))
# plotter.add_slider_widget(update_mesh, [-10, 10], value=0, title='Y Offset', pointa=(0.05, 0.3), pointb=(0.95, 0.3))
# plotter.add_slider_widget(update_mesh, [-10, 10], value=0, title='Z Offset', pointa=(0.05, 0.4), pointb=(0.95, 0.4))

# Show the plotter
plotter.show()




