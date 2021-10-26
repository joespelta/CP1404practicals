"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Cleanup file names."""
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    for directory_name, sub_directories, file_names in os.walk('.'):
        print(f"Directory: {directory_name}")
        print(f"Subdirectories: {sub_directories}")
        print(f"Files: {file_names}")
        print(f"Current directory: {os.getcwd()}")
        for file_name in file_names:
            new_name = get_fixed_filename(file_name)
            print(f"Renaming {file_name} to {new_name}")

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)


main()
# demo_walk()
