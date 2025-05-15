from ensembl_fetch import (
    fetch_gene_id_by_symbol,
    fetch_transcripts_for_gene,
    filter_protein_coding_transcripts,
    fetch_transcript_cdna_sequence,
    fetch_variants_by_gene
)

from seq_scan import find_targets
from db_access import (
    get_connection, initialize_db,
    get_transcript_sequence, insert_transcript,
    batch_insert_targets, delete_all_targets_for_transcript, check_or_create_db
)

from raw_seq_access import rawfile_checker_and_writer, find_file_and_load

def main():
    gene_symbol = input("Enter gene symbol: ").strip().upper()
    if not gene_symbol:
        print("Enter a Valid Gene symbol.")
        exit()
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

    # User-defined gRNA search parameters
    pam = input("Enter PAM pattern (e.g., NGG): ").strip().upper()
    if not pam:
        print("Enter a Valid PAM.")
        exit()
    try:
        target_len = int(input("Enter target sequence length (e.g., 20): ").strip())
        if not (0 < target_len):
            print("Invalid. Target length must be positive.")
            exit()
    except ValueError:
        print("Please enter a valid number.")
        exit()

    check_result = check_or_create_db(transcript_id, pam, target_len)
    if check_result['exists']:
        print(f"Database for Transcript {transcript_id}, PAM '{pam}', Target Length {target_len} already exists at {check_result['db_path']}")
        return
    dbpath = check_result["db_path"]
    print(f"dbpath is: {dbpath}")
    conn = get_connection(dbpath)
    initialize_db(conn)

    # loading sequence from DB
    seq = get_transcript_sequence(conn, transcript_id=transcript_id)

    """
    uncomment this if you want to load the sequence from the raw txt
    seq = find_file_and_load()
    """

    if not seq:
        seq = fetch_transcript_cdna_sequence(transcript_id)
        if not seq:
            print("Failed to fetch transcript sequence.")
            return
        insert_transcript(conn, transcript_id, gene_symbol, seq)
        print(f"Sequence fetched and stored for transcript {transcript_id}")
    else:
        print(f"Sequence loaded from DB for transcript {transcript_id}")

    print(f"Sequence length: {len(seq)}")

    rawfile_checker_and_writer(transcript_id=transcript_id, seq=seq, gene_symbol=gene_symbol)

    # Show number of overlapping variants
    #variants = fetch_variants_by_gene(gene_id)
    #print(f"Number of variants overlapping gene: {len(variants)}")

    # Proceed with target finding
    all_targets = find_targets(seq, pam_pattern=pam, target_len=target_len)

    if not all_targets:
        print("No targets found for given PAM and target length.")
        return

    print(f"Found {len(all_targets)} targets matching PAM '{pam}'.")

    # Delete old targets for this transcript (if any)
    delete_all_targets_for_transcript(conn, transcript_id)

    # Enrich and batch insert all target records
    enriched_targets = []
    for t in all_targets:
        enriched_targets.append({
            "transcript_id": transcript_id,
            "gene_symbol": gene_symbol,
            "target_seq": t["target_seq"],
            "pam_seq": t["pam_seq"],
            "strand": t["strand"],
            "target_start": t["target_start"],
            "target_end": t["target_end"],
            "pam_start": t["pam_start"],
            "pam_end": t["pam_end"],
            "target_length": len(t["target_seq"]),
            "sense": "sense" if t["strand"] == "+" else "antisense"
        })

    batch_insert_targets(conn, target_list=enriched_targets)

    print(f"Successfully inserted {len(enriched_targets)} target sites into the database.")

if __name__ == "__main__":
    main()
