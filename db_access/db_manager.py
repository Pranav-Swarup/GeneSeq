import os
from .db_utils import get_db_filename, db_exists

def check_or_create_db(transcript_id: str, pam: str, target_len: int, db_folder='datalibrary/sqlite_dbs'):
    """
    Returns dict with keys:
      - 'exists': True if DB file exists already
      - 'db_path': full path to the DB file
    """

    db_name = get_db_filename(transcript_id, pam, target_len)
    db_path = os.path.join(db_folder, db_name)

    return {
        'exists': db_exists(db_path),
        'db_path': db_name
    }
