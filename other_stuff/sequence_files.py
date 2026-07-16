from Bio import SeqIO

#_______________Opening .fasta or .fa file _____________
records = SeqIO.parse("sequences.fasta", "fasta")
# "sequences.fasta" in this case is the path to fasta file
for record in records:
    print(record.id) # find name of each entry
    print(str(record.seq)) # find sequence

# ___________________Opeing fastq file __________
records1 = SeqIO.parse("sequences.fastq", "fastq")
# "sequences.fasta" in this case is the path to fasta file
for record in records1:
    print(record.id) # find name of each entry
    print(str(record.seq))
    print(record.letter_annotations["phred_quality"]) # quality scores as list

# Using biopython assembling the fastq back from list of sequences, list of names and list
# of phred score lists

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def create_fastq(sequences, phred_scores, names):
    records = []
    for sequence1, phred_score, name in zip(sequences, phred_scores, names):
        # Create a Seq object
        seq_obj = Seq(sequence1)

        # Create a SeqRecord object
        record1 = SeqRecord(
            seq_obj,
            id=name,
            description=""
        )

        # Assign the Phred scores to the letter_annotations
        record1.letter_annotations["phred_quality"] = phred_score
        records.append(record1)
    return records

# ___________________Opening the .ab1 file ___________________
# Quick way to open ab1 file
record = SeqIO.read("Example.ab1", "abi")
print(record.id)
print(str(record.seq))
# Longer way to open the ab1 file

record = SeqIO.read("Example.ab1", "abi")

# get the dye order
dye_order = record.annotations['abif_raw']["FWO_1"].decode("ascii")
# get the traces for each base
traces = {
            'A': record.annotations['abif_raw']['DATA9'],
            'C': record.annotations['abif_raw']['DATA10'],
            'G': record.annotations['abif_raw']['DATA11'],
            'T': record.annotations['abif_raw']['DATA12']
        }
base_calls = str(record.seq)
# or alternatively
base_calls2 = str(record['abif_raw']['PBAS1'])
# where the peaks are in trace
peak_positions = record.annotations['abif_raw']['PLOC1']
