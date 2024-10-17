import os

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

merge(r'C:\Users\Administrator\Desktop\AnalysisLog\Test03\NeedAnalysis', r'C:\Users\Administrator\Desktop\AnalysisLog\Test03\Final_analysis.log')