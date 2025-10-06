import os 
import shutil

def copy_files(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.mkdir(destination_dir)

    for file in os.listdir(source_dir):
        source = os.path.join(source_dir, file)
        destination = os.path.join(destination_dir, file)
        print(f"copy from {source} to {destination}")
        if os.path.isfile(source):
            shutil.copy(source, destination)
        else:
            copy_files(source, destination)