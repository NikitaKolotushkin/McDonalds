#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtMultimedia, uic, QtCore
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QLabel, QFileDialog

from db import to_binary, products, product_types


class AddProductDialog(QDialog):
    """
    Product adding class, inherits from :class: QDialog
    Creates a Add Product window

    :param parent: Responsible for assigning the parent window, defaults to None
    :type parent: class
    """

    def __init__(self, parent=None):
        """
        Constructor method
        """

        super().__init__()
        self.file = ''
        uic.loadUi('ui_templates/AddProductDialog.ui', self)

        self.setWindowIcon(QtGui.QIcon('src/admin.png'))

        self.addProductButton.clicked.connect(self.addProduct)
        self.selectImageButton.clicked.connect(self.selectImage)
        self.cancelButton.clicked.connect(self.close)
        [self.productTypesList.addItem(type_[1]) for type_ in product_types.getData()]

    def selectImage(self) -> None:
        """
        Opens a dialog box for finding an image on a computer

        :return: None
        :rtype: None
        """

        filename, _ = QFileDialog.getOpenFileName(
            self, "Выберите изображение", "", "Image Files (*.jpg *.png *.jpeg *.svg)")
        self.imageName.setText(filename if filename else '')
        self.file = filename if filename else self.file

    def addProduct(self) -> None:
        """
        Adds a product to the database

        :return: None
        :rtype: None
        """

        if self.imageName != '' and self.productNameInput.text().strip() != '' and \
                self.productDescriptionInput.text().strip() != '' and \
                self.productTypesList.currentText() != 'Не выбрано':
            products.add(
                to_binary(self.file),
                self.productNameInput.text(),
                self.productDescriptionInput.text(),
                self.productTypesList.currentText(),
                float(self.priceInput.value()),)
            self.close()
