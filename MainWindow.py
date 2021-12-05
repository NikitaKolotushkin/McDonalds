#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtMultimedia, uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

from db import to_binary, products, product_types
from AdministratorPanel import AdministratorPanel
from ShoppingCart import ShoppingCart


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui_templates/MainWindow.ui', self)

        self.setWindowIcon(QtGui.QIcon('src/logo.png'))

        self.pushButton.clicked.connect(self.openCart)
        self.productManagementAction.triggered.connect(self.openAdminPanel)

    def openCart(self):
        cart = ShoppingCart(self)
        cart.exec_()

    def openAdminPanel(self):
        admin_panel = AdministratorPanel(self)
        admin_panel.exec_()