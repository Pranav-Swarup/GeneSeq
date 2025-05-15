from .utils import get_json

def fetch_transcripts_for_gene(gene_id, species="homo_sapiens"):
    """
    Returns list of transcript objects for the gene with transcripts expanded.
    """
    endpoint = f"/lookup/id/{gene_id}?expand=1"
    data = get_json(endpoint)
    if data and "Transcript" in data:
        return data["Transcript"]
    return []

def filter_protein_coding_transcripts(transcripts):
    """Filter list to keep only protein-coding transcripts."""
    return [t for t in transcripts if t.get("biotype") == "protein_coding"]

def fetch_transcript_info(transcript_id):
    """Fetch info for a single transcript by ID."""
    endpoint = f"/lookup/id/{transcript_id}"
    return get_json(endpoint)
