import zipfile
import os

def zip_files(file_paths, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in file_paths:
            if os.path.isfile(file):
                zipf.write(file, os.path.basename(file))
            elif os.path.isdir(file):
                for root, _, files in os.walk(file):
                    for f in files:
                        file_path = os.path.join(root, f)
                        arcname = os.path.relpath(file_path, os.path.dirname(file))
                        zipf.write(file_path, arcname)
    
    print(f"Архив {output_zip} успешно создан!")

files_to_zip = ["file1.txt", "тест.txt"] 
zip_files(files_to_zip, "archive.zip")
