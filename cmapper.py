#Imports
import argparse

# import matplot lib + colors


#convert hashes to 0-1s
def convert_hex_dec(color):
    """
    converts color hex code in format #RRGGBB into three decimals between 0 and 1

    PARAMETERS
    color: string of hex color code in format #RRGGBB 

    RETURNS
    red, green, blue: Each component with values between 0 and 1
    """

    #Strip # from color hex
    color = color.strip("#")

    #Turn each hex calue RRGGBB into integer and divide by 256 to decimals
    red = int(color[:2], 16) /256
    green = int(color[2:4], 16) /256
    blue = int(color[4:], 16) /256

    return red, green, blue

#def create cmap
#list of hashes
# len list = something about number of entries

#later: discrete list (not continuous) - input from 


#Parse Arguments
def arg_parser():
    #setting up argument parser
    parser = argparse.ArgumentParser(description='Create custom cmap from list of color hexes')
    
    #create arguments
    parser.add_argument("color_list", nargs="+", help="list of color hex values")

    #parse arguments to be returned
    args = parser.parse_args()
    
    return args


#main function
def main():
    args = arg_parser()
    
    #running tests
    convert_hex_dec("#a5a8b6")

if __name__ == "__main__":
    main()