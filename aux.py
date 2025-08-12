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
    return None

  # Read the contents of the file
  with open(_file, "r") as file:
    return file.read().strip()
  

def write_sequence(sequence):
  # Use current folder to save
  with open("output.txt", "w") as file:
    file.write(sequence)