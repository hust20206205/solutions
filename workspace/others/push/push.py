from modules.MyImport import MyImport
# MyImport.Import()
from modules.MyNow import MyNow
message = "VuVanNghia20206205"
message = MyNow()
from modules.MyGit import MyGit
MyGit.add(message)
MyGit.commit(message)
# MyGit.push(message)
from modules.MyClose import MyClose
# MyClose.OpenGit()
MyClose.ScrollBar()
# MyClose.CollapseFolders()
MyClose.CloseAll()
MyClose.Target(2)
# MyClose.Terminal()
# from modules.MyChrome import MyChrome
# MyChrome("https://github.com/vvn20206205/test")
# MyChrome()
import glob
import os
latex_folder = os.getcwd()
file_paths = glob.glob(os.path.join(latex_folder, f'**/*.tex'), recursive=True)
for file_path in file_paths:
    # print(file_path)
    with open(file_path, 'r', encoding="utf-8") as file:
        contents = file.read()

    replacements = {
        '\\\\': '\\\\',
        '=': '=',
        '+': '+',
        '-': '-',
        '\\(': '$',
        '\\)': '$'
    }

    for key, value in replacements.items():
        value = f"  {value}  "
        contents = contents.replace(key, value)
     
         
    while ' .' in contents:
        contents = contents.replace(' .', '. ') 
    contents = contents.replace(' .', '. ') 
    while ' ,' in contents:
        contents = contents.replace(' ,', ', ') 
    contents = contents.replace(' ,', ', ') 
    while ' ?' in contents:
        contents = contents.replace(' ?', '? ') 
    contents = contents.replace(' ?','? ') 
    while ' :' in contents:
        contents = contents.replace(' :', ': ') 
    contents = contents.replace(' :',': ') 
    while ' :' in contents:
        contents = contents.replace(' :', ': ') 
    contents = contents.replace(' :',': ') 
    while '  ' in contents:
        contents = contents.replace('  ', ' ')
    while '( ' in contents:
        contents = contents.replace('( ', '(')
    while ' )' in contents:
        contents = contents.replace(' )', ')') 
    while '[ ' in contents:
        contents = contents.replace('[ ', '[')
    while ' ]' in contents:
        contents = contents.replace(' ]', ']')  
    while '{ ' in contents:
        contents = contents.replace('{ ', '{')
    while ' }' in contents:
        contents = contents.replace(' }', '}') 
    contents = '\n'.join(line.strip() for line in contents.split('\n'))
    while "\n\n\n" in contents:
        contents = contents.replace("\n\n\n", "\n\n")
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(contents)






# 
# 
# 
# 
 

# # https://www.udemy.com/course/domain-driven-design-and-microservices
