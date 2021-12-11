#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtMultimedia, uic, QtCore
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QLabel


class ShoppingCart(QDialog):
    """
    Shopping cart class, inherits from :class: QDialog
    Creates a shopping cart window

    :param parent: Responsible for assigning the parent window, defaults to None
    :type parent: class
    """

    def __init__(self, parent=None):
        """
        Constructor method
        """

        super().__init__()
        uic.loadUi('ui_templates/ShoppingCart.ui', self)

        self.setWindowIcon(QtGui.QIcon('src/shopping-cart.png'))

        self.cancelButton.clicked.connect(self.close)

    def clearCart(self) -> None:
        """
        Method that empties the shopping cart

        :return: None
        :rtype: None
        """

        pass
