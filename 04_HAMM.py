from aux import *

def counting_point_mutations(dataset):
  """
  Problem
    Given two strings s and t of equal length, the Hamming distance between s
    and t, denoted dH(s,t), is the number of corresponding symbols that
    differ in s and t.

  Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

  Return: The Hamming distance dH(s,t).
  """
  str1, str2 = dataset.splitlines()
  if len(str1) != len(str2):
      raise ValueError("DNA strings must be of equal length")

  return sum(1 for a, b in zip(str1, str2) if a != b)


def prepare_output(hamming_distance):
  return str(hamming_distance)


def test():
  # Test case 1
  dataset = "GAGCCTACTAACGGGAT\nCATCGTAATACGGCCTT"
  expected_output = "9"
  assert prepare_output(counting_point_mutations(dataset)) == expected_output

  # Official test case
  dataset = "GAGCCTACTAACGGGAT\nCATCGTAATGACGGCCT"
  expected_output = "7"
  assert prepare_output(counting_point_mutations(dataset)) == expected_output

  print("All tests passed!")


def main():
  test()
  processing_pipeline(
    "rosalind_hamm.txt",
    counting_point_mutations,
    prepare_output
  )


if __name__ == "__main__":
  main()
