from methods import PULogin
from methods import NetPortal

class User():
    def __init__(self,username,password,nickname):
        self.username = username
        self.password = password
        self.nickname = nickname

    def login(self):
        status,msg = PULogin.login(user= self.username,password=self.password)
        return status,msg

    def logout(self):
        return PULogin.logout()

    def is_logged_in(self):
        PULogin.is_logged_in(user=self.username,password=self.password)

    def change_password(self,new_password):
        NetPortal.change_password(self.username,self.password,new_password)

    def info(self):
        return "Username: ",self.username,"Password: ",self.password,"Nickname: ",self.nickname

if __name__ == '__main__':
    shivam = User("135207", "shivam@#300A", "Shivam Wifi")
    shivam.change_password("shivam@A")
