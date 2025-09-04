from aux import *

def finding_a_spliced_motif(fasta_string):
  """
  Problem
    A subsequence of a string is a collection of symbols contained in order
    (though not necessarily contiguously) in the string (e.g., ACG is a
    subsequence of TATGCTAAGATC). The indices of a subsequence are the
    positions in the string at which the symbols of the subsequence appear;
    thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).

    As a substring can have multiple locations, a subsequence can have multiple
    collections of indices, and the same index can be reused in more than one
    appearance of the subsequence; for example, ACG is a subsequence of
    AACCGGTT in 8 different ways.

  Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

  Return: One collection of indices of s in which the symbols of t appear as a
  subsequence of s. If multiple solutions exist, you may return any one.
  """
  fasta_entries = decode_fasta(fasta_string)
  s = fasta_entries[list(fasta_entries.keys())[0]]
  t = fasta_entries[list(fasta_entries.keys())[1]]

  # iterate through all possible starting positions in s
  start = 0
  index = 0
  next = s.find(t[index], start)
  positions = []
  while next != -1 and index < len(t):
    start = next + 1
    index += 1
    positions.append(start)
    if index < len(t):
      next = s.find(t[index], start)

  return positions


def prepare_output(positions):
  return ' '.join(map(str, positions))


def test():
  # Official test cases
  dataset = """>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA"""
  expected_output = "3 4 5"
  assert prepare_output(finding_a_spliced_motif(dataset)) == expected_output, "Official test case failed"

  print("All tests passed!")


def main():
  test()
  processing_pipeline(
    "rosalind_sseq.txt",
    finding_a_spliced_motif,
    prepare_output
  )

if __name__ == "__main__":
  main()