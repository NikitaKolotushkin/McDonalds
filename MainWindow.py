#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools
import sys

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtMultimedia, uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QListWidget, QListWidgetItem

from db import to_binary, products, product_types, cart
from AdministratorPanel import AdministratorPanel
from SelectProductDialog import SelectProductDialog
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

        self.selectedProduct = 0

        self.openCartButton.clicked.connect(self.openCart)
        self.productManagementAction.triggered.connect(self.openAdminPanel)

        self.createTabs()

    def ProductDialog(self, item):

        product_data = products.getDataByTitle(item.text())
        product_title = product_data[2]
        image = product_data[1]
        description = product_data[3]
        price = product_data[5]

        select = SelectProductDialog(self, image, description, price)

        def addToCart():
            cart.add(product_title, select.spinBox.value(), price)
            select.close()

        select.addProductButton.clicked.connect(addToCart)

        select.exec_()

    def createTabs(self) -> None:
        """

        """

        for category in product_types.getValuesFromColumn('title'):
            self.tab = QListWidget()
            self.tab.move(0, 0)
            self.tab.resize(1283, 600)

            if products.getProductsByCategory(category[0]):
                for product in products.getProductsByCategory(category[0]):
                    self.tab.addItem(product[0])
                self.tabWidget.addTab(self.tab, category[0])

            self.tab.itemClicked.connect(self.ProductDialog)

    def openCart(self) -> None:
        """
        Method that calls the cart window (:class: ShoppingCart)

        :return: None
        :rtype: None
        """

        cart = ShoppingCart(self)
        cart.exec_()

    def openAdminPanel(self) -> None:
        """
        Method that calls the administrator panel window (:class: AdministratorPanel)

        :return: None
        :rtype: None
        """

        admin_panel = AdministratorPanel(self)
        admin_panel.exec_()
