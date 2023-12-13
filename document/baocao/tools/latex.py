from modules.Convert import Convert
import os
import shutil
import pyperclip
# nhận văn bản
input = pyperclip.paste()

# Define a regular expression pattern to match text inside curly braces
pattern = r'\{([^}]+)\}'

# Use re.search to find the pattern in the input string
match = re.search(pattern, input_str)

# Extract the text inside curly braces if a match is found
if match:
    output_str = match.group(1)
    print(output_str)
else:
    print("No match found.")
output = Convert.VarSnakeCase(input)
# sao chép file
ten_file_nguon = r"C:\Users\vvn20206205\Desktop\LatexATS\document\latex\contents\a.tex"
ten_file_dich = os.path.join(os.path.dirname(
    ten_file_nguon), f"{output}"+".tex")
shutil.copy(ten_file_nguon, ten_file_dich)
# return văn bản
output = "\\input{contents/" + output + "}"
pyperclip.copy(output)
