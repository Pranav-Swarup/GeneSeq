import sqlite3

def insert_transcript(conn: sqlite3.Connection, transcript_id: str, gene_symbol: str, sequence: str):
    with conn:
        conn.execute("""
            INSERT OR REPLACE INTO transcripts (transcript_id, gene_symbol, sequence)
            VALUES (?, ?, ?)
        """, (transcript_id, gene_symbol, sequence))

def get_transcript_sequence(conn: sqlite3.Connection, transcript_id: str) -> str:
    cur = conn.cursor()
    cur.execute("SELECT sequence FROM transcripts WHERE transcript_id = ?", (transcript_id,))
    row = cur.fetchone()
    return row[0] if row else None

def delete_transcript(conn: sqlite3.Connection, transcript_id: str):
    with conn:
        conn.execute("DELETE FROM transcripts WHERE transcript_id = ?", (transcript_id,))

def update_transcript_sequence(conn: sqlite3.Connection, transcript_id: str, new_sequence: str):
    with conn:
        conn.execute("""
            UPDATE transcripts
            SET sequence = ?
            WHERE transcript_id = ?
        """, (new_sequence, transcript_id))
