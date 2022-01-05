import os

from directory_list import file_list
from secrets import rs_region, rs_secret_arn, rs_cluster, rs_db
from sql_statements import *

# Using the file list along with sql statements from .py file to access the AWS Redshift Data API
# We use CLI commands to execute our sql statements with our file names as our parameters

# Defining our API call
def redshift_api_call(sql):
    
    os.system(os.system(f"aws redshift-data execute-statement --{rs_region} --secret {rs_secret_arn} --cluster-identifier {rs_cluster} --database {rs_db} --sql {sql}"))
    

# Now we loop through our directory and drop/create our tables    
for file_name in os.listdir(file_list):
    sql_statement = ''
    
    if 'City_MedianRentalPrice_5' in file_name:
        sql_statement = city_median_5br(file_name)
        redshift_api_call(sql_statement)
        
    elif 'City_MedianRentalPrice_AllHomes' in file_name:
        sql_statement = city_median_all_homes(file_name)
        redshift_api_call(sql_statement)
        
    elif 'City_MedianRentalPrice_Sfr' in file_name:
        sql_statement = city_median_sfr(file_name)
        redshift_api_call(sql_statement)
        
    elif 'City_MedianRentalPrice_Studio' in file_name:
        sql_statement = city_median_studio(file_name)
        redshift_api_call(sql_statement)
    
    elif 'City_MedianRentalPrice' in file_name:
        sql_statement = city_median_1_4br(file_name)
        redshift_api_call(sql_statement)
    
    # File is not in the original file list nor does it have a sql statment mapped to it    
    else:
        print('error: file not mapped to initial file list')
        
