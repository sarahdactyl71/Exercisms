transcription = {'G': 'C',
              'C': 'G',
              'T': 'A',
              'A': 'U'}


def to_rna(dna):
    return ''.join(transcription[key] for key in dna)
