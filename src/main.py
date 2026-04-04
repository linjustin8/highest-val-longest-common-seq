# main.py

import os
import shutil
import sys


def main():
    # delcare output directory and clear it if prev tests already exists
    output_directory = "./tests/output"
    shutil.rmtree(output_directory, ignore_errors=True)
    os.makedirs(output_directory, exist_ok=True)

    # declare variables to be used for algorithm
    file = sys.argv[1] # input file
    val_of_letter = {} 
    num_chars = -1 # (K): numbers of lines to read [letter -> val_of_letter]
    s1 = "" # (A): first string
    s2 = "" # (B): second string


    with(open(file, "r") as f):
        num_chars = int(f.readline().strip())
        for _ in range(num_chars):
            line = f.readline().strip().split()
            letter = line[0]
            val_of_letter[letter] = int(line[1])
        
        s1 = f.readline().strip()
        s2 = f.readline().strip()
    
    
    
    


if __name__ == "__main__":
    main()
