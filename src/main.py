# main.py

import os
import shutil
import sys
import time

from max_val_subsequence import max_val


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

    # read input file and populate variables
    with(open(file, "r") as f):
        num_chars = int(f.readline().strip())
        for _ in range(num_chars):
            line = f.readline().strip().split()
            letter = line[0]
            val_of_letter[letter] = int(line[1])
        
        s1 = f.readline().strip()
        s2 = f.readline().strip()
    
    # excute and calculate time taken
    start_time = time.time()
    
    res, sequence = max_val(s1, s2, val_of_letter)
    
    end_time = time.time()
    print(f"Result: {res}")
    print(f"Sequence: {sequence}") 
    print(f"Time taken: {end_time - start_time} seconds")
    
    # create output file and write result to it
    input_name = os.path.basename(file)
    output_name = f"{os.path.splitext(input_name)[0]}.out"
    output_file = os.path.join(output_directory, output_name)
    with open(output_file, "w") as f:
        f.write(str(res))
        f.write("\n")
        f.write(sequence)
        

if __name__ == "__main__":
    main()
