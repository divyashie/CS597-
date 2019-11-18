import sys 
import os 
import glob 
import shutil
import datetime as dt 
import calendar

def format_file(file_name):
       split_file_data = file_name.split("_") 
       i = split_file_data[1] #messy string 
       date = '-'.join([i[:4], i[4:6], i[6:8]])
       time = ':'.join([i[8:10], i[10:12], i[12:14]])
       result = date + " " + time 
       return result

def organize_calendar(result): 
    timestamp = dt.datetime.strptime(result, "%Y-%m-%d %H:%M:%S")
    get_month = calendar.month_name[timestamp.month] #month of the string
    return get_month

def create_subdirectory(): 
    directory = "/home/wincom/2019/2019_h5"
    files = os.listdir(directory)
    #file_path = new_dir + "/"
    for f in files:
        if f.endswith(".h5"): 
              existing_dir = directory + "/" + f 
              get_month = organize_calendar(format_file(f))
              file_path = directory + "/" + str(get_month) + "/" + f 
              os.makedirs(file_path)
              shutil.move(existing_dir, file_path)

def main(): 
    create_subdirectory()

if __name__ == "__main__":
    main()        
