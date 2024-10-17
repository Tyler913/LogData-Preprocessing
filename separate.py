import os
import shutil

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
