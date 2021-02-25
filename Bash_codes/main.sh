set file
awk ' BEGIN {IGNORECASE = 1} { sub(/unix/,"Unix OS"); print } ' file 