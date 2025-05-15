import sqlite3

def delete_all_targets_for_transcript(conn: sqlite3.Connection, transcript_id: str):
    with conn:
        conn.execute("DELETE FROM targets WHERE transcript_id = ?", (transcript_id,))
        conn.execute("DELETE FROM sqlite_sequence WHERE name='targets'")

def count_targets_for_transcript(conn: sqlite3.Connection, transcript_id: str) -> int:
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM targets WHERE transcript_id = ?", (transcript_id,))
    return cur.fetchone()[0]

def batch_insert_targets(conn: sqlite3.Connection, target_list: list):
    """
    Insert a batch of target sites into the 'targets' table.
    Each entry in target_list should be a dictionary with:
    {
        'transcript_id', 'gene_symbol', 'target_seq', 'pam_seq', 'strand',
        'target_start', 'target_end', 'pam_start', 'pam_end',
        'target_length', 'sense'
    }
    """
    if not target_list:
        return

    with conn:
        conn.executemany("""
            INSERT INTO targets (
                transcript_id, gene_symbol,
                target_seq, pam_seq, strand,
                target_start, target_end,
                pam_start, pam_end,
                target_length, sense
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [
            (
                t["transcript_id"],
                t["gene_symbol"],
                t["target_seq"],
                t["pam_seq"],
                t["strand"],
                t["target_start"],
                t["target_end"],
                t["pam_start"],
                t["pam_end"],
                t["target_length"],
                t["sense"]
            ) for t in target_list
        ])
