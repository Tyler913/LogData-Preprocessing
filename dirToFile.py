import os
import shutil

def dirToFile(source, distination):
    for item in os.listdir(source):
        item_path = os.path.join(source, item)

        if os.path.isdir(item_path):
            for subitem in os.listdir(item_path):
                subitem_path = os.path.join(item_path, subitem)
                shutil.move(subitem_path, distination)
            os.removedirs(item_path)