import os
import shutil
import zipfile
import time
import send2trash


def unzip_file(source):
    """_summary_
    遍历在指定的文件夹下是否存在.zip文件，如果有就解压他
    并且在解压完成之后删除该文件
    如果解压完成之后是文件夹形式那将会转移该文件夹下的文件到原来的路径下

    Args:
        source (string): 指定文件夹的绝对路径
    """    
    
    files = os.listdir(source)
    
    for file in files:
        file_path = os.path.join(source, file)
        if os.path.isfile(file_path) and file.endswith(".zip"):
            extract_path = os.path.splitext(file_path)[0]
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            os.remove(file_path)
    
    for item in os.listdir(source):
        item_path = os.path.join(source, item)
        if os.path.isdir(item_path):
            for subitem in os.listdir(item_path):
                subitem_path = os.path.join(item_path, subitem)
                shutil.move(subitem_path, source)
            os.removedirs(item_path)

def mkdir(path):
    """_summary_
    创建一个临时文件夹，去存放所有含有"logcat"字样的文件
    e.g
        如果想在 "/Users/username/Desktop" 下创建一个名为 "logcat" 的文件夹
        则**destination**参数需要设置为 "/Users/username/Desktop"

    Args:
        destination (string):绝对路径
    """    
    
    file_path = os.path.join(path, "logcat")
    if not os.path.exists(file_path):
        os.makedirs(file_path)
        print("文件夹创建成功")
    else:
        print("文件夹已经存在")

def transfer_logcat_to_new_path(source, destination):
    """_summary_
    遍历在指定的文件夹下是否存在"logcat"文件夹，如果有就剪切这些文件到临时文件夹中

    Args:
        source (string):存放所有log日志文件的文件夹的绝对路径
        destination (string):刚才创建的绝对路径
    """    
    
    files = os.listdir(source)
    
    for file in files:
        file_path = os.path.join(source, file)
        if "logcat" in file:
            shutil.move(file_path, destination)
    print("所有带有logcat的日志文件已经移动到临时文件夹中")

def formatter(source):
    """_summary_
    这是一个将log文件中的双空格转换成单空格的函数
    会在脚本中自动执行，不会做出信息打印

    Args:
        source (string): 指定文件夹的绝对路径
    """    
    
    files = os.listdir(source)
    for file in files:
        file_path = os.path.join(source, file)
        with open (file_path, "r", encoding="latin-1") as file:
            context = file.read()
        changed_context = context.replace("  ", " ")
        with open(file_path, "w") as new_file:
            new_file.write(changed_context)

def to_analysis_folder(source, path, delete):
    """_summary_
    将存储在临时文件夹中的logcat日志转存到日志分析工具的文件夹下
    并且用户可以选择先删除原来的日志文件，再添加新的文件还是说保留原有的日志并且添加新的日志文件
    在完成日志文件的转存之后，会自动删除之前创建的临时文件夹

    Args:
        path (string): 分析文件夹的绝对路径
        delete (string): 是否保留原有的日志文件
        source (string): 临时文件夹的绝对路径
    """    
    
    files = os.listdir(path)
    if delete == "y" and files != []:
        for file in files:
            file_path = os.path.join(path, file)
            os.remove(file_path)
    else:
        pass
    log_files = os.listdir(source)
    for log_file in log_files:
        log_file_path = os.path.join(source, log_file)
        shutil.move(log_file_path, path)
    os.removedirs(source)


multiple_carid = input("是否需要分析多个carid的日志？（y or n）")
print()

if multiple_carid == "y":
    CarID = []
    log_path = []
    num_carid = int(input("需要分析的carid的数量：\n"))
    print()
    for _ in range (num_carid):
        CarID.append(input("输入CarID：\n"))
        log_path.append(input("输入日志文件夹的绝对路径：\n"))
    print()
    for i in range (num_carid):
        unzip_file(log_path[i])
    print()
    temp_path = input("输入临时文件夹的位置：\n")
    print()
    # for j in range (num_carid):
    #     file_path = os.path.join(temp_path, CarID[j])
    #     mkdir(file_path)
    #     transfer_logcat_to_new_path(log_path[j], file_path)
    #     formatter(file_path)
    mkdir(temp_path)
    for j in range (num_carid):
        file_path = os.path.join(temp_path, "logcat", CarID[j])
        os.makedirs(file_path)
        transfer_logcat_to_new_path(log_path[j], file_path)
        formatter(file_path)
    print()
    analysis_path = input("输入分析文件夹的位置：\n")
    delete = input("是否要删除原有的日志文件？（y or n）")
    if delete == "y":
        for root, dirs, files in os.walk(analysis_path):
            for file in files:
                file_path_de = os.path.join(root, file)
                send2trash(file_path_de)
    for k in range (num_carid):
        shutil.move(os.path.join(temp_path, "logcat", CarID[k]), analysis_path)
        # send2trash.send2trash(os.path.join(temp_path, "logcat", CarID[k]))
    send2trash.send2trash(os.path.join(temp_path, "logcat"))
    print("完成")
    
else:
    print("所有的路径都需要是绝对路径")
    print()
    time.sleep(1.5)
    initial_path = input("所有原始日志存放的位置：\n")
    print("其中的文件即将得到解压")
    time.sleep(1.5)
    unzip_file(initial_path)
    print("\n")
    print("解压完成")
    time.sleep(1.5)
    print()
    temp_path = input("输入临时文件夹的位置：\n")
    time.sleep(1.5)
    print()
    print("即将创建文件夹并且转移logcat文件到临时文件夹")
    print()
    mkdir(os.path.join(temp_path))
    print()
    transfer_logcat_to_new_path(initial_path, os.path.join(temp_path, "logcat"))
    formatter(os.path.join(temp_path, "logcat"))
    print()
    print("所有的logcat日志文件转存在分析文件夹下")
    print()
    time.sleep(1.5)
    analysis_path = input("输入分析文件夹的位置：\n")
    delete = input("是否要删除原有的日志文件？（y or n）")
    print()
    to_analysis_folder(os.path.join(temp_path, "logcat"), analysis_path, delete)
    print("完成")
