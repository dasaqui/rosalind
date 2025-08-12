from glob import glob
import os

def read_sequence(expected_name):
  # Expecting to be run in a linux environment
  # Search for the home directory
  home_directory = os.path.expanduser("~")

  # Search for Download/Descargas folders
  folders = [os.path.join(home_directory, "Descargas"), os.path.join(home_directory, "Downloads")]
  files = []
  for folder in folders:
    if os.path.exists(folder):
      # Search for the expected file in the folder
      files.extend(glob(os.path.join(folder, expected_name)))
      # Search for subsequent copies
      files.extend(glob(os.path.join(folder, f"{expected_name.replace('.txt', ' (*).txt')}")))

  # Search for the newest file
  if files:
    _file = max(files, key=os.path.getctime)
  else:
    raise FileNotFoundError(f"No file named '{expected_name}' found in {folders}")

  # Print in yellow
  print(f"\033[93mReading from: {_file}\033[0m")

  # Read the contents of the file
  with open(_file, "r") as file:
    return file.read().strip()
  

def write_sequence(sequence):
  # Use current folder to save
  with open("output.txt", "w") as file:
    file.write(sequence)


def processing_pipeline(input_file, processing_function, formatting_function):
  # Read the input sequence
  sequence = read_sequence(input_file)

  # Process the sequence
  result = processing_function(sequence)

  # Prepare the output
  output = formatting_function(result)

  # Print the output
  print(output)

  # Write the output
  write_sequence(output)