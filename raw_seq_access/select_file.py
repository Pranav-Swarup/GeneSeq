import os
from .load_seq import load_seq_from_file

def list_txt_files(directory="datalibrary/rawsequences", return_count=False):
    files = [
        f for f in os.listdir(directory)
        if f.strip().lower().endswith("seq.txt")
    ]
    return (files, len(files)) if return_count else files

files, count = list_txt_files(return_count=True)

def find_file_and_load():

    if count == 0:
        print("No sequence files found in '/datalibrary'.")
        sequence = input("Enter custom Sequence: ")
        if(len(sequence) == 0):
            exit()
        return sequence

    print("Available sequence files:")
    for i, fname in enumerate(files):
        print(f"{i+1}: {fname}")

    try:
        choice = int(input("Select a file by number: ")) - 1
        if not (0 <= choice < count):
            print("Invalid selection. Index out of range.")
            exit()
    except ValueError:
        print("Please enter a valid number.")
        exit()

    filepath = f"datalibrary/rawsequences/{files[choice]}"
    sequence = load_seq_from_file(filepath)

    if not sequence:
        print("Failed to load sequence.")
        sequence = input("Enter custom Sequence: ")
        if(len(sequence) == 0):
            exit()
        return sequence

    print(f"\nLoaded sequence from {files[choice]} ({len(sequence)} bp)")

    return sequence
