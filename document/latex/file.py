file=r"C:\Users\vvn20206205\Documents\_______test\z\_DDD\08EventsDrivenArchitectureDomainEvents_VVN\000000001_vn2_nghia.mp4"
import os
# print(os.path.dirname(file))
folder=os.path.dirname(file)
import glob 
def TimKiem(root_dir, ext):
        return glob.glob(os.path.join(
            root_dir, f'**/*{ext}'), recursive=True)
sub_files=TimKiem(folder,'.srt')
# print(sub_files)
contents=""
for i in sub_files:
    # print(i)
    with open(i,mode="r",  encoding='utf-8') as f:
        contents += f"<!--@ {i.replace("C:\\Users\\vvn20206205\\Documents\\_______test\\z\\_DDD","")} -->\n\n"
        contents += f.read()
    with open("_output.md",mode="w",  encoding='utf-8') as output:
        output.write(contents)
# <!-- Ubiquitous Language, and Bounded Context. -->
    