import sys
from PyQt4 import QtGui

class UserCard (QtGui.QWidget):
    def __init__ (self, parent = None):
        super(UserCard, self).__init__(parent)
        self.textContainer = QtGui.QVBoxLayout()
        self.nicknameLabel    = QtGui.QLabel()
        self.usernameLabel  = QtGui.QLabel()
        self.passwordLabel = QtGui.QLabel()
        self.textContainer.addWidget(self.nicknameLabel)
        self.textContainer.addWidget(self.usernameLabel)
        self.textContainer.addWidget(self.passwordLabel)
        self.containerLayout  = QtGui.QHBoxLayout()
        self.containerLayout.addLayout(self.textContainer, 1)
        self.setLayout(self.containerLayout)

    def setNickname (self, text):
        self.nicknameLabel.setText(text)
        font = QtGui.QFont('Trebuchet MS', 16)
        self.nicknameLabel.setFont(font)

    def setUsername (self, text):
        self.usernameLabel.setText(text)
        font = QtGui.QFont('Lucida Sans', 9)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setStyleSheet("QLabel {color:grey}")

    def setPassword(self,text):
        self.passwordLabel.setText(text)
        font = QtGui.QFont('Lucida Sans', 9)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setStyleSheet("QLabel {color:grey}")

