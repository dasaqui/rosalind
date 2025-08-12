from aux import *

def searching_through_the_haystack(dataset):
  """
  Problem
    A common substring of a collection of strings is a substring of every
    member of the collection. We say that a common substring is a longest
    common substring if there does not exist a longer common substring.
    For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA",
    but it is not as long as possible; in this case, "CGTA" is a longest common
    substring of "ACGTACGT" and "AACCGTATA".

    Note that the longest common substring is not necessarily unique; for a
    simple example, "AA" and "CC" are both longest common substrings of "AACC"
    and "CCAA".

  Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in
    FASTA format.

  Return: A longest common substring of the collection. (If multiple solutions
    exist, you may return any single solution.)
  """
  chains = [c for c in dataset.split('>') if c.strip()]
  chains = ["".join(c.splitlines()[1:]) for c in chains]
  if not chains:
    return ""

  vocab = ["A","C","G","T"]
  sub_strings = {_k: [0 for _c in chains] for _k in vocab}
  _flag = True

  while _flag:
    new_sub_strings = {_k+_c: sub_strings[_k] for _k in sub_strings.keys() for _c in vocab}
    new_sub_strings = {_k: [_c.find(_k,_vv) for _c, _vv in zip(chains, _v)] for _k, _v in new_sub_strings.items()}
    new_sub_strings = {_k: _v for _k, _v in new_sub_strings.items() if all(_vv != -1 for _vv in _v)}
    if not new_sub_strings:
      _flag = False
    else:
      sub_strings = new_sub_strings

  return sub_strings


def prepare_output(longest_common_substring):
  if not longest_common_substring:
    return ""
  # return the first key from the dictionary
  return next(iter(longest_common_substring))


def test():
  # Official test case
  dataset = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""
  solution = "AC"
  assert prepare_output(searching_through_the_haystack(dataset)) == solution

  print("All tests passed!")


def main():
  test()
  processing_pipeline(
    "rosalind_lcsm.txt",
    searching_through_the_haystack,
    prepare_output
  )


if __name__ == "__main__":
  main()
