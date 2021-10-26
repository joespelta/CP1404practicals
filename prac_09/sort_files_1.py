import os


def main():
    os.chdir("FilesToSort")
    for file_name in os.listdir('.'):
        if os.path.isdir(file_name):
            continue

        extension = file_name.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        print(f"{extension}/{file_name}")
        os.rename(file_name, f"{extension}/{file_name}")


main()
