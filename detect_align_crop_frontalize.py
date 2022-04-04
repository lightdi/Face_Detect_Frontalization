import os
import argparse
from Crop_Align import Crop_Align

parser = argparse.ArgumentParser(description='Crop and align file on a list of folder')
parser.add_argument('--in_folder', type=str, default='data', help="folder to get images to be cropped and aligned")
parser.add_argument('--skip_files', type=bool, default=False ,  help="skip processed files (create a list of processed files)")
parser.add_argument('--out_folder', type=str, default='processed', help="folder to save cropped and aligned images")
parser.add_argument('--method', type=str, default='ssd', help="Method to cropped and aligned images")
    

args = parser.parse_args()


def main(args):

    in_folder = args.in_folder
    skip_files = args.skip_files
    out_folder = args.out_folder   
    method = args.method
    
    crop_align = Crop_Align()
    # Create folder if not exists
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    
    # Create list of processed files
    files_to_skip = []
    if skip_files:
        if os.path.exists(out_folder+"/processed_files.txt"):
            with open(out_folder+"/processed_files.txt") as f:
                files_to_skip = f.read().splitlines()
        
        
    # Loop over files
    for file in os.listdir(in_folder):
        if file in files_to_skip:
            continue
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".bmp"):
            print(in_folder + "/" + file)
            try:
                crop_align.crop(in_folder + "/" + file, out_folder + "/" + file)
            except Exception  as e :
                print ("Error processing file: " + file)
                print (str(e))
        
            with open(out_folder+"/processed_files.txt", 'a+') as f:
                f.write(file+ '\n')
        
        # Crop and align
        # crop_and_align(in_folder + file, out_folder + file)


if __name__ == '__main__':
   main( args)
   