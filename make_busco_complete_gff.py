import os
import sys

# full_table_tsv_in = '/work2/yuka97524/Temma/19omniC/redbean_polca3_ph/05busco/busco_long_output2/run_arthropoda_odb10/full_table.tsv'
# gff_dir_path = '/work2/yuka97524/Temma/19omniC/redbean_polca3_ph/05busco/busco_long_output2/run_arthropoda_odb10/augustus_output/gff'

full_table_tsv_in = sys.argv[1]
gff_dir_path = sys.argv[2]

complete_gff_file_name_all = list()

with open(full_table_tsv_in, 'r') as full_table_tsv_in:
    for full_table_tsv_in_line in full_table_tsv_in:
        if full_table_tsv_in_line[0] == '#':
            continue
        full_table_tsv_in_line = full_table_tsv_in_line.split('\t')
        if full_table_tsv_in_line[1] == 'Complete':
            complete_gff_file_name_all.append(full_table_tsv_in_line[0])

for complete_gff_file_name in complete_gff_file_name_all:
    with open(gff_dir_path + '/' + complete_gff_file_name + '.gff', 'r') as f:
        for line in f:
            line_list = line.split('\t')
            if line_list[2] == 'gene':
                print('\t'.join([str(i) for i in line_list[0:8]]) + '\t' + 'ID=' + complete_gff_file_name)
                print(line_list[0] + '\t' + line_list[1] + '\t' + 'mRNA' + '\t' + '\t'.join([str(i) for i in line_list[3:8]]) + '\t' + 'ID=' + complete_gff_file_name + ';Parent=' + complete_gff_file_name)
            elif line_list[2] == 'CDS':
                print('\t'.join([str(i) for i in line_list[0:8]]) + '\t' + 'ID=cds.' + complete_gff_file_name + ';Parent=' + complete_gff_file_name)
            elif line_list[2] == 'exon':
                print('\t'.join([str(i) for i in line_list[0:8]]) + '\t' + 'ID=exon.' + complete_gff_file_name + ';Parent=' + complete_gff_file_name)
            elif line_list[2] == 'start_codon':
                print('\t'.join([str(i) for i in line_list[0:8]]) + '\t' + 'ID=start_codon.' + complete_gff_file_name + ';Parent=' + complete_gff_file_name)
            elif line_list[2] == 'stop_codon':
                print('\t'.join([str(i) for i in line_list[0:8]]) + '\t' + 'ID=stop_codon.' + complete_gff_file_name + ';Parent=' + complete_gff_file_name)
