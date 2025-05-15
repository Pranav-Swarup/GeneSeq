# GeneSeq

***A CRISPR gRNA mapping tool that:***

- **Gene & Transcript Retrieval via Ensembl**
  - Fetches gene metadata, transcript lists, and cDNA sequences using the Ensembl REST API.

- **Customizable PAM Pattern & Target Length**
  - Supports user-defined PAM sequences (e.g., `NGG`, `NNGRRT`) and target site lengths (e.g., 15–25 bp).

- **Strand-Aware Target Detection**
  - Scans both sense and antisense strands for target sites matching criteria.

- **Raw Sequence Caching**
  - Stores fetched sequences as `.txt` files in `/datalibrary/rawsequences` to avoid repeated API calls.

- **Variant Overlap Reporting**
  - Displays the number of variants overlapping the selected gene from Ensembl variation data.

- **Auto-Named SQLite Target Databases**
  - Stores results in uniquely named `.db` files based on transcript ID, PAM, and target length.

- **Smart Database Reuse**
  - Checks if the same parameter combination has already been processed — skips redundant computation.

## How to Use
1. Run `grna_map.py`
2. Enter a gene, The PAM sequence and the target length desired.  
3. If the combination of parameters specified above already has a database, access it from datalibrary/sqlite_dbs
4. If not, a new DB will be created as `db_{ENSEMBL_TRANSCRIPT_ID}_{PAM}_{TARGET_LEN}_.db` after scanning for matches.  


## Folder Structure
GeneSeq/  
|--- datalibrary/   
|------|--- rawsequences  
|------|--- sqlite_dbs  
|--- db_access/  
|--- ensembl_fetch/  
|--- raw_seq_access/  
|--- seq_scan/  
|--- grna_map.py  
|--- README.md  

## Folder and File Purposes
rawsequences -> repository with gene sequences locally as `{GENE SYMBOL}_{ENSEMBL_TRANSCRIPT_ID}_seq.txt` files.  
sqlite_dbs -> unique sqlite dbs for each variation of params - `db_{ENSEMBL_TRANSCRIPT_ID}_{PAM}_{TARGET_LEN}_.db`  
db_access -> to check if a db exists, if not - functions to create and access it.  
ensembl_fetch -> fetching various genetic data from ensembl  
raw_seq_access -> functions to directly access to the local datalibrary/rawsequences bypassing the DB.  
seq_scan -> scans the gene sequence for matches based on GENE, PAM and TARGET LENGTH.  
grna_map -> main function  
