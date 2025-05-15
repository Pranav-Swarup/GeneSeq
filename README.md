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
|------|--- rawsequences        1  
|------|--- sqlite_dbs          2  
|--- db_access/                 3  
|--- ensembl_fetch/             4  
|--- raw_seq_access/            5  
|--- seq_scan/                  6  
|--- grna_map.py                7  
|--- README.md  

## Folder and File Purposes
-> repository with gene sequences locally as `{GENE SYMBOL}_{ENSEMBL_TRANSCRIPT_ID}_seq.txt` files.  
-> unique sqlite dbs for each variation of params - `db_{ENSEMBL_TRANSCRIPT_ID}_{PAM}_{TARGET_LEN}_.db`  
-> to check if a db exists, if not - functions to create and access it.  
-> fetching various genetic data from ensembl  
-> functions to directly access to the local datalibrary/rawsequences bypassing the DB.  
-> scans the gene sequence for matches based on GENE, PAM and TARGET LENGTH.  
-> main function  
