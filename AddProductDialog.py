#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtMultimedia, uic, QtCore
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QLabel

from db import to_binary, products, product_types


class AddProductDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('ui_templates/AddProductDialog.ui', self)

        self.setWindowIcon(QtGui.QIcon('src/admin.png'))

        self.addProductButton.clicked.connect(self.addProduct)

        self.cancelButton.clicked.connect(self.close)

    def addProduct(self):
        if self.imageName != '1' and self.productNameInput.text().strip() != '' and \
                self.productDescriptionInput.text().strip() != '':
            products.add(
                to_binary('admin.png'),
                self.productNameInput.text(),
                self.productDescriptionInput.text(),
                self.productTypesList.currentText(),
                self.priceInput.value(),)
            self.close()
