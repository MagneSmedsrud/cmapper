# cmapper
cmapper is a simple pyscript to create custom colormaps for matplotlib. Simple .py script to create custom color maps for [matplotlib](https://matplotlib.org/). The .py-file can be run from shell or imported as a function to e.g. a Jupyter Notebook. 

# Get started
To "install", simply clone the files in this repo by doing the following: 
```
> https://github.com/MagneSmedsrud/cmapper.git
> cd cmapper
```

## Running cmapper from shell
Run cmapper.py with a list of color hex codes. The hex codes are separated with spaces. 

Example - Creating a cmap with black and white colors: 

`> python cmapper.py `

returns a cmap dictionary: `{'red': [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)], 'green': [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)], 'blue': [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)]}`

This must be added as a custom cmap with the following commands
```
from matplotlib.colors import LinearSegmentedColormap

cmap_dict = {
'red': [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)], 
'green': [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)], 
'blue': [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)]
}

cust_cmap = LinearSegmentedColormap(cmap_name="custom_cmap, cmap_dict)

```
## Running as a function
Import the cmapper and create a LinearSegmentedColormap object to be used as the cmap object in matplotlib.

Example: 
```
import matplotlib.pyplot as plt
import cmapper

#list of hex codes to be added to cmap
list_of_colors_hex = ["#000000","#460073","#7500c0","#a100ff","#be82ff", "dcafff", "#ffffff"]

# Create cmap project
cmap = cmapper.create_cmap(list_of_colors_hex)
```

## Example with Matplotlib
With the cmap object created, use as the `cmap` argument in matplotlib: 
```
im = ax.imshow(Z, interpolation='nearest', origin='lower', cmap=cmap)
```

# References
- [Matplotlib - LinearSegmentedColormap](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap)
