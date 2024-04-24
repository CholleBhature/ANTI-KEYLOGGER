import os
import numpy as np
import pandas as pd
import seaborn as sns

def find_files_with_keywords(root_dir, keywords):
    found_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if any(keyword in content for keyword in keywords):
                    found_files.append((file_path, content))
    return found_files

def main():
    root_dir = input("Enter the root directory to search: ")
    keywords = input("Enter specific keywords separated by comma: ").split(',')
    
    found_files = find_files_with_keywords(root_dir, keywords)
    
    if found_files:
        print("Files containing the specified keywords:")
        for file_path, _ in found_files:
            print(file_path)
    else:
        print("No files containing the specified keywords were found.")

if __name__ == "__main__":
    main()
