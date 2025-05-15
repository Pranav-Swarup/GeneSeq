def write_to_file(transcript_id, seq, genesymbol):

    with open(f"datalibrary/{genesymbol}_{transcript_id}_seq.txt", "w") as f:
        f.write(seq)
    print(f"Saved sequence to {genesymbol}_{transcript_id}_seq.txt")
