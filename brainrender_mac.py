from brainrender.scene import Scene
from brainrender.actors import Points
from bg_atlasapi.bg_atlas import BrainGlobeAtlas
from brainrender import settings
from brainrender.actors import Cylinder
import bg_space as bg
import numpy as np
from rich import print
from myterial import orange
from pathlib import Path

bg_atlas.structures

# >>> UPDATE THESE TWO PATHS
# 1. path to cellfinder output folder
cellfinder_output_path = "/Users/grant/Desktop/mock_df/cellfinder_output/"
# 2. path to local location of allen mouse brain atlas
allen_mouse_10um = '/Users/grant/brainglobe/allen_mouse_10um'

# Path to cellfinder_output points.npy file
cells_path = cellfinder_output_path + 'points/points.npy'
print(cells_path)

# unknown from cylinder example file on github
settings.SHOW_AXES = False
settings.WHOLE_SCREEN = False

print(f"[{orange}]Running example: {Path(__file__).name}")

# atlas version you want to use
atlas = BrainGlobeAtlas('allen_mouse_50um', check_latest=False)

# intialise brainrender scene
scene = Scene(atlas_name='allen_mouse_50um', title="G20_test")
print(scene.atlas.space)
# You can specify color, transparency... of brain regions
VISp = scene.add_brain_region("VISp", alpha=0.2, color="green")
VISl = scene.add_brain_region('VISl',  alpha=0.2, color="red")
LGd = scene.add_brain_region('LGd', alpha=0.2, color="blue")
LP = scene.add_brain_region('LP', alpha=0.2, color="yellow")

# Add lables to brain regions'
scene.add_label(VISp, "Primary Visual area")
scene.add_label(VISl, "Lateral Visual area")
scene.add_label(LGd, "Lateral Geniculate Nucleus of the Thalmus")
scene.add_label(LP, "Lateral Posterior Thalmus")

# create and add a cylinder actor
actor_electrode = Cylinder(
    VISp,  # center the cylinder at the center of mass of Primary Visual area, by using its varaible name
    scene.root,  # the cylinder actor needs information about the root mesh
)

# NOT sure what this does, from brainrender documentation...
# BGSpace AnatomicalSpace Objects
# origin: ('Superior', 'Posterior', 'Lateral')
# sections: ('Frontal plane')
# shape: (528, 320, 456)


# create points actor
cells = Points(cells_path)

# Add cells Actor to Scence
scene.add(cells, actor_electrode)

# print the content of the scence
scene.content

# Render the 3D brain Scence
scene.render()
