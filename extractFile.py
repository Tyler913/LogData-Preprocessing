import os
import shutil

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
