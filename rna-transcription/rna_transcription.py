def to_rna(dna_strand):
    rna_strand = dna_strand.replace('G', 'C').replace('C', 'G').replace('T', 'A').replace('A', 'U')
    return rna_strand
