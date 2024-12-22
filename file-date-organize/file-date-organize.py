import sys
import os
import datetime

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} <directory>')
    
    folder = sys.argv[1]
    for file in os.listdir(folder):
        # only consider files, not directories
        if not os.path.isfile(os.path.join(folder, file)):
            continue
        
        # find the timestamp (last modified time) of the file
        timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(folder, file)))
        yearmonth = timestamp.strftime("%Y%m")

        # create the yearmonth directory if not already existent
        if not os.path.exists(os.path.join(folder, yearmonth)):
            os.mkdir(os.path.join(folder, yearmonth))
            print(f'folder {yearmonth} created')
        
        # move the file to the yearmonth directory
        os.rename(os.path.join(folder, file), os.path.join(folder, yearmonth, file))
        print(f'{file} moved to {yearmonth}')
        
