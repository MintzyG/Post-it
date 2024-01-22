import os

def check_file(path: str) -> bool:
    check_file = os.stat(path).st_size

    if(check_file == 0):
        print("The file is empty.")
        return False
    else:
        print("The file is not empty.")
        return True