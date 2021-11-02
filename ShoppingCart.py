#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtMultimedia, uic, QtCore
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QLabel


class ShoppingCart(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('ui_templates/ShoppingCart.ui', self)

        self.setWindowIcon(QtGui.QIcon('src/shopping-cart.png'))

        self.cancelButton.clicked.connect(self.close)

    def clearCart(self):
        pass