#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtMultimedia, uic, QtCore
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QLabel, QFileDialog

from db import to_binary, products, product_types, cart


class SelectProductDialog(QDialog):
    """
    Product selecting class, inherits from :class: QDialog
    Creates a Select Product window

    :param parent: Responsible for assigning the parent window, defaults to None
    :type parent: class
    :param image: Product's image
    :type image: bytes
    :param description: Product's description
    :type description: str
    """

    def __init__(self, parent=None, image: bytes = None, description: str = None, price: int = None):
        """
        Constructor method
        """

        super().__init__()
        uic.loadUi('ui_templates/SelectProductDialog.ui', self)
        self.setWindowIcon(QtGui.QIcon('src/shopping-cart.png'))
        self.cancelButton.clicked.connect(self.close)

        self.pic = QtGui.QPixmap()
        self.pic.loadFromData(image)

        self.productDescription.setText(description)

        self.setImage(self.pic)

    def setImage(self, image: bytes) -> None:
        self.Image.setPixmap(image)