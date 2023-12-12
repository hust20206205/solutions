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
    print(file_path)
    with open(file_path, 'r', encoding="utf-8") as file:
        contents = file.read()
    contents = contents.replace('\\\\', '             \\\\          ')
    while '  ' in contents:
        contents = contents.replace('  ', ' ')
    while '{ ' in contents:
        contents = contents.replace('{ ', '{')
    while ' }' in contents:
        contents = contents.replace(' }', '}') 
    contents = '\n'.join(line.strip() for line in contents.split('\n'))
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(contents)
# #     contents = [line.strip() for line in contents] 







# file_paths = glob.glob(os.path.join(latex_folder, f'**/*.md'), recursive=True)
# for file_path in file_paths:
#     with open(file_path, 'r', encoding="utf-8") as file:
#         contents = file.read()

#     # contents = contents.replace("=", " = ")
#     # contents = contents.replace("+", " + ")
#     # contents = contents.replace("-", " - ") 
#     contents = contents.replace('Monolithic', '                                     kiến trúc nguyên khối ')
#     contents = contents.replace('monolithic', '                                 kiến trúc nguyên khối ')
#     contents = contents.replace('Microservices', '                                 kiến trúc vi dịch vụ   ')
#     contents = contents.replace('microservices', '                                kiến trúc vi dịch vụ         ')
#     contents = contents.replace('Microservice', '                                kiến trúc vi dịch vụ         ')
#     contents = contents.replace('microservice', '                                kiến trúc vi dịch vụ         ')
#     contents = contents.replace('dịch vụ vi mô', '                                vi dịch vụ         ')
#     contents = contents.replace('Domain-Driven Design', '                                thiết kế hướng miền         ')
#     contents = contents.replace('Domain Driven Design', '                                thiết kế hướng miền         ')
#     contents = contents.replace('domain driven design', '                                thiết kế hướng miền         ')
#     contents = contents.replace('ddd', '                                 thiết kế hướng miền          ')
#     contents = contents.replace('DDD', '                                 thiết kế hướng miền          ')
#     contents = contents.replace('patterns', '                                mẫu         ')
#     contents = contents.replace('pattern', '                                mẫu         ')
#     contents = contents.replace('cơ sở dữ liệu', '                                CSDL         ')
#     contents = contents.replace('csdl', '                                CSDL         ')
#     contents = contents.replace('database', '                                CSDL         ')
#     contents = contents.replace('services', '                                dịch vụ         ')
#     contents = contents.replace('service', '                                dịch vụ         ')
#     contents = contents.replace('đội', '                                nhóm         ')
#     contents = contents.replace('![Alt text](', '                                ![](')


    

#     contents = contents.replace('Domain expert', '           chuyên gia ngành     ')
#     contents = contents.replace('domain expert', '           chuyên gia ngành     ')
#     contents = contents.replace('chuyên gia kinh doanh', '           chuyên gia ngành     ')
#     contents = contents.replace('chuyên gia nghiệp vụ', '           chuyên gia ngành     ')
#     contents = contents.replace('chuyên gia tên miền', '           chuyên gia ngành     ')

#     contents = contents.replace('Ngôn ngữ phổ biến', '      ngôn ngữ chung     ')
#     contents = contents.replace('ngôn ngữ phổ biến', '      ngôn ngữ chung     ')
#     contents = contents.replace('bạn', '      chúng ta     ')
#     contents = contents.replace('Bạn', '      Chúng ta     ')
#     contents = contents.replace('tên miền', '       miền   ')
#     contents = contents.replace('Tên miền', '       Miền   ')
    
#     contents = contents.replace('bị ràng buộc', '       giới hạn   ')
#     contents = contents.replace('bị giới hạn', '       giới hạn   ')
#     contents = contents.replace('bị chặn', '       giới hạn   ')
#     contents = contents.replace('chống tham nhũng', '       chống đổ vỡ   ')
#     # contents = contents.replace('.' 
    
#     while "\n\n\n" in contents:
#         contents = contents.replace("\n\n\n", "\n\n")
#     contents = contents.replace("?", "? ")
#     while " ?" in contents:
#         contents = contents.replace(" ?", "?")
#     contents = contents.replace("?", "? ")
    
#     while " ," in contents:
#         contents = contents.replace(" ,", ",")
#     contents = contents.replace(",", ", ")
    
#     # while " :" in contents:
#     #     contents = contents.replace(" :", ":")
#     # contents = contents.replace(":", ": ")
    
    
#     # while " !" in contents:
#     #     contents = contents.replace(" !", "!")
#     # contents = contents.replace("!", "! ")


#     while '  ' in contents:
#         contents = contents.replace('  ', ' ')
#     while '<!-- ' in contents:
#         contents = contents.replace('<!-- ', '<!--')
#     while ' -->' in contents:
#         contents = contents.replace(' -->', '-->')
#     while '! ' in contents:
#         contents = contents.replace('! ', '!')
#     while ' !' in contents:
#         contents = contents.replace(' !', '!')
#     while '@ ' in contents:
#         contents = contents.replace('@ ', '@')
#     while ' @' in contents:
#         contents = contents.replace(' @', '@')
#     while '( ' in contents:
#         contents = contents.replace('( ', '(')
#     while ' )' in contents:
#         contents = contents.replace(' )', ')')
#         # 
#     with open(file_path, 'w', encoding="utf-8") as file:
#         file.write(contents)
#         # 
#     # with open(file_path, 'r', encoding="utf-8") as file:
#     #     contents = file.readlines()
#     # contents = [line.strip() for line in contents]
#     # with open(file_path, 'w', encoding="utf-8") as file:
#     #     for line in contents:
#     #         file.write(line + '\n')

# # https://www.udemy.com/course/domain-driven-design-and-microservices
