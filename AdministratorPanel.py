#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtMultimedia, uic, QtCore
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView

from AddProductDialog import AddProductDialog
from AddCategoryDialog import AddCategoryDialog
from db import products, product_types


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

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.horizontalHeader = self.tableWidget.horizontalHeader()
        self.horizontalHeader.resizeSection(0, 85)
        self.horizontalHeader.resizeSection(1, 150)
        self.horizontalHeader.resizeSection(2, 200)
        self.horizontalHeader.resizeSection(3, 200)
        self.horizontalHeader.resizeSection(4, 100)

        self.tableWidget.setRowCount(len(products.getData()))
        for n, category in enumerate(products.getData()):
            product_id = category[0]
            title = category[2]
            description = category[3]
            product_type = category[4]
            price = category[5]

            self.tableWidget.setItem(n, 0, QTableWidgetItem(str(product_id)))
            self.tableWidget.setItem(n, 1, QTableWidgetItem(title))
            self.tableWidget.setItem(n, 2, QTableWidgetItem(description))
            self.tableWidget.setItem(n, 3, QTableWidgetItem(product_type))
            self.tableWidget.setItem(n, 4, QTableWidgetItem(str(price)))

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
