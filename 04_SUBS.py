from aux import *

def combing_through_the_haystack(dataset):
  """
  Problem
    Given two strings s and t, t is a substring of s if t is contained as a
    contiguous collection of symbols in s (as a result, t must be no longer
    than s).

    The position of a symbol in a string is the total number of symbols found
    to its left, including itself (e.g., the positions of all occurrences of
    'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at
    position i of s is denoted by s[i].

    A substring of s can be represented as s[j:k], where j and k represent the
    starting and ending positions of the substring in s; for example, if
    s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

    The location of a substring s[j:k] is its beginning position j; note that t
    will have multiple locations in s if it occurs more than once as a
    substring of s (see the Sample below).

  Given: Two DNA strings s and t (each of length at most 1 kbp).

  Return: All locations of t as a substring of s.
  """
  _s, _t = dataset.splitlines()
  _s = _s.strip()
  _t = _t.strip()

  # iterate through all possible starting positions in _s
  start = 0
  next = _s.find(_t, start)
  positions = []
  while next != -1:
    positions.append(next + 1)
    start = next + 1
    next = _s.find(_t, start)

  return positions


def prepare_output(positions):
  return ' '.join(map(str, positions))


def test():
  # Test case 1
  dataset = "AUGCUUCAGAAAGGUCUUACG\nUGCU"
  expected_output = "2"
  assert prepare_output(combing_through_the_haystack(dataset)) == expected_output

  # Test case 2
  dataset = "GATTACA\nAT"
  expected_output = "2"
  assert prepare_output(combing_through_the_haystack(dataset)) == expected_output

  # Test case 3
  dataset = "AAAAA\nAA"
  expected_output = "1 2 3 4"
  assert prepare_output(combing_through_the_haystack(dataset)) == expected_output

  # Official test cases
  dataset = "GATATATGCATATACTT\nATAT"
  expected_output = "2 4 10"
  assert prepare_output(combing_through_the_haystack(dataset)) == expected_output

  print("All tests passed!")


def main():
  test()
  processing_pipeline(
    "rosalind_subs.txt",
    combing_through_the_haystack,
    prepare_output
  )

if __name__ == "__main__":
  main()
  