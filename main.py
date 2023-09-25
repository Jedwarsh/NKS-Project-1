from brute import read_words
from brute import string_exists_in_file
import subprocess
import time
import sys
import multiprocessing

# Function to process a combination of adjective and noun
def process_combination(adj, noun):
    text = adj + noun
    print(text)
    process = subprocess.run(['python3', 'btc.py', text, '97935'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    stdout_output = process.stdout
    values = stdout_output.split(',')
    value = values[3]
    code = value[1:]
    print(code)
    if string_exists_in_file('z23-01-pk.txt', code):
        print("exists in the file.")
        with open('output.txt', 'a') as f:
            f.write(text + '\n')
    else:
        print("does not exist in the file.")

if __name__ == "__main__":
    start_time = time.time()

    # Reading the Adjectives
    adjectives = read_words("english-adjectives.txt")

    # Reading the Nouns
    nouns = read_words("english-nouns.txt")

    # Create a pool of worker processes
    pool = multiprocessing.Pool()

    # Use multiprocessing to process combinations
    for noun in nouns:
        pool.starmap(process_combination, [(adj, noun) for adj in adjectives])

    # Close the pool and wait for the worker processes to finish
    pool.close()
    pool.join()

    elapsed_time = time.time() - start_time

    print(elapsed_time)