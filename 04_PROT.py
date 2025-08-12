from aux import *

def translating_rna_into_protein(rna_sequence):
  """
  Problem
    The 20 commonly occurring amino acids are abbreviated by using 20 letters
    from the English alphabet (all letters except for B, J, O, U, X, and Z).
    Protein strings are constructed from these 20 symbols. Henceforth, the term
    genetic string will incorporate protein strings along with DNA strings and
    RNA strings.

    The RNA codon table dictates the details regarding the encoding of specific
    codons into the amino acid alphabet.

  Given: An RNA string s corresponding to a strand of mRNA (of length at most
  10 kbp).

  Return: The protein string encoded by s.
  """
  CODON_TABLE = {
    "UUU":"F","CUU":"L","AUU":"I","GUU":"V",
    "UUC":"F","CUC":"L","AUC":"I","GUC":"V",
    "UUA":"L","CUA":"L","AUA":"I","GUA":"V",
    "UUG":"L","CUG":"L","AUG":"M","GUG":"V",
    "UCU":"S","CCU":"P","ACU":"T","GCU":"A",
    "UCC":"S","CCC":"P","ACC":"T","GCC":"A",
    "UCA":"S","CCA":"P","ACA":"T","GCA":"A",
    "UCG":"S","CCG":"P","ACG":"T","GCG":"A",
    "UAU":"Y","CAU":"H","AAU":"N","GAU":"D",
    "UAC":"Y","CAC":"H","AAC":"N","GAC":"D",
    "UAA":"Stop","CAA":"Q","AAA":"K","GAA":"E",
    "UAG":"Stop","CAG":"Q","AAG":"K","GAG":"E",
    "UGU":"C","CGU":"R","AGU":"S","GGU":"G",
    "UGC":"C","CGC":"R","AGC":"S","GGC":"G",
    "UGA":"Stop","CGA":"R","AGA":"R","GGA":"G",
    "UGG":"W","CGG":"R","AGG":"R","GGG":"G",
  }

  # divide dna sequence into codons
  codons = [rna_sequence[i:i+3] for i in range(0, len(rna_sequence), 3)]
  protein = []

  proteins = [CODON_TABLE[codon] for codon in codons]

  return "".join(proteins)


def prepare_output(protein_sequence):
  # cut string on first Stop
  stop_index = protein_sequence.find("Stop")
  if stop_index != -1:
    return protein_sequence[:stop_index]
  return protein_sequence


def test():
  # Official test
  rna_sequence = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
  protein = "MAMAPRTEINSTRING"
  assert prepare_output(translating_rna_into_protein(rna_sequence)) == protein

  # Print in green
  print("\033[92mAll tests passed!\033[0m")


def main():
  test()
  processing_pipeline(
    "rosalind_prot.txt",
    translating_rna_into_protein,
    prepare_output
  )


if __name__ == "__main__":
  main()