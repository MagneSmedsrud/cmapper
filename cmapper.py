#Imports
import argparse

# import matplot lib + colors


#convert hashes to 0-1s


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
    for a in args.color_list:
        print(type(int(a)))


if __name__ == "__main__":
    main()