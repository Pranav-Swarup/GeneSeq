from .utils import get_json

def fetch_gene_expression(gene_id):
    """
    Get gene expression data across tissues (if available).
    """
    endpoint = f"/expression/id/{gene_id}"
    return get_json(endpoint)
