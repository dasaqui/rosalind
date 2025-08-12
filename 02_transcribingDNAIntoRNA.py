from aux import *

def transcribe_dna_to_rna(dna_sequence):
  """
  Problem
    An RNA string is a string formed from the alphabet containing
    'A', 'C', 'G', and 'U'.

    Given a DNA string t corresponding to a coding strand, its transcribed RNA
    string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

  Given: A DNA string t having length at most 1000 nt.

  Return: The transcribed RNA string of t.
  """
  return dna_sequence.replace("T", "U")


def test():
  seq1 = "GATGGAACTTGACTACGTAAATT"
  expected = "GAUGGAACUUGACUACGUAAAUU"
  assert transcribe_dna_to_rna(seq1) == expected
  
  print("All tests passed!")


def prepare_output(rna_sequence):
  """
  Prepare the output for the RNA sequence by formatting it as required.
  """
  return rna_sequence


def main():
  test()
  processing_pipeline(
    "rosalind_rna.txt",
    transcribe_dna_to_rna,
    prepare_output
  )


if __name__ == "__main__":
  main()