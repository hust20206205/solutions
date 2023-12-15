import os
import glob


def TimKiem(root_dir, ext):
 return glob.glob(os.path.join(
 root_dir, f'**/*{ext}'), recursive=True)


folder = r"C:\Users\vvn20206205\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\New folder\Video\DDD\_DDD\07 Domain Driven Design - Tactical Patterns"
files = TimKiem(folder, '.srt')
# files = TimKiem(folder, '.md')
for f in files:
 print(f)


 