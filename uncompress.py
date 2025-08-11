import os
import zipfile

ZIPPED_DIR = "zipped_data"
DATA_DIR = "data"

def unzip_files(src_dir, dest_dir):
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith(".zip"):
                zip_path = os.path.join(root, file)

                # Calculate relative path from zipped_data to preserve structure
                rel_path = os.path.relpath(root, src_dir)
                extract_folder = os.path.join(dest_dir, rel_path)
                os.makedirs(extract_folder, exist_ok=True)

                # Extract all contents of the zip
                with zipfile.ZipFile(zip_path, 'r') as zipf:
                    zipf.extractall(path=extract_folder)

                print(f"Extracted: {zip_path} -> {extract_folder}")

if __name__ == "__main__":
    if not os.path.exists(ZIPPED_DIR):
        print(f"Directory '{ZIPPED_DIR}' not found.")
    else:
        unzip_files(ZIPPED_DIR, DATA_DIR)
