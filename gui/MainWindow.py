from PyQt4 import QtCore,QtGui
from database import usersdb
from gui.dialogs.dialog_userinfo import UserInfoDialog
from gui.dialogs import InfoDialog
from gui.listitem import ListItem
from gui.usercard import *

minimizeToSystemTray = True

class MainWindow(QtGui.QMainWindow):
    logged_in_user = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.initSystemTray()

    def initUI(window):
        #Setup menu bar
        window.setupMenuBar()

        #Setup toolbar
        window.setupToolbar()

        #Setup userlist
        window.setupUserList()

        #Setup user_buttons
        window.setupUserButtons()

        #Final layout
        window.finalLayout()

    def initSystemTray(self):
        self.systemTrayIcon = QtGui.QSystemTrayIcon(self)
        self.systemTrayIcon.setIcon(QtGui.QIcon.fromTheme('face-smile'))
        self.systemTrayIcon.setVisible(True)
        self.systemTrayIcon.activated.connect(self.onSystemTrayActivated)

        context_menu = QtGui.QMenu(self)
        self.showAction = context_menu.addAction("Show")
        self.exitAction = context_menu.addAction("Exit")

        self.showAction.triggered.connect(self.show)
        self.exitAction.triggered.connect(self.exit)

        self.systemTrayIcon.setContextMenu(context_menu)

    def closeEvent(self, event):
        if minimizeToSystemTray:
            event.ignore()
            self.hide()
            self.systemTrayIcon.showMessage('PU Wifi Manager','Running in the background!!')

    def setupMenuBar(window):
        menu_bar = window.menuBar()

        file_menu = menu_bar.addMenu('&File')

        action_add_new = QtGui.QAction(QtGui.QIcon('add-user.png'), '&Add new', window)
        action_add_new.setShortcut('Ctrl+A')
        action_add_new.triggered.connect(window.add_user)

        file_menu.addAction(action_add_new)

        action_logout = QtGui.QAction(QtGui.QIcon('logout.png'), '&Logout', window)
        action_logout.setShortcut('Ctrl+L')
        action_logout.triggered.connect(window.logout_user)

        file_menu.addAction(action_logout)

        action_exit = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', window)
        action_exit.setShortcut('Ctrl+Q')
        action_exit.triggered.connect(window.exit)

        file_menu.addAction(action_exit)

        help_menu = menu_bar.addMenu('&Help')
        action_check_updates = QtGui.QAction(QtGui.QIcon('updates.png'),'Check for updates',window)
        action_check_updates.setShortcut('Ctrl+U')
        action_check_updates.triggered.connect(window.check_for_updates)
        help_menu.addAction(action_check_updates)

        action_about = QtGui.QAction(QtGui.QIcon('about.png'),'About Us',window)
        action_about.setShortcut('Ctrl+I')
        action_about.triggered.connect(window.show_about_dialog)
        help_menu.addAction(action_about)

    def setupToolbar(window):
        window.toolbar = QtGui.QToolBar()

        icon = QtGui.QIcon('add_user.png')
        icon = icon.fromTheme("contact-add")

        add_user_Action = QtGui.QAction(icon, 'Add User', window)
        add_user_Action.triggered.connect(window.add_user)

        window.toolbar.addAction(add_user_Action)

        edit_user_Action = QtGui.QAction(icon,'Edit User',window)
        edit_user_Action.setShortcut('Ctrl+E')
        edit_user_Action.triggered.connect(window.edit_user)

        window.toolbar.addAction(edit_user_Action)

        action_logout = QtGui.QAction(QtGui.QIcon('logout.png'),'Logout',window)

        window.toolbar.addAction(action_logout)

        window.addToolBar(QtCore.Qt.BottomToolBarArea, window.toolbar)

    def setupUserList(window):
        # Create QListWidget
        window.listWidget = QtGui.QListWidget(window)
        userlist = usersdb.get_all_users()
        if userlist is not None:
            for user in userlist:
                # Create UserCardWidget
                usercard = UserCard()
                usercard.setNickname(user.nickname)
                usercard.setUsername(user.username)
                usercard.setPassword(user.password)

                # Create QListWidgetItem
                listItem = ListItem(window.listWidget,user.username)
                # Set size hint
                listItem.setSizeHint(usercard.sizeHint())
                # Add QListWidgetItem into QListWidget
                window.listWidget.addItem(listItem)

                window.listWidget.setItemWidget(listItem, usercard)
            #return window.listWidget

    def setupUserButtons(window):
        window.loginBtn = QtGui.QPushButton("Login")
        window.logoutBtn = QtGui.QPushButton("Logout")
        window.changePasswordBtn = QtGui.QPushButton("Change Password")
        window.removeUserBtn = QtGui.QPushButton("Remove User")

        window.btnsContainer = QtGui.QVBoxLayout()
        window.btnsContainer.addWidget(window.loginBtn)
        window.btnsContainer.addStretch(1)
        window.btnsContainer.addWidget(window.changePasswordBtn)
        window.btnsContainer.addStretch(1)
        window.btnsContainer.addWidget(window.logoutBtn)
        window.btnsContainer.addStretch(1)
        window.btnsContainer.addWidget(window.removeUserBtn)

        window.loginBtn.setSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        window.loginBtn.setStyleSheet("padding:20px; font-size:14px;")
        window.logoutBtn.setStyleSheet("padding:20px; font-size: 14px;")
        window.changePasswordBtn.setStyleSheet("padding:20px; font-size:14px;")
        window.removeUserBtn.setStyleSheet("padding:20px;")

        window.loginBtn.clicked.connect(window.login_user)
        window.logoutBtn.clicked.connect(window.logout_user)
        window.changePasswordBtn.clicked.connect(window.change_password_user)
        window.removeUserBtn.clicked.connect(window.remove_user)

    def printSize(self):
        print self.size()

    def finalLayout(window):
        parentLayout = QtGui.QVBoxLayout()
        window.statusLabel = QtGui.QLabel("Logged in user: ")
        window.statusLabel.setStyleSheet("margin-bottom: 10px;")
        parentLayout.addWidget(window.statusLabel)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(window.listWidget, 0)
        hbox.addLayout(window.btnsContainer, 0)

        parentLayout.addLayout(hbox)
        window.center()

        widget = QtGui.QWidget(window)
        widget.setLayout(parentLayout)
        widget.resize(widget.sizeHint())
        window.setCentralWidget(widget)
        window.resize(620,420)

        #QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
        #for key in QtGui.QStyleFactory.keys():
        #    print key

    def center(window):
        rect = window.frameGeometry()
        screen_resolution = QtGui.QDesktopWidget().availableGeometry()
        center_point = screen_resolution.center()
        rect.moveCenter(center_point)
        window.move(rect.topLeft())

    def exit(self):
        QtCore.QCoreApplication.exit(0)

    def update_logged_in_user(self):
        self.statusLabel.setText('Logged in user: ' + MainWindow.logged_in_user)

    def add_user(self):
        result,user = UserInfoDialog.addUser()
        if result == True:
            status,msg = usersdb.add_user(user)
            if status == 1:
                self.add_user_to_list(user)
                InfoDialog.showMessage(msg)
            else:
                InfoDialog.showError(msg)

    def add_user_to_list(self,user):
        usercard = UserCard()
        usercard.setUsername(user.username)
        usercard.setPassword(user.password)
        usercard.setNickname(user.nickname)

        listItem = ListItem(self.listWidget,user.username)
        # Set size hint
        listItem.setSizeHint(usercard.sizeHint())
        self.listWidget.addItem(listItem)
        self.listWidget.setItemWidget(listItem,usercard)

    def updateListItem(self,listItem):
        user = usersdb.get_user(listItem.username)
        usercard = UserCard()
        usercard.setUsername(user.username)
        usercard.setPassword(user.password)
        usercard.setNickname(user.nickname)
        self.listWidget.setItemWidget(listItem,usercard)

    def edit_user(self):
        print "Edit user clicked"
        listItem = self.listWidget.currentItem()
        selected_user = usersdb.get_user(listItem.username)

        result,user = UserInfoDialog.updateUser(selected_user)
        print result

        usersdb.update_user(user)
        print user.info()
        usercard = UserCard()
        usercard.setUsername(user.username)
        usercard.setPassword(user.password)
        usercard.setNickname(user.nickname)
        self.listWidget.setItemWidget(listItem,usercard)

    def remove_user(self):
        print "Remove user clicked"
        result = InfoDialog.showConfirmationDialog('Are you sure you want to delete the selected user?')

        if result == QtGui.QMessageBox.Yes:
            listItem = self.listWidget.currentItem()
            if listItem is None:
                InfoDialog.showError('Please select a user first!')
                return
            user = usersdb.get_user(listItem.username)
            status, msg = usersdb.delete_user(user)
            if status == 1:
                self.listWidget.takeItem(self.listWidget.currentRow())
                InfoDialog.showMessage(msg)
            else:
                InfoDialog.showError(msg)

    def login_user(self):
        print "Login user clicked"
        listitem = self.listWidget.currentItem()
        if listitem is None:
            InfoDialog.showError('Please select a user first!')
            return
        user = usersdb.get_user(listitem.username)
        status, msg = user.login()
        if status == 1:
            InfoDialog.showMessage('Login successful!')
            MainWindow.logged_in_user = user.nickname
            self.update_logged_in_user()
        else:
            InfoDialog.showError(msg)

    def logout_user(self):
        print "Logout user clicked"
        listitem = window.listWidget.currentItem()
        if listitem is None:
            from users import User
            user = User.User('','','')
        else:
            user = usersdb.get_user(listitem.username)
        status = user.logout()
        if status == True:
            InfoDialog.showMessage('Logout successful!')
        else:
            InfoDialog.showMessage('Unable to log out!')

    def change_password_user(self):
        print "Change password clicked"
        listitem = self.listWidget.currentItem()
        if listitem is None:
            InfoDialog.showError('Please select a user first!')
            return
        new_password,result = QtGui.QInputDialog.getText(self,'Change Password','Enter new password: ')
        if result:
            user = usersdb.get_user(listitem.username)
            user.change_password(str(new_password))
            InfoDialog.showMessage('Password changed successfully!')
            user.password = new_password
            usersdb.update_user(user)
            self.updateListItem(listitem)

    def show_about_dialog(self):
        from gui.dialogs import about_dialog
        dialog = about_dialog.AboutDialog()
        dialog.exec_()

    def check_for_updates(self):
        print "Checking for updates..."

    @QtCore.pyqtSlot(QtGui.QSystemTrayIcon.ActivationReason)
    def onSystemTrayActivated(self,reason):
        if reason == QtGui.QSystemTrayIcon.DoubleClick:
            if self.isHidden():
                self.show()
            else:
                self.hide()


if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setApplicationName('PU Wifi Manager')
    window = MainWindow()
    window.setWindowTitle("PU Wifi Manager")
    window.show()
    sys.exit(app.exec_())