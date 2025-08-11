import os
import zipfile
import json

DATA_DIR = "data"
ZIPPED_DIR = "zipped_data"

def zip_json_files(src_dir, dest_dir):
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith(".json"):
                json_path = os.path.join(root, file)

                # Calculate relative path and ensure output folder exists
                rel_path = os.path.relpath(root, src_dir)
                dest_folder = os.path.join(dest_dir, rel_path)
                os.makedirs(dest_folder, exist_ok=True)

                zip_path = os.path.join(dest_folder, os.path.splitext(file)[0] + ".zip")

                # Read and minify JSON
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                minified_json = json.dumps(data, separators=(',', ':'))

                # Create zip with max compression and write minified json
                with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
                    zipf.writestr(file, minified_json)

                print(f"Zipped (minified): {json_path} -> {zip_path}")

if __name__ == "__main__":
    if not os.path.exists(DATA_DIR):
        print(f"Directory '{DATA_DIR}' not found.")
    else:
        zip_json_files(DATA_DIR, ZIPPED_DIR)
