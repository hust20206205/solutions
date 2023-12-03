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
MyClose.ScrollBar()
# MyClose.CollapseFolders()
MyClose.CloseAll()
MyClose.Target(2)
MyClose.Terminal()
from modules.MyChrome import MyChrome
# MyChrome("https://github.com/vvn20206205/test")
# MyChrome()
import glob
import os
print(os.getcwd())
os.chdir("document/latex")
print(os.getcwd())
latex_folder = os.getcwd()
file_paths = glob.glob(os.path.join(latex_folder, f'**/*.tex'), recursive=True)
for file_path in file_paths:
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()

    content = content.replace('\\\\', '             \\\\          ')
    while '  ' in content:
        content = content.replace('  ', ' ')
    while '{ ' in content:
        content = content.replace('{ ', '{')
    while ' }' in content:
        content = content.replace(' }', '}')
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(content)
        # 
    with open(file_path, 'r', encoding="utf-8") as file:
        contents = file.readlines()
    contents = [line.strip() for line in contents]
    with open(file_path, 'w', encoding="utf-8") as file:
        for line in contents:
            file.write(line + '\n')
file_paths = glob.glob(os.path.join(latex_folder, f'**/*.md'), recursive=True)
for file_path in file_paths:
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()

    content = content.replace('\\\\', '             \\\\          ')
    while '  ' in content:
        content = content.replace('  ', ' ')
    while '<!-- ' in content:
        content = content.replace('<!-- ', '<!--')
    while ' -->' in content:
        content = content.replace(' -->', '-->')
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(content)
        # 
    with open(file_path, 'r', encoding="utf-8") as file:
        contents = file.readlines()
    contents = [line.strip() for line in contents]
    with open(file_path, 'w', encoding="utf-8") as file:
        for line in contents:
            file.write(line + '\n')