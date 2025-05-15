import os
import re

def get_db_filename(transcript_id: str, pam: str, target_len: int) -> str:
    # Clean PAM to be filesystem safe
    pam_clean = re.sub(r'[^A-Za-z0-9]+', '_', pam)
    filename = f"db_{transcript_id}_{pam_clean}_{target_len}.db"
    return filename

def db_exists(db_path: str) -> bool:
    return os.path.isfile(db_path)