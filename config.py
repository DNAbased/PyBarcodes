# choose the length of the barcodes
length = 6
# remove barcodes containing repeats of more than three nucleotides?
repeats = 1
# only keep barcodes containing each nucleotide at least once?
each_nt = 1
# set a lower and an upper limit to GC content
gc_lower = 40
gc_upper = 60
# remove barcodes containing blacklisted sequences (otherwise set to <None>)
blacklist = 'blacklist.tsv'
# set a minimum levenshtein distance for barcodes
levenshtein = 3
# set an output mode [tsv, json]
output_mode = 'tsv'
# set a prefix for the output
output_prefix = 'my_barcodes'