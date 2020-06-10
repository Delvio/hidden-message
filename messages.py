import os

def change_files_names():
    """
        this function gets all the names on the pictures folder and removes
        the numbers form their names
    """
    #list all the file names
    list_of_files = os.listdir("pictures/")
    print(list_of_files)

    #change each file name
    for file in list_of_files:
        translation_table = str.maketrans("0123456789", "          ", "0123456789")
        os.rename(os.getcwd() + "/pictures/" + file, os.getcwd() + "/pictures/" + file.translate(translation_table))
        print("Renamed file %s to %s" % (file, file.translate(translation_table)))


change_files_names()