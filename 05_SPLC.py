from aux import *

def rna_splicing(fasta_string):
  """
  Problem
    After identifying the exons and introns of an RNA string, we only need to
    delete the introns and concatenate the exons to form a new string ready
    for translation.

  Given: A DNA string s (of length at most 1 kbp) and a collection of
    substrings of s acting as introns. All strings are given in FASTA format.

  Return: A protein string resulting from transcribing and translating the
    exons of s. (Note: Only one solution will exist for the dataset provided.)
  """
  fasta_entries = list(decode_fasta(fasta_string).values())
  
  # Split into string and sub-strings
  main_string = fasta_entries[0]
  introns = fasta_entries[1:]

  # Translate DNA into RNA
  def translate_dna_to_rna(dna_string):
    return dna_string.replace("T", "U")

  # Translate the main string
  proteins = []
  started = True
  start_point = 0
  while start_point < len(main_string):
    if started:
      _introns = [intron for intron in introns if main_string.startswith(intron, start_point)]
      if len(_introns) > 0:
        started = True
        start_point += len(_introns[0])
        print(f"Intron found at position {start_point}. Skipping segment.")
      else:
        codon = main_string[start_point:start_point + 3]
        codon = translate_dna_to_rna(codon)
        if codon in CODON_TABLE:
          if CODON_TABLE[codon] != "Stop":
            proteins.append(CODON_TABLE[codon])
          else:
            started = False
            print(f"Stop codon encountered at position {start_point}. Ending translation.")
        start_point += 3
    else:
      _introns = [intron for intron in introns if main_string.startswith(intron, start_point)]
      if len(_introns) > 0:
        started = True
        start_point += len(_introns[0])
        print(f"Intron found at position {start_point}. Resuming translation.")
      else:
        start_point += 1
  
  return ''.join(proteins)


def prepare_output(protein_string):
  # Format the output as required
  return protein_string


def test():
  # Official test case
  fasta_string = """>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT"""
  expected_output = "MVYIADKQHVASREAYGHMFKVCA"
  assert prepare_output(rna_splicing(fasta_string)) == expected_output

  # Print success message
  print("\033[92mAll tests passed!\033[0m")


def main():
  test()
  processing_pipeline(
    "rosalind_splc.txt",
    rna_splicing,
    prepare_output
  )


if __name__ == "__main__":
  main()