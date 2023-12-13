import os
import glob


def TimKiem(root_dir, ext):
 return glob.glob(os.path.join(
 root_dir, f'**/*{ext}'), recursive=True)


folder = r"C:\Users\vvn20206205\Desktop\solutions"
files = TimKiem(folder, '.md')
for f in files:
 print(f)
contents = """
Your input text here
"""

replacements = {
 'Monolithic': 'kiến trúc nguyên khối ',
 'monolithic': 'kiến trúc nguyên khối ',
 'Microservices': 'kiến trúc vi dịch vụ ',
 'microservices': 'kiến trúc vi dịch vụ ',
 'Microservice': 'kiến trúc vi dịch vụ ',
 'microservice': 'kiến trúc vi dịch vụ ',
 'dịch vụ vi mô': 'vi dịch vụ ',
 'Domain-Driven Design': 'thiết kế hướng miền ',
 'Domain Driven Design': 'thiết kế hướng miền ',
 'domain driven design': 'thiết kế hướng miền ',
 'ddd': 'thiết kế hướng miền ',
 'DDD': 'thiết kế hướng miền ',
 'patterns': 'mẫu ',
 'pattern': 'mẫu ',
 'cơ sở dữ liệu': 'CSDL ',
 'csdl': 'CSDL ',
 'database': 'CSDL ',
 'services': 'dịch vụ ',
 'service': 'dịch vụ ',
 'đội': 'nhóm ',
 '![Alt text](': '![](',
 'Domain expert': 'chuyên gia ngành ',
 'domain expert': 'chuyên gia ngành ',
 'chuyên gia kinh doanh': 'chuyên gia ngành ',
 'chuyên gia nghiệp vụ': 'chuyên gia ngành ',
 'chuyên gia tên miền': 'chuyên gia ngành ',
 'Ngôn ngữ phổ biến': 'ngôn ngữ chung ',
 'ngôn ngữ phổ biến': 'ngôn ngữ chung ',
 'bạn': 'chúng ta ',
 'Bạn': 'Chúng ta ',
 'tên miền': 'miền ',
 'Tên miền': 'Miền ',
 'bị ràng buộc': 'giới hạn ',
 'bị giới hạn': 'giới hạn ',
 'bị chặn': 'giới hạn ',
 'chống tham nhũng': 'chống đổ vỡ '
}

for key, value in replacements.items():
 contents = contents.replace(key, value)

# Now 'contents' variable contains the modified text
