import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")  # cls for Windows clear for Linux


def cleanFolder(folder):
    files_list = findAllFiles(folder)
    if not os.path.exists(folder+"/Clean_Up"):
        os.mkdir(folder+"/Clean_Up")
        print('Made Clean Up Folder')

    for file_type in getAllFileTypes(files_list):
        directory = "All " + file_type.upper() + " Files"
        path = os.path.join(folder+"/Clean_Up", directory)
        if not os.path.exists(path):
            os.mkdir(path)
            print("Directory '%s' created" % directory)
        for file in files_list:
            current_file_type = os.path.splitext(file)[-1]
            if current_file_type == file_type:
                os.rename(folder + "/" + file, path + "/" + file)


def findAllFiles(folder) -> list:
    all_Files_list = []
    for path in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, path)):
            all_Files_list.append(path)
    return all_Files_list


def getAllFileTypes(files: list) -> list:
    file_types = []
    for file in files:
        file_type = os.path.splitext(file)[-1]
        if file_type not in file_types:
            file_types.append(file_type)
    return file_types


def main():
    clear()
    while True:
        user_path = input("Input full path to Folder that needs Cleaning > ")
        if os.path.exists(user_path):
            cleanFolder(user_path)
            print(f'{user_path} has been Cleaned')
            break
        else:
            print('Path does not exist')


if __name__ == "__main__":
    main()
