from aux import *

def rearrangements_power_large_scale_genomic_changes(num):
  """
  Problem
    A permutation of length n is an ordering of the positive integers {1,2,…,n}.
    For example, π=(5,3,2,1,4) is a permutation of length 5.

  Given: A positive integer n≤7.

  Return: The total number of permutations of length n, followed by a list of
    all such permutations (in any order).
  """
  # format n to int if it's a string
  if isinstance(num, str):
      num = int(num)

  # Generate all permutations of length n
  def permute(_n, seq):
    if len(seq) == _n:
      return [seq]
    _seq = [[*seq, i] for i in range(1, _n + 1) if i not in seq]

    __seq = [p for s in _seq for p in permute(_n, s)]
    return __seq
  seq = [p for s in range(1, num + 1) for p in permute(num, [s])]
  return len(seq), seq


def prepare_output(permutations):
  length, seq = permutations
  # Format the output as required
  output = f"{length}\n"
  output += "\n".join(" ".join(map(str, p)) for p in seq)
  return output


def test():
  # test case 1
  input_data = 3
  expected_output = "6\n1 2 3\n1 3 2\n2 1 3\n2 3 1\n3 1 2\n3 2 1"
  assert prepare_output(rearrangements_power_large_scale_genomic_changes(input_data)) == expected_output

  print("All tests passed!")


def main():
  test()


if __name__ == "__main__":
  main()

  processing_pipeline(
    "rosalind_perm.txt",
    rearrangements_power_large_scale_genomic_changes,
    prepare_output
  )