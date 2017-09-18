import sys
from PyQt4 import QtGui,QtCore

class UserInfoDialog(QtGui.QDialog):
    ADD_USER = 1
    EDIT_USER = 2
    def __init__(self,add_or_edit,user=None):
        super(UserInfoDialog, self).__init__()
        self.add_or_edit = add_or_edit
        self.initUI(add_or_edit,user)

    def initUI(self,add_or_edit,user=None):
        self.hbox = QtGui.QHBoxLayout()
        self.userInfoLabel = QtGui.QLabel("User Info")
        self.userInfoLabel.setStyleSheet("font-size:16px")
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.userInfoLabel)
        self.hbox.addStretch(1)

        self.formLayout = QtGui.QFormLayout()
        self.usernameEdit = QtGui.QLineEdit(self)
        self.passwordEdit = QtGui.QLineEdit(self)
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.nicknameEdit = QtGui.QLineEdit(self)

        self.formLayout.addRow('Username: ',self.usernameEdit)
        self.formLayout.addRow('Password: ',self.passwordEdit)
        self.formLayout.addRow('Nickname: ',self.nicknameEdit)
        self.formLayout.setSpacing(10)
        self.formLayout.setMargin(20)

        self.buttons = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Save|QtGui.QDialogButtonBox.Cancel,QtCore.Qt.Horizontal,self)

        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        self.parentLayout = QtGui.QVBoxLayout()
        self.parentLayout.addLayout(self.hbox)
        self.parentLayout.addLayout(self.formLayout)
        self.parentLayout.addWidget(self.buttons)
        self.setLayout(self.parentLayout)

        if add_or_edit == UserInfoDialog.ADD_USER:
            print "Add user dialog"
            self.setWindowTitle("Add new user")
        else:
            print "Edit user dialog"
            self.setWindowTitle("Edit user")
            if user is not None:
                print "User info: ("+user.username+","+user.password+","+user.nickname+")"
                self.usernameEdit.setText(user.username)
                self.passwordEdit.setText(user.password)
                self.nicknameEdit.setText(user.nickname)

    def get_user_info(self):
        username = self.usernameEdit.text()
        password = self.passwordEdit.text()
        nickname = self.nicknameEdit.text()

        from users import User
        user = User.User(str(username),str(password),str(nickname))
        return user

    @staticmethod
    def addUser():
        dialog = UserInfoDialog(UserInfoDialog.ADD_USER)
        result = dialog.exec_()
        user = dialog.get_user_info()
        return (result == QtGui.QDialog.Accepted,user)

    @staticmethod
    def updateUser(user):
        dialog = UserInfoDialog(UserInfoDialog.EDIT_USER,user)
        result = dialog.exec_()
        user = dialog.get_user_info()
        return (result == QtGui.QDialog.Accepted,user)