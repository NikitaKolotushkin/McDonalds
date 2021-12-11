#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtMultimedia, uic, QtCore
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QLabel

from AddProductDialog import AddProductDialog
from AddCategoryDialog import AddCategoryDialog


class AdministratorPanel(QDialog):
    """
    Administrator panel class, inherits from :class: QDialog
    Creates a administrator panel window

    :param parent: Responsible for assigning the parent window, defaults to None
    :type parent: class
    """

    def __init__(self, parent=None):
        """
        Constructor method
        """

        super().__init__()
        uic.loadUi('ui_templates/AdministratorPanel.ui', self)

        self.setWindowIcon(QtGui.QIcon('src/admin.png'))

        self.addProductButton.clicked.connect(self.addProduct)
        self.addCategoryButton.clicked.connect(self.addCategory)
        self.cancelButton.clicked.connect(self.close)

    def addCategory(self) -> None:
        """
        Method that calls the dialog window for adding a product category (:class: AddCategoryDialog)

        :return: None
        :rtype: None
        """

        add = AddCategoryDialog(self)
        add.exec_()

    def addProduct(self) -> None:
        """
        Method that calls the dialog window for adding a product (:class: AddProductDialog)

        :return: None
        :rtype: None
        """

        add = AddProductDialog(self)
        add.exec_()
