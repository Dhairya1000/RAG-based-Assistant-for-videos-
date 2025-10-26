import os 
import subprocess 
files = os.listdir("videos")
for file in files:
    tutorial_no = file.split(".")[0].split(" #")[1]
    file_name = file.split("_")[0]
    print(tutorial_no , file_name)
    subprocess.run([
        "ffmpeg",
        "-i", os.path.join("videos", file),
        os.path.join("audios", f"{tutorial_no}_{file_name}.mp3")
    ])


