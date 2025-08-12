from aux import *

def count_dna_nucleotides(dna_sequence):
  """
  Counts the occurrences of each DNA nucleotide ('A', 'C', 'G', 'T') in the given DNA sequence.

  Args:
    dna_sequence (str): A string representing a DNA sequence consisting of characters 'A', 'C', 'G', and 'T'.

  Returns:
    dict: A dictionary with keys 'A', 'C', 'G', and 'T', and values representing the count of each nucleotide in the sequence.
  """
  count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
  for nucleotide in dna_sequence:
    if nucleotide in count:
      count[nucleotide] += 1
  return count


def test():
  # Test sequence provided by Rosalind
  seq1 = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
  expected = {'A': 20, 'C': 12, 'G': 17, 'T': 21}
  assert count_dna_nucleotides(seq1) == expected, "Test case 1 failed"

  # Additional test case provided by me
  seq2 = "CGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCT"
  expected2 = {'A': 9, 'C': 11, 'G': 10, 'T': 10}
  assert count_dna_nucleotides(seq2) == expected2, "Test case 2 failed"

  print("All tests passed!")


def prepare_output(counts):
  # Four integers (separated by spaces) counting the respective number of times
  # that the symbols 'A', 'C', 'G', and 'T' occur in s

  return " ".join(str(counts[nucleotide]) for nucleotide in ['A', 'C', 'G', 'T'])


def main():
  test()

  processing_pipeline(
    "rosalind_dna.txt",
    count_dna_nucleotides,
    prepare_output
  )


if __name__ == "__main__":
  main()
