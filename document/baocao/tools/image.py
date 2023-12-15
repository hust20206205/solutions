import os
import glob


def TimKiem(root_dir, ext):
    return glob.glob(os.path.join(
        root_dir, f'**/*{ext}'), recursive=True)


base_folder = os.path.join(os.getcwd(), "..")
folder = os.path.join(base_folder, "pictures")

files = TimKiem(folder, '.png')
files += TimKiem(folder, '.jpg')

with open(os.path.join(folder,"_image.md"), 'w') as markdown:
    for file in files:
        markdown.write(f"========================================\n")
        markdown.write(f"![]({os.path.relpath(file, folder)})\n")
        markdown.write(f"\n")
        markdown.write(f"\\begin{{figure}}[h]\n")
        markdown.write(f"\\centering\n")
        markdown.write("\\includegraphics[height=3cm]{"+f"{os.path.relpath(file, base_folder)}"+"}\n")
        markdown.write("\\caption{vvn20206205}\n")
        markdown.write("\\label{pictures:"+ f"{os.path.relpath(file, folder)}"+"}\n")
        markdown.write(f"\\end{{figure}}\n")
        markdown.write(f"========================================\n")
        
 
