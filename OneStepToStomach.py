# import
import os
import shutil
import send2trash
import zipfile
import tarfile


class CheckTarGZ():
    def __init__(self, path) -> None:
        """_summary_
        init the path.

        Args:
            path (string): # ? Absolute path of the folder.
        """        
        self.path = path

    def get_targz_dir(self) -> list:
        """_summary_
        # ! Get the .tar.gz file in the path.

        Returns:
            list: if the .tar.gz file is in the path, return the .tar.gz file path.
            # ? the absolute path of the .tar.gz file will be return.
        """        
        tar_gz_dirs = []
        for root, _, files in os.walk(self.path):
            for file in files:
                if file.endswith(".tar.gz"):
                    tar_gz_dirs.append(root)
        return tar_gz_dirs
    
    def targz_exist(self) -> bool:
        """_summary_
        # ! Check if the .tar.gz file exist in the path.

        Returns:
            Boolean: if the .tar.gz file exist in the path, return True, else return False.
        """        
        if len(self.get_targz_dir()) == 0:
            return False
        else:
            return True
    
    def get_targz_sub_root(self) -> list:
        """_summary_
        # ! Get the sub root of the tar.gz file.
        
        Returns:
            list: if the .tar.gz file is in the path, return the sub root of the tar.gz file.
            for example: /Users/tyler/Desktop/Development/Smart/document/2020-12-01/2020-12-01-10-00-00.tar.gz
            # ? program will return [2020-12-01]
        """        
        sub_root = []
        for i in range (len(self.get_targz_dir())):
            for j in range (len(self.get_targz_dir()[i])):
                if self.get_targz_dir()[i][len(self.get_targz_dir()[i])-j-1] == "/" or self.get_targz_dir()[i][len(self.get_targz_dir()[i])-j-1] == "\\":
                    sub_root.append(self.get_targz_dir()[i][len(self.get_targz_dir()[i])-j : ])
                    break
        return sub_root


def mkdir(source, name) -> None:
    """_summary_
    # ! Create folder in the source path, with the name provided

    Args:
        source (string): The absolute path of the source folder.
        name (string): The name of the folder.
    """    
    folder_path = os.path.join(source, name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print("Create folder: " + folder_path)
    else:
        print("Folder exist: " + folder_path)

def transfer_logcat_files(source, destination) -> None:
    """_summary_
    # ! Transfer the logcat files from source to destination.

    Args:
        source (string): The absolute path of the source folder.
        destination (string): The absolute path of the destination folder.
    """    
    files = os.listdir(source)
    for file in files:
        file_path = os.path.join(source, file)
        if "logcat" in file:
            shutil.move(file_path, destination)

def get_temp_path(file_path) -> str:
    """_summary_
    # ! Find the temp path of the file
    if the file path is /Users/tyler/Desktop/Development/Smart/document/2020-12-01
    # ? than the temp path will be /Users/tyler/Desktop/Development/Smart/document

    Args:
        file_path (string): The path which contain the file.
    
    Returns:
        str: The temp path of the file.
    """    
    for i in range (len(file_path)):
        if file_path[len(file_path)-i-1] == "/" or file_path[len(file_path)-i-1] == "\\":
            temp_path = file_path[ : len(file_path)-i]
            break
    return os.path.join(temp_path)

def unzip_file(source):
    """_summary_
    # ! Do the unzip process.
    # ? This is only unzip the .zip file, not the .tar.gz file.
    # ? After the files been unziped the .zip file will be deleted.

    Args:
        source (string): The absolute path of the .tar.gz file.
    """    
    files = os.listdir(source)
    
    for file in files:
        file_path = os.path.join(source, file)
        if os.path.isfile(file_path) and file.endswith(".zip"):
            extract_path = os.path.splitext(file_path)[0]
            try:
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)
            except zipfile.BadZipFile:
                print("BadZipFile: " + file_path)
            finally:
                os.remove(file_path)
    
    for item in os.listdir(source):
        item_path = os.path.join(source, item)
        if os.path.isdir(item_path):
            for subitem in os.listdir(item_path):
                subitem_path = os.path.join(item_path, subitem)
                shutil.move(subitem_path, source)
            os.removedirs(item_path)

