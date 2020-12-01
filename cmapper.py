#Imports
import argparse
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

#convert hashes to 0-1s
def convert_hex_dec(color):
    """
    converts color hex code in format #RRGGBB into three decimals between 0 and 1

    PARAMETERS
    color: string of hex color code in format #RRGGBB 

    RETURNS
    red, green, blue: Tuple with each component with values between 0 and 1
    """

    #Strip # from color hex
    color = color.strip("#")
    #print("color: {}".format(color))

    #Turn each hex calue RRGGBB into integer and divide by 255 to decimals
    red = int(color[:2], 16) /255
    green = int(color[2:4], 16) /255
    blue = int(color[4:], 16) /255
    
    return (red, green, blue)

def create_cmap_dict(colors):
    """
    Creates a dictionary for custom cmap for each color value (RGB)

    PARAMETERS
    colors: List of tuples with color values (each tuple in format (r,g,b) between 0 and 1)

    RETURNS
    cdict: Color map dictionary per color. Used for creating custom cmap.
    """

    #creating the cmap dictionary with a key per color. Each containing a list of tuples
    cdict = {
        "red": [],
        "green": [],
        "blue": []
    }

    #gets length of cmap and subtracts 1 to make list evenly distributed between 0 and 1 later
    if len(colors) == 1:
        cmap_len = len(colors)
    else: cmap_len = len(colors)-1
   
    for i,c in enumerate(colors):
        #getting location of color code (where in the range 0-1 of cmap is this color (0 is beginning, 1 is end))
        loc = i/cmap_len

        #appending color values for each color in dictionary. Double value for color intensity due to matplotlib cmap dictionary format
        r,g,b = c
        cdict["red"].append((loc,r,r))
        cdict["green"].append((loc,g,g))
        cdict["blue"].append((loc,b,b))

    return cdict

def create_cmap(list_of_colors, cmap_name="Cust_Cmap"):
    """
    Creates custom matplotlib cmap based on a list of hex color codes

    PARAMETERS
    cmap_name: name of custom cmap
    list_of_colors: list of hex color codes in format #RRGGBB

    RETURNS
    cust_cmap: Matplotlib colormap object
    
    """

    color_list_tuples = [convert_hex_dec(x) for x in list_of_colors]
    cmap_dict = create_cmap_dict(color_list_tuples)
    cust_cmap = LinearSegmentedColormap(cmap_name, cmap_dict)

    return cust_cmap

#Parse Arguments
def arg_parser():
    #setting up argument parser
    parser = argparse.ArgumentParser(description='Create custom cmap from list of color hexes')
    
    #create arguments
    parser.add_argument("color_list", nargs="+", help="list of color hex values")
    parser.add_argument("--cmap_name", type=str, nargs='?', default="cust_cmap", help="name of cmap")

    #parse arguments to be returned
    args = parser.parse_args()
    
    return args

#main function
def main():
    
    args = arg_parser()
    
    cust_cmap = create_cmap(args.color_list, args.cmap_name)
    
    #Print cmap dictionary for copy-paste if invoked from command line
    print(cust_cmap._segmentdata)

if __name__ == "__main__":
    main()