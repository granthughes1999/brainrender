# brainrender
using cellfinder output files to render 3D models of fluorescently labeled cells 

# Create Conda env 
#### This will create an env where you can render 3D models of you labled cells
##### open an Anaconda prompt
##### >> conda create --brainrender myenv
##### >> conda activate brainrender 
##### >> pip install brainrender

# Changes to make to brainrender.py file before running
## 1. Change Path to cellfinder_output points.npy file
##### line 21 cells_path = r"C:\Users\denma\Desktop\Grant\cellfinder\cellfinder_output\points\points.npy"

## 2. change the path to where your locally stored allen mouse atlas
##### line 25 allen_mouse_50um = r'C:\Users\denma\.brainglobe\allen_mouse_50um_v1.2'

# Run updated brainrender.py file
##### >> conda activate brainrender 
##### >> python /path/to/your/brainrender.py