def untar_gz(source) -> None:
    """_summary_
    # ! Decompress the tar.gz file
    # ? After the files been decompressed the .tar.gz file will be deleted.

    Args:
        source (string): Absolute path of the folder that contain the .tar.gz file.
    """    
    # print(type(source))
    # print(type(os.listdir(source)))
    # testing = os.listdir(source)
    # for i in range(len(testing)):
    #     print(testing[i])
    file_path = os.path.join(source, os.listdir(source)[0])
    # print(file_path)
    with tarfile.open(file_path, "r:gz") as tar:
        tar.extractall(source)
    send2trash.send2trash(file_path)

def move_folder(source_folder, destination, delete) -> None:
    """_summary_
    # ! Move the folder from source to destination.
    # ? If the user want to delete all the previous log file, the program will first move all the file or folders to the trash
    
    Args:
        source_folder (string): _description_
        destination (string): _description_
    """    
    if delete == "y":
        send2trash.send2trash(destination)
    # shutil.move(source_folder, destination)
    folder_name = os.path.basename(source_folder)
    destination_path = os.path.join(destination, folder_name)
    shutil.move(source_folder, destination_path)

# def get_CarID(CarID_source, path_source) -> list:
#     num_CarID = len(path_source)

def formatter(source) -> None:
    """_summary_
    # ! Change the double space into single space.

    Args:
        source (string): The absolute path of the folder.
    """    
    files = os.listdir(source)
    for file in files:
        file_path = os.path.join(source, file)
        with open (file_path, "r", encoding="latin-1") as file:
            context = file.read()
        changed_context = context.replace("  ", " ")
        with open(file_path, "w") as new_file:
            new_file.write(changed_context)


if __name__ == "__main__":
    path = input("Enter the path which contain the .tar.gz compressed file: \n") # ! path is "string" datatype
    analysis_path = input("Enter the path which you want to store the logcat files: \n") # ! analysis_path is "string" datatype
    delete_previous_log = input("Do you want to delete the previous logcat files? (y/n) \n") # ! delete_previous_log is "string" datatype
    CheckTarGZ = CheckTarGZ(path)
    targz_filepath = CheckTarGZ.get_targz_dir() # ! targz_filepath is "list" datatype
    if not CheckTarGZ.targz_exist(): # ? If the file is not exist the program will end.
        print("No .tar.gz file in the path.")
    else:
        CarID = CheckTarGZ.get_targz_sub_root() # ! CarID is "list" datatype
        # CarID = get_CarID(CarID_contained, targz_filepath)
        # for i in range(len(CarID)):
        #     print(CarID[i])
        # for i in range(len(targz_filepath)):
        #     print(targz_filepath[i])
        for i in range (len(targz_filepath)):
            # print(targz_filepath[i])
            untar_gz(targz_filepath[i]) # Decompress the .tar.gz file
            new_path = os.path.join(targz_filepath[i], "log")
            targz_filepath[i] = new_path
            unzip_file(targz_filepath[i])
            temp_file_name = str(CarID[i]) + "logcat"
            mkdir(get_temp_path(targz_filepath[i]), temp_file_name)
            temp_file_path = os.path.join(get_temp_path(targz_filepath[i]), temp_file_name)
            transfer_logcat_files(targz_filepath[i], temp_file_path) # All the logcat files will be transferred to the temp folder.
            formatter(temp_file_path)
            move_folder(temp_file_path, analysis_path, delete_previous_log) # Move the temp folder to the analysis path.
            print(f"Finish dealing with the CarID: {CarID[i]}")
        print("\n")
        print("Complete!")
