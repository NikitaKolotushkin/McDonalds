#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import sys

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtMultimedia, uic, QtCore
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QLabel, QMessageBox

from db import products, product_types, cart


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
        self.total_price = 0

        self.setWindowIcon(QtGui.QIcon('src/shopping-cart.png'))

        self.cancelButton.clicked.connect(self.close)
        self.clearCartButton.clicked.connect(self.clearCart)
        self.orderButton.clicked.connect(self.order)

        for product in cart.getData():
            self.listWidget.addItem(f'{product[1]}, {product[2]} шт.')
            self.total_price += int(product[3]) * float(product[2])

        self.totalPrice.setText(f'Итого: {self.total_price} руб.')

    def clearCart(self) -> None:
        """
        Method that empties the shopping cart

        :return: None
        :rtype: None
        """

        cart.clearTable()
        self.close()

    def order(self) -> None:
        """

        """
        if len(cart.getData()) > 0:

            with open('receipt.txt', mode='w+', encoding='utf8') as f:
                price = 0
                f.write(f'\tЧЕК\n{datetime.datetime.now()}\n\n')
                for data in cart.getData():
                    f.write(f'{data[1]} x {data[2]} - {data[2] * data[3]} руб.\n')
                    price += data[3] * data[2]
                f.write(f'\n\tИтого: {float(price)} руб.')
                f.close()
            self.showOrderMessage()

    def showOrderMessage(self) -> None:
        msg = QMessageBox()
        msg.setWindowTitle('Информация о заказе')
        msg.setWindowIcon(QtGui.QIcon('src/logo.png'))
        msg.setText('Ваш заказ успешно оформлен!')
        msg.exec_()
        self.close()