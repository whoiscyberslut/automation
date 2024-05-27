from pathlib import Path

filename = Path("source_data/text_files/raw_data.txt")

print(filename.name) # prints "raw_data.txt"
print(filename.suffix) # prints "txt"
print(filename.stem) # prints "raw_data"

if not filename.exists():
  print("Oops, file doesn't exist!")
else:
  print("Yay, the file exists!")

# Use pathlib to generate file:// urls and open a local file in your web browser

import webbrowser
from pathlib import Path
filename = Path("source_data/text_files/raw_data.txt")
webbrowser.open(filename.absolute().as_uri())
