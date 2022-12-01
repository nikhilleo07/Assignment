"""Function To open a file"""

def open_log_file(file_location)->str:
    """To open a file, common exceptions are handled here"""
    try:
        with open(file_location,encoding="utf-8") as file_handler:
            fstring = file_handler.readlines()
            return fstring
    except IOError as err:
        print(f"IOError was {err}")
    except EOFError as err:
        print(f"End of file error was {err}")
    return None

if __name__ == '__main__':
    print("This module executes as a standalone script")
    INPUTFILE_PATH = str(input("Enter the file to read, example dhcpd.log : "))
    result = open_log_file(INPUTFILE_PATH)
    print(result)
else:
    pass
