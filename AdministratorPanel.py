#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtMultimedia, uic, QtCore
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QLabel

from AddProductDialog import AddProductDialog
from AddCategoryDialog import AddCategoryDialog


class AdministratorPanel(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('ui_templates/AdministratorPanel.ui', self)

        self.setWindowIcon(QtGui.QIcon('src/admin.png'))

        self.addProductButton.clicked.connect(self.addProduct)
        self.addCategoryButton.clicked.connect(self.addCategory)
        self.cancelButton.clicked.connect(self.close)

    def addCategory(self):
        add = AddCategoryDialog(self)
        add.exec_()

    def addProduct(self):
        add = AddProductDialog(self)
        add.exec_()