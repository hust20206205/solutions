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
# MyClose.Target(4)
MyClose.Target(3)
MyClose.Terminal()
from modules.MyChrome import MyChrome
# MyChrome("https://github.com/vvn20206205/test")
# MyChrome()
import glob
import os
print(os.getcwd())
# os.chdir("document/latex")
print(os.getcwd())
latex_folder = os.getcwd()
# file_paths = glob.glob(os.path.join(latex_folder, f'**/*.tex'), recursive=True)
 

#     content = content.replace('\\\\', '             \\\\          ')
#     while '  ' in content:
#         content = content.replace('  ', ' ')
#     while '{ ' in content:
#         content = content.replace('{ ', '{')
#     while ' }' in content:
#         content = content.replace(' }', '}') 
#     content = [line.strip() for line in content] 
file_paths = glob.glob(os.path.join(latex_folder, f'**/*.md'), recursive=True)
for file_path in file_paths:
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()

    # content = content.replace("=", " = ")
    # content = content.replace("+", " + ")
    # content = content.replace("-", " - ") 
    content = content.replace('Monolithic', '                                     kiến trúc nguyên khối ')
    content = content.replace('monolithic', '                                 kiến trúc nguyên khối ')
    content = content.replace('Microservices', '                                 kiến trúc vi dịch vụ   ')
    content = content.replace('microservices', '                                kiến trúc vi dịch vụ         ')
    content = content.replace('Microservice', '                                kiến trúc vi dịch vụ         ')
    content = content.replace('microservice', '                                kiến trúc vi dịch vụ         ')
    content = content.replace('dịch vụ vi mô', '                                vi dịch vụ         ')
    content = content.replace('Domain-Driven Design', '                                thiết kế hướng miền         ')
    content = content.replace('Domain Driven Design', '                                thiết kế hướng miền         ')
    content = content.replace('ddd', '                                 thiết kế hướng miền          ')
    content = content.replace('DDD', '                                 thiết kế hướng miền          ')
    content = content.replace('patterns', '                                mẫu         ')
    content = content.replace('pattern', '                                mẫu         ')
    content = content.replace('cơ sở dữ liệu', '                                CSDL         ')
    content = content.replace('csdl', '                                CSDL         ')
    content = content.replace('database', '                                CSDL         ')
    content = content.replace('services', '                                dịch vụ         ')
    content = content.replace('service', '                                dịch vụ         ')
    content = content.replace('đội', '                                nhóm         ')
    content = content.replace('![Alt text](', '                                ![](')


    

    content = content.replace('Domain expert', '           chuyên gia ngành     ')
    content = content.replace('domain expert', '           chuyên gia ngành     ')
    content = content.replace('chuyên gia kinh doanh', '           chuyên gia ngành     ')
    content = content.replace('chuyên gia nghiệp vụ', '           chuyên gia ngành     ')
    content = content.replace('chuyên gia tên miền', '           chuyên gia ngành     ')

    # content = content.replace('.' 
    # content = content.replace('bài toán', 'giải pháp')
    
    while " ?" in content:
        content = content.replace(" ?", "?")
    content = content.replace("?", "? ")
    
    while " ," in content:
        content = content.replace(" ,", ",")
    content = content.replace(",", ", ")
    
    while " :" in content:
        content = content.replace(" :", ":")
    content = content.replace(":", ": ")
    
    # content = content.replace("https: ","https:")
    
    # while " !" in content:
    #     content = content.replace(" !", "!")
    # content = content.replace("!", "! ")


    while '  ' in content:
        content = content.replace('  ', ' ')
    while '<!-- ' in content:
        content = content.replace('<!-- ', '<!--')
    while ' -->' in content:
        content = content.replace(' -->', '-->')
    while '( ' in content:
        content = content.replace('( ', '(')
    while ' )' in content:
        content = content.replace(' )', ')')
        # 
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(content)
        # 
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.readlines()
    content = [line.strip() for line in content]
    with open(file_path, 'w', encoding="utf-8") as file:
        for line in content:
            file.write(line + '\n')

# https://www.udemy.com/course/domain-driven-design-and-microservices
