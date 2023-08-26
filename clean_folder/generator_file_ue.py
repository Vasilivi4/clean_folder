import os

formats = {
    "image": ["JPEG", "PNG", "JPG", "SVG"],
    "video": ["AVI", "MP4", "MOV", "MKV"],
    "document": ["DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"],
    "audio": ["MP3", "OGG", "WAV", "AMR"],
    # "archive": ["ZIP", "GZ", "TAR"],
}


def generate_empty_files_ue(output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for category, ext_list in formats.items():
        for ext in ext_list:
            filename = os.path.join(output_path, f"No_name_file.{ext.lower()}")
            with open(filename, "wb") as f:
                pass
            print(f"Generated {filename} in {category} category.")
