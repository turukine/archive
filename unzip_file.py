import zipfile
import os
def unzip_file(zip_path, extract_to="."):
    """
    Распаковывает ZIP-архив.
    
    :param zip_path: Путь к ZIP-файлу.
    :param extract_to: Папка для распаковки (по умолчанию — текущая).
    """
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_to)
    
    print(f"Файлы из {zip_path} распакованы в {extract_to}")

# Пример использования
unzip_file("archive.zip", "extracted_files")