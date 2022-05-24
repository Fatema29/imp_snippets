# importing shutil module 
import shutil 
    
# path 
path = '/home/fjannat/Documents/EarthVision/' 
    
# Source path 
src = '/home/fjannat/Documents/EarthVision/dataset_1'
    
# Destination path 
dest = '/home/fjannat/Documents/EarthVision/dataset_2'
    
# Copy the content of 
# source to destination 
destination = shutil.copytree(src, dest) 
    
# print(destination) prints the
# path of newly created file
