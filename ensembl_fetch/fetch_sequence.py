from .utils import get_text

def fetch_transcript_cdna_sequence(transcript_id):
    """
    Returns cDNA sequence (spliced transcript sequence) for a transcript ID.
    """
    endpoint = f"/sequence/id/{transcript_id}?type=cdna"
    seq = get_text(endpoint)
    if seq:
        return seq.strip().upper()
    return None

def fetch_protein_sequence(protein_id):
    """Fetch protein sequence by protein ID."""
    endpoint = f"/sequence/id/{protein_id}?type=protein"
    seq = get_text(endpoint)
    if seq:
        return seq.strip().upper()
    return None

def fetch_exon_sequence(exon_id):
    """Fetch exon sequence by exon ID."""
    endpoint = f"/sequence/id/{exon_id}?type=exon"
    seq = get_text(endpoint)
    if seq:
        return seq.strip().upper()
    return None
