#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import sqlite3


def to_binary(file: str) -> bytes:
    """
    A function that converts an image file into byte format
    in order to enter it into the database in BLOB format

    :return: Byte representation of the image file
    :rtype: bytes
    """

    with open(file, mode='rb') as f:
        bin_ = f.read()
    return bin_


class Database:
    """
    Parent class that is a stub for creating table classes in a database

    :param db_name: The name of the database to work with
    :type db_name: str
    """

    def __init__(self, db_name: str) -> None:
        """
        Constructor method
        """

        self.con = sqlite3.connect(r'databases/' + f'{db_name}.db')
        self.cur = self.con.cursor()

    def create(self) -> None:
        """
        An empty stub method for creating a table in a database

        :return: None
        :rtype: None
        """

        pass

    def add(self, *args) -> None:
        """
        An empty stub method for adding data to the created table

        :param args: Data entered in the corresponding fields in the database table
        :type args: tuple

        :return: None
        :rtype: None
        """

        pass

    def getData(self) -> list:
        """
        An empty stub method to get all data from the selected table

        :return: List of data from a table
        :rtype: list
        """

        pass


class ProductsTable(Database):
    """
    Product table class, inherited from :class: Database
    """

    def __init__(self):
        """
        Constructor method
        """

        super().__init__('products')

    def create(self):
        """
        Creates a table of products in products.db

        :return: None
        :rtype: None
        """

        self.cur.execute("""CREATE TABLE IF NOT EXISTS products (
                            product_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                            photo BLOB NOT NULL,
                            title TEXT NOT NULL,
                            description TEXT NOT NULL,
                            type INTEGER NOT NULL,
                            price INTEGER NOT NULL,
                            date TEXT NOT NULL,
                            FOREIGN KEY (type) REFERENCES product_types(id))
                        """)

    def add(self, photo: bytes, title: str, description: str, type_: int, price: float):
        """
        Adds one item to the products table

        :param photo: Product photo
        :type photo: bytes
        :param title: The product's name
        :type title: str
        :param description: Product description
        :type description: str
        :param type_: Product type (selected from the product_types table)
        :type type_: int
        :param price: Product price
        :type price: float

        :return: None
        :rtype: None
        """

        self.cur.execute("""INSERT INTO products(photo, title, description, type, price, date)
                            VALUES(?, ?, ?, ?, ?, ?)
                        """, (photo, title, description, type_, price, datetime.datetime.now()))
        self.con.commit()


class ProductTypesTable(Database):
    """
    Product types table class, inherited from :class: Database
    """

    def __init__(self):
        """
        Constructor method
        """

        super().__init__('products')

    def create(self):
        """
        Creates a table of product types in products.db

        :return: None
        :rtype: None
        """

        self.cur.execute("""CREATE TABLE IF NOT EXISTS product_types (
                            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                            title TEXT NOT NULL)
                        """)

    def add(self, title: str):
        """
        Adds one category of product to the product types table

        :param title: The product type's name
        :type title: str

        :return: None
        :rtype: None
        """

        self.cur.execute("""INSERT INTO product_types (title)
                            VALUES(?)
                        """, (title,))
        self.con.commit()

    def getData(self):
        """
        Returns the entire list of product categories

        :return: list of product categories
        :rtype: list
        """

        return [data for data in self.cur.execute('SELECT * FROM product_types').fetchall()]


class ShoppingCartTable(Database):
    """
    Database and table for the shopping cart class, inherited from :class: Database
    """

    def __init__(self):
        """
        Constructor method
        """

        super().__init__('shopping_cart')

    def create(self) -> None:
        """
        Creates a table for shopping cart in shopping_cart.db

        :return: None
        :rtype: None
        """

        pass

    def add(self, *args) -> None:
        """
        Adds one product to the cart table

        :return: None
        :rtype: None
        """

        pass

    def getData(self) -> list:
        """
        Returns the entire list of products

        :return: List of products in cart
        :rtype: list
        """

        pass


products = ProductsTable()
product_types = ProductTypesTable()
products.create()
product_types.create()
