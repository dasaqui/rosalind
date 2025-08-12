from aux import *

def complementing_a_strand_of_dna(dna_sequence):
  """
  Problem
    In DNA strings, symbols 'A' and 'T' are complements of each other, as are
    'C' and 'G'.

    The reverse complement of a DNA string s is the string sc formed by
    reversing the symbols of s, then taking the complement of each symbol
    (e.g., the reverse complement of "GTCA" is "TGAC").

  Given: A DNA string s of length at most 1000 bp.

  Return: The reverse complement sc of s.
  """

  sc = dna_sequence[::-1].translate(str.maketrans("ATCG", "TAGC"))
  return sc


def format_output(reverse_complement):
  """
  Prepare the output for the reverse complement sequence by formatting it as required.
  """
  return reverse_complement


def test():
  # Test case 1
  dna_sequence = "GTCA"
  expected_output = "TGAC"
  assert format_output(complementing_a_strand_of_dna(dna_sequence)) == expected_output

  # Test case 2
  dna_sequence = "AAGCT"
  expected_output = "AGCTT"
  assert format_output(complementing_a_strand_of_dna(dna_sequence)) == expected_output

  # Test case 3
  dna_sequence = "TTAGGG"
  expected_output = "CCCTAA"
  assert format_output(complementing_a_strand_of_dna(dna_sequence)) == expected_output

  # Official test case
  dna_sequence = "AAAACCCGGT"
  expected_output = "ACCGGGTTTT"
  assert format_output(complementing_a_strand_of_dna(dna_sequence)) == expected_output

  print("All tests passed!")


def main():
  test()
  processing_pipeline(
    "rosalind_revc.txt",
    complementing_a_strand_of_dna,
    format_output
  )


if __name__ == "__main__":
  main()
