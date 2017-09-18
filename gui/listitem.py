import sys
from PyQt4 import QtGui

class ListItem(QtGui.QListWidgetItem):
    def __init__(self,listWidget,username):
        super(ListItem, self).__init__(listWidget)
        self.username = username