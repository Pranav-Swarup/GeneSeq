import os
import sqlite3
from sqlite3 import Connection

DB_FOLDER = "./datalibrary/sqlite_dbs"

def get_connection(db_filename: str) -> Connection:
    """Connects to the specified DB file inside /databases directory."""
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)
    db_path = os.path.join(DB_FOLDER, db_filename)
    print(db_path)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Enable dict-like rows
    return conn

def initialize_db(conn: Connection):
    """Initializes tables in the connected DB if not already present."""
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transcripts (
            transcript_id TEXT PRIMARY KEY,
            gene_symbol TEXT,
            sequence TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS targets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transcript_id TEXT,
            gene_symbol TEXT,
            target_seq TEXT,
            pam_seq TEXT,
            strand TEXT,
            target_start INTEGER,
            target_end INTEGER,
            pam_start INTEGER,
            pam_end INTEGER,
            target_length INTEGER,
            sense BOOLEAN,
            FOREIGN KEY (transcript_id) REFERENCES transcripts(transcript_id)
        )
    """)

    conn.commit()
