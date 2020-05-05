# PyBarcodes

This Python tool can be used to generate barcodes used in custom NGS approaches such as targeted sequencing or massively-parallel reporter assays.

## Installation

Download or clone this repository.

## Dependencies

polyleven >= 0.3

Also see the requirements.txt file.

## Usage

Besides the length of the barcodes, you can control the removal of barcodes containing homotrinucleotides or barcodes containing blacklisted sequences. You can choose to only keep barcodes containing each base at least once, and control the GC content of the generated barcodes as well as the maximum allowed levenshtein edit distance. All options are chosen in the config file (e.g., config.py). 

Call the script using 'python3 main.py config.py'.
Run time of the barcode generation is mainly dependent on the length of the barcodes and the chosen edit distance.

The following sets of barcodes are already provided in json format:

| Length [nt] | Number of barcodes |
| --- | --- |
| 6 | 36 |
| 7 | 127 |
| 8 | 351 |
| 9 | 1,215 |
| 10 | 4,217 |
| 11 | 10,807 |
| 12 | 38,718 |
| 13 | 99,853 |
| 14 | 370,911 |
| 15 | 954,072 |

The following criteria were applied to obtain these barcodes:

- Removed barcodes with repeats of more than two identical nucleotides
- Removed barcodes without at least one of each nucleotide
- Lower GC threshold: 40 %
- Upper GC threshold: 60 %
- Removed barcodes containing ACA/CAC/GTG/TGT
- Minimum levenshtein distance between barcodes of 3

For further information regarding the ACA (etc.) trinucleotides, see
> Fumitaka Inoue, Martin Kircher, Beth Martin, Gregory M Cooper, Daniela M Witten, Michael T McManus, Nadav Ahituv, Jay Shendure, A systematic comparison reveals substantial differences in chromosomal versus episomal encoding of enhancer activity, _Genome Res_, Volume 27, Issue 1, Pages 38-52, https://doi.org/10.1101/gr.212092.116

> Matthias Meyer, Martin Kircher, Illumina Sequencing Library Preparation for Highly Multiplexed Target Capture and Sequencing, _Cold Spring Harb Protoc_, https://doi.org/10.1101/pdb.prot5448

## Config

Detailed description of the parameters set in the config file:

| Parameter | Description | Value |
| --- | --- | --- |
| length | Determines the length of the created barcodes | Integer |
| repeats | Remove barcodes containing repeats of three or more nucleotides | 1: yes; 0: no |
| each_nt | Only keep barcodes containing each nucleotide at least once | 1: yes; 0: no |
| gc_lower | Lower threshold for GC-content (%) | Integer |
| gc_upper | Upper threshold for GC-content (%) | Integer |
| blacklist | Remove barcodes containing blacklisted sequences | String (path to file) or None |
| levenshtein | Set minimum levenshtein distance for barcodes | Integer |
| output_mode | File type of output | 'tsv' or 'json' |
| output_prefix | File name of output | String |
