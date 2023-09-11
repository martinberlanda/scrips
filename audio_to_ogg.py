import os
import sys
from pydub import AudioSegment

def get_size(path):
    return os.stat(path).st_size

def convert_to_ogg(folder_path):
    total_files = 0
    converted_files = 0
    space_saved = 0

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            total_files += 1
            file_ext = filename.split('.')[-1].lower()
            if file_ext in ['mp3', 'opus', 'm4a']:
                converted_files += 1
                file_path = os.path.join(root, filename)
                ogg_path = os.path.join(root, filename.rsplit('.', 1)[0] + '.ogg')

                original_size = get_size(file_path)

                print(f"Converting {filename} ...")
                
                if file_ext == 'mp3':
                    audio = AudioSegment.from_mp3(file_path)
                elif file_ext == 'opus':
                    audio = AudioSegment.from_file(file_path, format='ogg', codec='opus')
                elif file_ext == 'm4a':
                    audio = AudioSegment.from_file(file_path, format='m4a')
                audio.export(ogg_path, format="ogg")

                new_size = get_size(ogg_path)

                space_saved += original_size - new_size

                os.remove(file_path)

    print(f"Total number of files found: {total_files}")
    print(f"Number of audio files converted: {converted_files}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_to_ogg.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        if not os.path.isdir(folder_path):
            print(f"The provided path '{folder_path}' is not a directory.")
        else:
            convert_to_ogg(folder_path)