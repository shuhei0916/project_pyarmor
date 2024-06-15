import datetime

error_message = "A critical error has occurred in the system. Continued use of the program may result in data loss or system instability.\nPlease contact the program administrator immediately.\nError Code: ERR-5001"

# stimer用の関数
def check_expiration():
    expiration_date = datetime.datetime(2016, 6, 13)
    current_date = datetime.datetime.now()
    if current_date > expiration_date:
        raise Exception("This program has expired and can no longer be used.")



