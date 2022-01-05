# Script used to generate the list of .csv files to be imported into s3.
# Other parts of the process check to see if a file name is in this list
# before acting upon file in question.
# This script is only run once after confirming the correct files are in our directory

import os
from secrets import local_data_directory

file_list = []

for file in os.listdir(local_data_directory):
    if '.csv' in file:
        file_list.append(file)
        
