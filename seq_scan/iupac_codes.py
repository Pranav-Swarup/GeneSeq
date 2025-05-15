
IUPAC_CODES = {
    'A': {'A'}, 'C': {'C'}, 'G': {'G'}, 'T': {'T'},
    'R': {'A', 'G'}, 'Y': {'C', 'T'}, 'S': {'G', 'C'},
    'W': {'A', 'T'}, 'K': {'G', 'T'}, 'M': {'A', 'C'},
    'B': {'C', 'G', 'T'}, 'D': {'A', 'G', 'T'},
    'H': {'A', 'C', 'T'}, 'V': {'A', 'C', 'G'},
    'N': {'A', 'C', 'G', 'T'}
}

def matches_iupac(seq_segment: str, pattern: str) -> bool:
    """Check if seq_segment matches pattern allowing IUPAC codes."""
    if len(seq_segment) != len(pattern):
        return False
    seq_segment = seq_segment.upper()
    pattern = pattern.upper()
    for base, pat_base in zip(seq_segment, pattern):
        if base not in IUPAC_CODES.get(pat_base, {pat_base}):
            return False
    return True