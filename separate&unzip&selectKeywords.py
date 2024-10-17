import separate
import unzip
import dirToFile
import selectKeyWord

if __name__ == '__main__':
    search_keywords = ['logcat']
    source_directory = r'C:\Users\Administrator\Desktop\AnalysisLog\Test02\log'
    destination_directory = r'C:\Users\Administrator\Desktop\AnalysisLog\Test02\Temp'
    fina_dir = r'C:\Users\Administrator\Desktop\AnalysisLog\Test02\NeedAnalysis'
    separate.classify_files(source_directory, destination_directory, search_keywords)
    unzip.unzip_files(destination_directory)
    dirToFile.dirToFile(destination_directory, destination_directory)
    selectKeyWord.select_words('1297', destination_directory, fina_dir)