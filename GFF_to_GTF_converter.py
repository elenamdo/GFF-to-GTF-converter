import os
import re
from pathlib import Path

pathname = input("Enter GFF file location: ")
filename = Path(pathname)
new_filename = filename.stem + ".gtf"
with open(os.path.join(pathname), "r") as fh:
    new_file = open(str(new_filename), 'a+')
    for line in fh:
        if line.startswith("NC"):
            p = re.compile('.+GeneID:([0-9]+)')
            id = p.search(line)
            if id is not None:
                gene_id = id.group(1)
                attribute = re.search('ID=.+', line)
                new_line = line.replace((attribute.group()),('gene_id "'+ (str(gene_id)) + '"; ' + 'transcript_id "' + str(gene_id)+ '"; '), 1)
                seq_id, ev_else = line.split('\t',1)
                if seq_id == "NC_007416.3":
                    newest_line = new_line.replace("NC_007416.3", "chrX", 1)
                if seq_id == "NC_007417.3":
                    newest_line = new_line.replace("NC_007417.3", "chr2", 1)
                if seq_id == "NC_007418.3":
                    newest_line = new_line.replace("NC_007418.3", "chr3", 1)
                if seq_id == "NC_007419.2":
                    newest_line = new_line.replace("NC_007419.2", "chr4", 1)
                if seq_id == "NC_007420.3":
                    newest_line = new_line.replace("NC_007420.3", "chr5", 1)
                if seq_id == "NC_007421.3":
                    newest_line = new_line.replace("NC_007421.3", "chr6", 1)
                if seq_id == "NC_007422.5":
                    newest_line = new_line.replace("NC_007422.3", "chr7", 1)
                if seq_id == "NC_007423.3":
                    newest_line = new_line.replace("NC_007423.3", "chr8", 1)
                if seq_id == "NC_007424.3":
                    newest_line = new_line.replace("NC_007424.3", "chr9", 1)
                if seq_id == "NC_007425.3":
                    newest_line = new_line.replace("NC_007425.3", "chr10", 1)
                new_file.write(str(newest_line))
            if id is None:
                failures = open('failures.txt', 'a+')
                failures.write(str(line))
                failures.close()
new_file.close()
