import os
from pathlib import Path

# Change this to the exact name of your folder if it's different
folder_name = "miscrits_silhouettes"

def generate_js_array():
    folder_path = Path(folder_name)
    
    # Check if the folder actually exists before trying to read it
    if not folder_path.exists() or not folder_path.is_dir():
        print(f"Error: Could not find a folder named '{folder_name}' in the current directory.")
        return

    miscrit_names = []
    
    # Find all .png files in the folder
    for file in folder_path.glob("*.png"):
        # file.stem gets the name without .png (e.g., "Agnuf_silhouette")
        # .replace() removes the "_silhouette" part
        clean_name = file.stem.replace("_silhouette", "")
        miscrit_names.append(clean_name)
    
    # Sort them alphabetically
    miscrit_names.sort()

    # Print the formatted JavaScript array
    print("const MISCRITS_DATA = [")
    for name in miscrit_names:
        print(f'  "{name}",')
    print("];")

if __name__ == "__main__":
    generate_js_array()