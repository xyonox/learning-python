import os
import shutil
from pathlib import Path

docpath = "C:\\Users\\carlf\\Documents\\"


#function
def clean(path):
    list_dir = os.listdir(path)
    print(list_dir)

    ## create if not exists
    audio = os.path.join(path, "audios")
    video = os.path.join(path, "videos")
    notes = os.path.join(path, "notes")
    pics = os.path.join(path, "pics")
    other = os.path.join(path, "other")

    for directory in [audio, video, notes, pics, other]:
        if not os.path.exists(directory):
            os.makedirs(directory)

    # move files
    for x in list_dir:
        src_path = os.path.join(path, x)

        if not os.path.isfile(src_path):
            continue  # skip dir

        if x.endswith((".mp3", ".wav", ".m4a", ".aac", ".ogg", ".aiff", ".aif", ".wma")):
            shutil.move(src_path, audio)
        elif x.endswith((".mp4", ".avi", ".mov", ".webm")):
            shutil.move(src_path, video)
        elif x.endswith((".txt", ".java", ".py", ".pdf")):
            shutil.move(src_path, notes)
        elif x.endswith((".jpg", ".jpeg", ".png", ".webp")):
            shutil.move(src_path, pics)
        else:
            shutil.move(src_path, other)


if __name__ == "__main__":
    clean(docpath)
