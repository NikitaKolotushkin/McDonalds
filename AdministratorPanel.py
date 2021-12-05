#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtMultimedia, uic, QtCore
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QLabel

from AddProductDialog import *


class AdministratorPanel(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('ui_templates/AdministratorPanel.ui', self)

        self.setWindowIcon(QtGui.QIcon('src/admin.png'))

        self.addProductButton.clicked.connect(self.openProductAdding)
        self.cancelButton.clicked.connect(self.close)

    def openProductAdding(self):
        addProduct = AddProductDialog()
        addProduct.exec_()