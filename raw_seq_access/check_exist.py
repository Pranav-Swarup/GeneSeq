import os

from .write_file import write_to_file

raw_dir = "datalibrary\\rawsequences"
os.makedirs(raw_dir, exist_ok=True)

def rawfile_checker_and_writer(transcript_id,seq, gene_symbol):

    raw_file_path = os.path.join(raw_dir, f"{gene_symbol}_{transcript_id}_seq.txt")

    if not os.path.exists(raw_file_path):
        write_to_file(transcript_id, seq, gene_symbol, out_dir=raw_dir)
        print(f"Raw sequence saved to {raw_file_path}")
    else:
        print(f"Raw sequence exists at {raw_file_path}")