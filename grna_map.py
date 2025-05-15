from ensembl_fetch import (
    fetch_gene_id_by_symbol,
    fetch_transcripts_for_gene,
    filter_protein_coding_transcripts,
    fetch_transcript_cdna_sequence,
    fetch_variants_by_gene
)

from seq_scan import find_targets
from lib_access import find_file_and_load, write_to_file

def main():

    gene_symbol = input("Enter gene symbol: ").strip().upper()
    gene_id = fetch_gene_id_by_symbol(gene_symbol)
    if not gene_id:
        print("Gene not found.")
        return

    transcripts = fetch_transcripts_for_gene(gene_id)
    protein_coding = filter_protein_coding_transcripts(transcripts)

    print(f"Found {len(protein_coding)} protein-coding transcripts.")

    if not protein_coding:
        return

    transcript_id = protein_coding[0]["id"]
    seq = fetch_transcript_cdna_sequence(transcript_id)

    if seq:
        print(f"Sequence length: {len(seq)}")
        write_to_file(transcript_id, seq, gene_symbol)
    else:
        print("Failed to fetch sequence.")

    variants = fetch_variants_by_gene(gene_id)
    print(f"Number of variants overlapping gene: {len(variants)}")

    find_file_and_load()

    pam = input("Enter PAM pattern (e.g., NGG): ").strip().upper()
    target_len = int(input("Enter target sequence length (e.g., 20): ").strip())

    all_targets = find_targets(seq, pam_pattern=pam, target_len=target_len)
    print(f"Found {len(all_targets)} targets matching PAM '{pam}' on both strands.")

    for t in all_targets:
        print(t)

if __name__ == "__main__":
    main()
