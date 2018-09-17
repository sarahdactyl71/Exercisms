def to_rna(dna_strand):
    string = ''
    if dna_strand == '':
        return string
    for char in dna_strand.split():
        if char == 'G':
            string += 'C'
        elif char == 'C':
            string += 'G'
        elif char == 'T':
            string += 'A'
        elif char == 'A':
            string += 'U'
    return string
