from datetime import datetime
from os import scandir

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def get_files():
    dir_entries = scandir("C:\\Users\\User\\Desktop")
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            print("%s\n" % f'{entry.name} \n Last Modified: {convert_date(info.st_mtime)}')
            #print(f"{entry.name}" + "%10s" % f" Last Modified: " + "%10s" % f"{convert_date(info.st_mtime)}")
            #print(f'{entry.name}\t\t Last Modified: {convert_date(info.st_mtime)}')
print(get_files())


