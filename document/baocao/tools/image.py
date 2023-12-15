import os
import glob


def TimKiem(root_dir, ext):
    return glob.glob(os.path.join(
        root_dir, f'**/*{ext}'), recursive=True)


base_folder = os.path.join(os.getcwd(), "..")
folder = os.path.join(base_folder, "pictures")

print(folder)
files = TimKiem(folder, '.png')
files += TimKiem(folder, '.jpg')

with open("_image.md", 'w') as markdown:
    for file in files:
        markdown.write(f"![]({os.path.relpath(file, base_folder)})\n")
