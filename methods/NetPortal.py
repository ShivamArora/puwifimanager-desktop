import requests

status = None
msg = None

def login_net_portal(username,password,session):
    URL = "http://netportal.pu.ac.in/chklogin.php"
    params = {
        "loginid":username,
        "passwd":password
    }
    response =  session.post(url=URL,data=params)

    if response.url == "http://netportal.pu.ac.in/candidate.php":
        print "Login to Netportal successful!"
        return 1
    else:
        print "Unable to login Netportal!"
        return 0

def logout_net_portal(session):
    response = session.get(url="http://netportal.pu.ac.in/logout.php")
    print "Logged out successfully!"
    print response.status_code
    print response.url

def change_password(username,password,new_password):
    with requests.Session() as session:
        status = login_net_portal(username,password,session)
        if status == 0:
            msg = "Unable to login using the saved credentials!\n" \
                  "Make sure you have saved the correct username and password!"
            return status,msg

        params = {
            "oldpass":password,
            "passwd":new_password
        }
        #response = r.get("http://netportal.pu.ac.in/change-password.php")
        #print response.url
        response = session.post(url="http://netportal.pu.ac.in/change-password_proc.php",data=params)
        #print response
        #print response.status_code
        #print response.url
        #print response.text

        if response.url == "http://netportal.pu.ac.in/candidate.php?err=ps1":
            status = 1
            msg = "Password changed successfully!"
            print msg
        else:
            status = 0
            msg = "Password change unsuccessful!"
            print msg

            error_start = response.text.find("<div class=\"err\">")
            error_end = response.text.find("</div>",error_start+1)
            error = response.text[error_start+17:error_end]
            print error

        logout_net_portal(session)
        return status,msg