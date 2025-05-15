# GeneSeq

A CRISPR gRNA mapping tool that:
- Fetches gene sequences via Ensembl REST API
- Finds target sites of custom length, adjacent to custom PAMs
- Supports local sequence library
- Organizes code in modular folders (`ensembl_fetch`, `seq_scan`, `lib_access`)

## How to Use
1. Run `grna_map.py`
2. Enter a gene or load a local `.txt` sequence into the datalibrary directory.
3. Scan for targets with specified PAMs

## Folder Structure
GeneSeq/
├── datalibrary/   -> place to store gene sequences locally as `{GENE SYMBOL}_{ENSEMBL_TRANSCRIPT_ID}_seq.txt` files.
├── ensembl_fetch/ -> fetching various genetic data from ensembl
├── lib_access/    -> access to the local datalibrary
├── seq_scan/      -> scans the + and - strands for matches
├── grna_map.py    -> main function
└── README.md
