import os

BASE_DIR = os.path.expanduser('~')
EXTENSIONS_IMAGE = ['jpg', 'gif', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'ico', 'png', 'svg', 'bmp', 'webp', 'tif', 'tiff']
EXTENSIONS_EXEC = ['exe', 'bat', 'cmd', 'msi', 'jar', 'app', 'deb', 'rpm', 'run', 'sh', 'com', 'scr']
EXTENSIONS_AUDIO = ['mp3', 'wav', 'ogg', 'flac']
EXTENSIONS_VIDEO = ['mp4', 'mov', 'avi', 'mkv']
EXTENSIONS_DOCUMENTS = ['doc', 'docx', 'pdf', 'txt', 'ppt', 'pptx', 'xls', 'xlsx']
EXTENSIONS_COMPRESSED = ['zip', 'rar', '7z', 'tar', 'gz']

myMainDir='C:\\mySortedDownloads'
myFolders=['myDownloadedImages','myDownloadedExecutables','myDownloadedAudio','myDownloadedVideo','myDownloadedDocuments','myDownloadedCompressed','myDownloadedOthers']

def categorize_files(directory):
    files = os.listdir(directory)
   

    for file in files:
        source_file_path = os.path.join(directory, file)
        extension = file.split('.')[-1].lower()
        if extension in EXTENSIONS_IMAGE:
            destination_folder = os.path.join(myMainDir, 'myDownloadedImages')
        elif extension in EXTENSIONS_EXEC:
            destination_folder = os.path.join(myMainDir, 'myDownloadedExecutables')
        elif extension in EXTENSIONS_AUDIO:
            destination_folder = os.path.join(myMainDir, 'myDownloadedAudio')
        elif extension in EXTENSIONS_VIDEO:
            destination_folder = os.path.join(myMainDir, 'myDownloadedVideo')
        elif extension in EXTENSIONS_DOCUMENTS:
            destination_folder = os.path.join(myMainDir, 'myDownloadedDocuments')
        elif extension in EXTENSIONS_COMPRESSED:
            destination_folder = os.path.join(myMainDir, 'myDownloadedCompressed')
        else:
            destination_folder = os.path.join(myMainDir, 'myDownloadedOthers')

        destination_file_path = os.path.join(destination_folder, file)
        try:
            os.rename(source_file_path, destination_file_path)
            print(f"Moved {file} to {destination_folder}")
        except OSError as e:
            print(f"Error moving {file}: {e}")

    

def checkFolder(dir):
    if(os.path.exists(dir) == False):
        os.mkdir(dir)

def foldersExist():
    checkFolder(myMainDir)
    for folder in myFolders:
        checkFolder(myMainDir+'\\'+folder)
        

foldersExist()
downloads_directory = os.path.join(BASE_DIR, 'Downloads')
print('Done! Checking folders!')
categorize_files(downloads_directory)
print('Done! Categorizing files!')

