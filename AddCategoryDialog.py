#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtMultimedia, uic, QtCore
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView

from db import to_binary, products, product_types


class AddCategoryDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('ui_templates/AddCategoryDialog.ui', self)

        self.setWindowIcon(QtGui.QIcon('src/admin.png'))

        self.cancelButton.clicked.connect(self.close)
        self.addCategoryButton.clicked.connect(self.addCategory)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.horizontalHeader = self.tableWidget.horizontalHeader()
        self.horizontalHeader.resizeSection(0, 85)
        self.horizontalHeader.resizeSection(1, 320)

        self.updateCategoryList()

    def addCategory(self):
        if self.categoryNameInput.text().strip() != '':
            product_types.add(self.categoryNameInput.text())
            self.updateCategoryList()

    def updateCategoryList(self):
        self.tableWidget.setRowCount(len(product_types.getData()))
        for n, category in enumerate(product_types.getData()):
            id, title = category
            self.tableWidget.setItem(n, 0, QTableWidgetItem(str(id)))
            self.tableWidget.setItem(n, 1, QTableWidgetItem(title))