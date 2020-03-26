# INF322 Python
# Josh Lewis
# Week 7 – Strong Password Regex

def strongPass(password):
    # Import regex module
    import re
    
    # Regex filters on password argument
    lengthRegex = re.compile(r'\w{8,}')
    upperRegex = re.compile(r'[A-Z]+')
    lowerRegex = re.compile(r'[a-z]+')
    digitRegex = re.compile(r'\d+')
    specialRegex = re.compile(r'[#$&+-]+')

    # Five password boolean tests
    if lengthRegex.search(password) == None:
        print("Invalid password. Please check the length and try again!")
        return False
    elif upperRegex.search(password) == None:
        print("Invalid password. Please use at least one uppercase letter and try again!")
        return False
    elif lowerRegex.search(password) == None:
        print("Invalid password. Please use at least one lowercase letter and try again!")
        return False
    elif digitRegex.search(password) == None:
        print("Invalid password. Please use at least one digit and try again!")
        return False
    elif specialRegex.search(password) == None:
        print("Invalid password. Please use #, $, &, +, or - and try again!")
        return False
    else:
        print("Strong password!")
        return True

# Test function
userPass = input()
strongPass(userPass)
