import os
import shutil
import magic
import threading

source_directory = "D:/File type generator/file"
destination_directory = "D:/File type generator/Recieved"

for file_type in ['PNG', 'MP3', 'JPEG', 'PDF']:
    directory = os.path.join(destination_directory, file_type)
    os.makedirs(directory, exist_ok=True) # Create the destination directories 

def classify_and_move_files():
    while True:
        for filename in os.listdir(source_directory):
            file_path = os.path.join(source_directory, filename)
            if os.path.isfile(file_path):
                file_type, file_extension = get_file_type(file_path)
                if file_type:
                    destination_path = os.path.join(destination_directory, file_type, filename + file_extension)
                    shutil.move(file_path, destination_path)


def get_file_type(file_path):
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)

    if file_type.startswith('image/png'):
        return 'PNG', '.png'
    elif file_type.startswith('audio/mpeg'):
        return 'MP3', '.mp3'
    elif file_type.startswith('image/jpeg'):
        return 'JPEG', '.jpg'
    elif file_type.startswith('application/pdf'):
        return 'PDF', '.pdf'
    else:
        return None

if __name__ == "__main__":
    T1=threading.Thread(target=classify_and_move_files)
    T1.start()
    T1.join()
