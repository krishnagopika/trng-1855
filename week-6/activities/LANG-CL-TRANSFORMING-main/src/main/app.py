from src.main.lab import transform_html, transform_txt, transform_md
import sys
import os

# add ../../resources to the path so we can import from there
sys.path.append(os.path.abspath('../../resources/'))

# Use this program to manually check your work
# Feel free to add more test files to resources/ 
# but keep in mind the tests are structured around the
# files already in resources/ (index.html, index.md, index.txt)
if __name__ == '__main__':
    if len(sys.argv) > 1:
        filen = sys.argv[1]
    else:
        filen = input("Enter file name: ").strip()
        if filen[0:10] != 'resources/':
            filen = 'resources/' + filen

    L = filen.split(".")
    if L[-1] == "html":
        print(transform_html(filen))
    elif L[-1] == "md":
        print(transform_md(filen))
    elif L[-1] == "txt":
        print(transform_txt(filen))
    else:
        print("Invalid file type")
