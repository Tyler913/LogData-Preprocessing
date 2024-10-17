import os
import zipfile

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
