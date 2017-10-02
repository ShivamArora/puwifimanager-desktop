import requests

status = None
msg = None

def is_logged_in(user, password):
    print "check login"
    URL = "https://securelogin.pu.ac.in/cgi-bin/login"
    params = {
        "cmd": "logout",
        "user": user,
        "password": password}

    response = requests.get(URL, params)

    print response
    #print response.text

    if "User not logged in" in response.text:
        print "User not logged in!"
    else:
        print "User might be logged in!"
        print "Try Relogging in..."
        login(user,password,checking=True)


def login(user=None,password=None,checking=False):
    if user is None and password is None:
        user = raw_input("Enter username:")
        password = raw_input("Enter password:")

    URL = "https://securelogin.pu.ac.in/cgi-bin/login"
    params = {
        "cmd": "logout",
        "user": user,
        "password": password}

    response = requests.post(URL, params)

    print response
    # print response.text
    if response.status_code == 500:
        status = 0
        msg = "User might be logged in!"
        print msg
        is_logged_in(user,password)
        return status,msg

    if "Authentication failed" in response.text:
        if checking is True:
            print "User not logged in!"
        else:
            status = 0
            msg = "Authentication failed!!!"
            print msg
            return status, msg
    elif "External Welcome Page" in response.text:
        status = 1
        msg = "Login successful!"
        print msg
        return status,msg
    else:
        is_logged_in(user, password)
        status = 0
        msg = "Unable to login!"
        print msg
        return status,msg


def logout():
    URL = "https://securelogin.pu.ac.in/cgi-bin/login"
    params = {
        "cmd": "logout"
    }

    response = None
    try:
        response = requests.get(URL, params)
    except requests.exceptions.ConnectionError:
        #check if not connected to PU@Campus
        print "Check for error"
        print "Make sure you have Wifi enabled and connected to PU@Campus."


    print response
    # print response.text

    if response is not None:
        if "Logout Successful" in response.text:
            print "Logout successful!"
            return True
        else:
            print "Unable to logout!"
            return False
    else:
        print "Unable to logout"
        return False


"""
Main code begins here

print "1. Login"
print "2. Logout"
choice = int(raw_input("Enter your choice: "))

if choice == 1:
    login()
elif choice == 2:
    logout()
else:
    print "Wrong choice entered"
"""