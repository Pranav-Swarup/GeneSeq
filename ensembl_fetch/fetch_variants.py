from .utils import get_json

def fetch_variants_by_gene(gene_id):
    """
    Fetches known variants (e.g., SNPs) overlapping a gene.
    Useful to link mutations/disease relevance.
    """
    endpoint = f"/overlap/id/{gene_id}?feature=variation"
    return get_json(endpoint) or []

def fetch_variant_info(variant_id):
    """
    Fetch detailed info about a specific variant.
    """
    endpoint = f"/variation/human/{variant_id}"
    return get_json(endpoint)
