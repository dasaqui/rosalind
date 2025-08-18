from aux import *

def computing_gc_content(dataset):
  """
  Problem
    The GC-content of a DNA string is given by the percentage of symbols in the
    string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is
    37.5%. Note that the reverse complement of any DNA string has the same
    GC-content.

    DNA strings must be labeled when they are consolidated into a database. A
    commonly used method of string labeling is called FASTA format. In this
    format, the string is introduced by a line that begins with '>', followed
    by some labeling information. Subsequent lines contain the string itself;
    the first line to begin with '>' indicates the label of the next string.

    In Rosalind's implementation, a string in FASTA format will be labeled by
    the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between
    0000 and 9999.

  Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

  Return: The ID of the string having the highest GC-content, followed by the
  GC-content of that string. Rosalind allows for a default error of 0.001 in
  all decimal answers unless otherwise stated; please see the note on absolute
  error below.
  """
  fasta_entries = decode_fasta(dataset)
  gc_contents = {id: gc_content(entry) for id, entry in fasta_entries.items()}
  max_gc = max(gc_contents, key=gc_contents.get)
  return max_gc, gc_contents[max_gc]

def gc_content(dna_string):
  """
  Calculate the GC-content of a DNA string.
  """
  gc_count = len([1 for base in dna_string if base in 'GC'])
  return gc_count / len(dna_string) * 100

def prepare_output(gc_content_result):
  """
  Format the output as required.
  """
  id_string, gc_value = gc_content_result
  return f"{id_string}\n{gc_value:.6f}"

def test():
  # Official test case
  fasta_string = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""
  result = "Rosalind_0808\n60.919540"
  assert prepare_output(computing_gc_content(fasta_string)) == result, "Test case failed"

  print("\033[92mAll tests passed!\033[0m")

def main():
  test()
  processing_pipeline(
    "rosalind_gc.txt",
    computing_gc_content,
    prepare_output
  )
  

if __name__ == "__main__":
  main()