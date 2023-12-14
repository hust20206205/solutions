import os
import glob
from modules.MyClose import MyClose
from modules.MyGit import MyGit
from modules.MyImport import MyImport
# MyImport.Import()
from modules.MyNow import MyNow
message = "VuVanNghia20206205"
message = MyNow()
MyGit.add(message)
MyGit.commit(message)
# MyGit.push(message)
# MyClose.OpenGit()
MyClose.ScrollBar()
# MyClose.CollapseFolders()
MyClose.CloseAll()
MyClose.Target(1)
MyClose.Terminal()
# MyClose.Latex()
# from modules.MyChrome import MyChrome
# MyChrome("https://github.com/vvn20206205/test")
# MyChrome()
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
        '\\)': '$',

        'Monolithic': 'kiến trúc nguyên khối',
        'monolithic': 'kiến trúc nguyên khối',

        'Microservices': 'kiến trúc vi dịch vụ',
        'microservices': 'kiến trúc vi dịch vụ',
        'Microservice': 'kiến trúc vi dịch vụ',
        'microservice': 'kiến trúc vi dịch vụ',
        'dịch vụ vi mô': 'vi dịch vụ',

        'Domain-Driven Design': 'thiết kế hướng miền',
        'Domain Driven Design': 'thiết kế hướng miền',
        'domain driven design': 'thiết kế hướng miền',
        'ddd': 'thiết kế hướng miền',
        'DDD': 'thiết kế hướng miền',

        'patterns': 'mẫu',
        'pattern': 'mẫu',

        'cơ sở dữ liệu': 'CSDL',
        'csdl': 'CSDL',
        'database': 'CSDL',

        'services': 'dịch vụ',
        'service': 'dịch vụ',

        'đội': 'nhóm',

        '![Alt text](': '![](',

        'Domain expert': 'chuyên gia ngành',
        'domain expert': 'chuyên gia ngành',
        'chuyên gia kinh doanh': 'chuyên gia ngành',
        'chuyên gia nghiệp vụ': 'chuyên gia ngành',
        'chuyên gia tên miền': 'chuyên gia ngành',

        'Ngôn ngữ phổ biến': 'ngôn ngữ chung',
        'ngôn ngữ phổ biến': 'ngôn ngữ chung',
        'phổ biến': 'chung',

        'bạn': 'chúng ta',
        'Bạn': 'Chúng ta',

        'tên miền': 'miền',
        'Tên miền': 'Miền',

        'bị ràng buộc': 'giới hạn',
        'bị giới hạn': 'giới hạn',
        'bị chặn': 'giới hạn',

        'chống tham nhũng': 'chống đổ vỡ',


        'Tổng Cục Thuế': 'TCT',

        'tổng Cục Thuế': 'TCT',
        'Tổng cục Thuế': 'TCT',
        'Tổng Cục thuế': 'TCT',

        'tổng cục Thuế': 'TCT',
        'tổng Cục thuế': 'TCT',
        'Tổng cục thuế': 'TCT', 




        'tổng cục thuế': 'TCT',
        "kiến ​​trúc": 'kiến trúc',
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
    contents = contents.replace(' ?', '? ')
    # while ' :' in contents:
    #     contents = contents.replace(' :', ': ')
    # contents = contents.replace(' :', ': ')
    # while ' :' in contents:
    #     contents = contents.replace(' :', ': ')
    # contents = contents.replace(' :', ': ')
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
    contents = contents.lstrip('\n')
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(contents)


#
#
#
#


# # https://www.udemy.com/course/domain-driven-design-and-microservices
