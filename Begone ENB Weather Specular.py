import fileinput
import os
import sys
import re

def main():  
    path = r"E:\SteamLibrary\steamapps\common\Skyrim Special Edition\enbseries\W"
    file_list = os.listdir(path)
    full_file_paths = [os.path.join(path, file_name) for file_name in file_list]

    for line in fileinput.input(files=full_file_paths, inplace=True, encoding="utf-8"):
        if "SpecularAmountMultiplier" in line:
            line = re.sub(r"\d+\.\d", "1.0", line)
        sys.stdout.write(line)
        
if __name__ == "__main__":
    main()