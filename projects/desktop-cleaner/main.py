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
    user_folder = os.path.expanduser("~")
    documents_folder = os.path.join(user_folder, "Documents")
    desktop_folder = os.path.join(user_folder, "Desktop")
    while True:
        print("documents(1), Desktop(2) or own folder(3)")
        i1 = input()
        if i1 == "1":
            clean(documents_folder)
        elif i1 == "2":
            clean(documents_folder)
        elif i1 == "3":
            d = input("Path: ")
            if not os.path.exists(d) or not os.path.isdir(d):
                print("not found or is no folder")
            else:
                clean(d)
        else:
            print("brooo 1,2 or 3!")
