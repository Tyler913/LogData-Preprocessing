import os
import shutil


def merge(source, distination):
    for root, dirs, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as one_file:
                context = one_file.read()
                print(context)
            # output_path = os.path.join(distination, 'final_analysis.log')
            with open(distination, 'a') as output:
                output.write(context)
                
def unzip_files(source_dir):
    # 获取源路径下的所有文件
    files = os.listdir(source_dir)
    
    for file in files:
        file_path = os.path.join(source_dir, file)
        if os.path.isfile(file_path) and file.endswith('.zip'):
            # 解压缩文件到相同路径
            extract_path = os.path.splitext(file_path)[0]
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            
            # 删除压缩包
            os.remove(file_path)

def dirToFile(source, distination):
    for item in os.listdir(source):
        item_path = os.path.join(source, item)

        if os.path.isdir(item_path):
            for subitem in os.listdir(item_path):
                subitem_path = os.path.join(item_path, subitem)
                shutil.move(subitem_path, distination)
            os.removedirs(item_path)
            
def extract(start, end, file_path):
    with open(file_path, 'r') as file:
        context = file.read()
        print(context)
        strat_index = context.find(start)
        end_index = context.find(end)
        if strat_index != -1 and end_index != -1:
            extracted_text = context[strat_index + len(start) : end_index]
            return extracted_text
        else:
            return None

def transfer(source, distination, start, end):
    for root, dirs, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root, file)
            extracted_text = extract(start, end, file_path)
            if extracted_text != None:
                outfile = file.replace('.log', '_extracted.log')
                outpath = os.path.join(distination, outfile)
                with open(outpath, 'w') as output:
                    output.write(extracted_text)

def change_space(file_path):
    with open(file_path, 'r') as file:
        context = file.read()
    changed_context = context.replace("  ", " ")
    
    with open(file_path, 'w') as new_file:
        new_file.write(changed_context)

def select_words(key_word, source, destination):
    for root, dirs, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as lines:
                # each_line = lines.readline()
                # if each_line != '' and each_line.find(key_word) != -1:
                #     output_path = os.path.join(destination, file)
                #     with open(output_path, 'w') as output:
                #         output.write(each_line)
                each_line = lines.readline()
                while each_line != '':
                    if each_line.find(key_word) != -1:
                        output_path = os.path.join(destination, file)
                        with open(output_path, 'a') as output:
                            output.write(each_line)
                    each_line = lines.readline()

def classify_files(source_dir, destination_dir, keywords):
    # 读出所有的文件
    files = os.listdir(source_dir)
    
    for file in files:
        file_path = os.path.join(source_dir, file)
        
        if os.path.isfile(file_path):
            # 检查文件名是否包含关键字
            for keyword in keywords:
                if keyword in file:
                    # 创建目标路径，如果不存在的话
                    destination_path = os.path.join(destination_dir)
                    os.makedirs(destination_path, exist_ok=True)
                    
                    # 移动文件到目标路径
                    shutil.move(file_path, destination_path)
                    break

