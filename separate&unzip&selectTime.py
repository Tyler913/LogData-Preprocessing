import separate
import unzip
import dirToFile
import extractFile

if __name__ == '__main__':
    search_keywords = ['logcat']
    source_directory = r'C:\Users\Administrator\Desktop\AnalysisLog\Test02\log'
    destination_directory = r'C:\Users\Administrator\Desktop\AnalysisLog\Test02\Temp'
    fina_dir = r'C:\Users\Administrator\Desktop\AnalysisLog\Test02\NeedAnalysis'
    separate.classify_files(source_directory, destination_directory, search_keywords)
    unzip.unzip_files(r'C:\Users\Administrator\Desktop\AnalysisLog\Temp')
    dirToFile.dirToFile(destination_directory, destination_directory)
    extractFile.transfer(destination_directory, fina_dir, '08:00:10.596', '08:00:10.597')