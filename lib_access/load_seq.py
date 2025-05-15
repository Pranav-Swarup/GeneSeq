def load_seq_from_file(filepath):
    try:
        with open(filepath, "r") as f:
            return f.read().strip()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
