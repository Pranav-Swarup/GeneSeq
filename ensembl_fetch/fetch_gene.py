from .utils import get_json

def fetch_gene_id_by_symbol(gene_symbol, species="homo_sapiens"):
    """
    Returns Ensembl gene ID for a gene symbol.
    e.g. TP53 -> ENSG00000141510
    """
    endpoint = f"/lookup/symbol/{species}/{gene_symbol}"
    data = get_json(endpoint)
    if data and "id" in data:
        return data["id"]
    return None

def fetch_gene_info(gene_id):
    """
    Returns full gene info JSON for given gene_id.
    """
    endpoint = f"/lookup/id/{gene_id}"
    return get_json(endpoint)
