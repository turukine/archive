import zipfile
import os
def unzip_file(zip_path, extract_to="."):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_to)
    
    print(f"Файлы из {zip_path} распакованы в {extract_to}")

unzip_file("archive.zip", "extracted_files")
