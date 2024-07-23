import os
import shutil

# ik is kein desktop hahaha
docpath = "C:\\Users\\carlf\\Documents\\"
def clean(path):
    list_dir = os.listdir(path)
    print(list_dir)

    ## ornder
    audio = path + "audios"

    # sicherstellen das die ordner exestieren
    if not os.path.exists(audio):
        os.makedirs(audio)

    video = path + "videos"

    if not os.path.exists(video):
        os.makedirs(video)

    notes = path + "notes"

    if not os.path.exists(notes):
        os.makedirs(notes)

    pics = path + "pics"

    if not os.path.exists(pics):
        os.makedirs(pics)

    # bewegen der datein
    for x in list_dir:
        if (x.endswith(".mp3") | x.endswith(".wav") | x.endswith(".wav") | x.endswith(".m4a")
                | x.endswith(".aac") | x.endswith(".ogg") | x.endswith(".aiff") | x.endswith(".aif")
                | x.endswith(".wma")):
            src_path = os.path.join(path, x)

            # Vollständiger Pfad zur Zieldatei
            dest_path = os.path.join(audio, x)

            # Verschieben der Datei
            shutil.move(src_path, audio)
        if (x.endswith(".mp4") | x.endswith(".avi") | x.endswith(".mov") | x.endswith(".webm")):
            src_path = os.path.join(path, x)
            dest_path = os.path.join(audio, x)
            shutil.move(src_path, video)
        if (x.endswith(".txt") | x.endswith(".java") | x.endswith(".python") | x.endswith(".pdf")):
            src_path = os.path.join(path, x)
            dest_path = os.path.join(audio, x)
            shutil.move(src_path, notes)
        if (x.endswith(".jpg") | x.endswith(".jpng") | x.endswith(".png") | x.endswith(".webp")):
            src_path = os.path.join(path, x)
            dest_path = os.path.join(audio, x)
            shutil.move(src_path, pics)
    #    if (x.endswith(".mp3") | x.endswith(".wav")) :
    #        src_path = os.path.join(path, x)
    #        dest_path = os.path.join(audio, x)
    #        shutil.move(src_path, audio)

clean(docpath)