import os
import filecmp
import difflib

def comp_files(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        content1 = f1.read().splitlines()
        content2 = f2.read().splitlines()

    differ = difflib.Differ()
    differences = list(differ.compare(content1, content2))

    return differences

def main():
    path = "this is the path"  
    files = [f for f in os.listdir(path) if f.endswith('.txt')]

    for i, file1 in enumerate(file):
        for archivo2 in files[i+1:]:
            print(f"Comparing {file1} and {file2}")
            diff = comp_files(os.path.join(path, file1), os.path.join(path, file2))

            if diff:
                print("Diff found:")
                for line in diff:
                    print(line)
            else:
                print("Equal files")
            print("\n")

if __name__ == '__main__':
    main()

