import os
import re
import shutil

"""Renaming of zReports

This script bulk renames Z-reports according to the organisational standard

This file can also be imported as a module and contains the following
functions:

    * autoRename - Takes a dir and creates another dir with renamed files
"""
month_dict = {"Jan": "01",
              "Feb": "02",
              "Mar": "03",
              "Apr": "04",
              "May": "05",
              "Jun": "06",
              "Jul": "07",
              "Aug": "08",
              "Sep": "09",
              "Oct": "10",
              "Nov": "11",
              "Dec": "12"}


def autoRename(directory):
    """Renames all Z-reports according to the convention used
        """

    try:
        folder = os.listdir(directory)
    except FileNotFoundError:
        os.mkdir(directory)
        print("Mappen fanns inte men den skapades")
        return
    try:
        os.mkdir(os.path.join(directory, "renamed"))
    except OSError:
        print("Outputmappen finns redan")

    new_dir = os.path.join(directory, "renamed")

    for filename in folder:
        if filename[0] == '.':
            continue
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            # Ta bort mappen från ad
            name = f
            # Regexes för att extrahera information
            month = month_dict[re.findall(r'__\D{3}_', name)[0][2:-1]]
            ident = re.findall(r'__\d+_', name)[0][2:-1]
            date = re.findall(r'_\d+__\d{4}', name)[0][1:-6].rjust(2, '0')
            year = re.findall(r'\d{4}', name)[0]
            # Klistra ihop
            new_name = f'{year}-{month}-{date}#{ident}.pdf'
            new_dist = os.path.join(new_dir, new_name)
            shutil.copy(f, new_dist)
    print(f'Du hittar nu filerna med nytt namn här: {new_dir}')


if __name__ == '__main__':
    # Takes relative path
    autoRename(input("Ange vilken mapp filerna ligger i: "))
