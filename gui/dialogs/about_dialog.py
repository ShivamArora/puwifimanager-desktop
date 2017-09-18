from PyQt4 import QtGui

class AboutDialog(QtGui.QDialog):
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.initUI()

    def initUI(self):
        from constants import constants
        self.setWindowTitle('About Us')
        self.containerLayout = QtGui.QVBoxLayout()

        self.iconContainer = QtGui.QHBoxLayout()
        self.productIcon = QtGui.QLabel('icon')
        self.iconContainer.addStretch(1)
        self.iconContainer.addWidget(self.productIcon)
        self.iconContainer.addStretch(1)

        self.formLayout = QtGui.QFormLayout()

        self.developerLabel = QtGui.QLabel('Shivam Arora')
        self.emailLabel = QtGui.QLabel('email.shivamarora@gmail.com')
        self.productWebsiteLabel = QtGui.QLabel("<a href='https://productpage.github.io'>https://productpage.github.io</a>")

        self.formLayout.addRow('Version: ', QtGui.QLabel(constants.VERSION_NUMBER))
        self.formLayout.addRow('Developed By: ',self.developerLabel)
        self.formLayout.addRow('Developer email: ',self.emailLabel)
        self.formLayout.addRow('Product Website: ',self.productWebsiteLabel)

        self.formLayout.setMargin(25)
        self.containerLayout.addLayout(self.iconContainer)
        self.containerLayout.addLayout(self.formLayout)

        self.setLayout(self.containerLayout)

