import sys
from PyQt4 import QtGui

class Dialog(QtGui.QMessageBox):
    def __init__(self):
        super(Dialog, self).__init__()
        self.setWindowTitle('PU Wifi Manager')


def showMessage(text):
    msgbox = Dialog()
    msgbox.setIcon(QtGui.QMessageBox.Information)
    msgbox.setText(text)
    msgbox.addButton(QtGui.QMessageBox.Ok)

    msgbox.setDefaultButton(QtGui.QMessageBox.Ok)
    result = msgbox.exec_()
    return result

def showError(text):
    msgbox = Dialog()
    msgbox.setIcon(QtGui.QMessageBox.Warning)
    msgbox.setText(text)
    msgbox.addButton(QtGui.QMessageBox.Ok)
    msgbox.setDefaultButton(QtGui.QMessageBox.Ok)
    result = msgbox.exec_()
    return result

def showConfirmationDialog(text):
    msgbox = Dialog()
    msgbox.setIcon(QtGui.QMessageBox.Warning)
    msgbox.setText(text)
    msgbox.addButton(QtGui.QMessageBox.Yes)
    msgbox.addButton(QtGui.QMessageBox.No)
    msgbox.setDefaultButton(QtGui.QMessageBox.No)
    result = msgbox.exec_()
    return result