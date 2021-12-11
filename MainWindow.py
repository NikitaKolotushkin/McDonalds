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
    """
    Main window class, inherits from :class: QMainWindow
    Creates the main application window
    """

    def __init__(self):
        """
        Constructor method
        """

        super().__init__()
        uic.loadUi('ui_templates/MainWindow.ui', self)

        self.setWindowIcon(QtGui.QIcon('src/logo.png'))

        self.pushButton.clicked.connect(self.openCart)
        self.productManagementAction.triggered.connect(self.openAdminPanel)

    def openCart(self):
        """
        Method that calls the cart window (:class: ShoppingCart)

        :return: None
        :rtype: None
        """

        cart = ShoppingCart(self)
        cart.exec_()

    def openAdminPanel(self):
        """
        Method that calls the administrator panel window (:class: AdministratorPanel)

        :return: None
        :rtype: None
        """

        admin_panel = AdministratorPanel(self)
        admin_panel.exec_()
