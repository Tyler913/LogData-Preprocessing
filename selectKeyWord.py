import os
import shutil

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
