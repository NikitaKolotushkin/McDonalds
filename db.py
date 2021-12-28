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
    :param table_name: The name of table
    :type table_name: str
    """

    def __init__(self, db_name: str, table_name: str) -> None:
        """
        Constructor method
        """

        self.table_name = table_name

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

    def getValuesFromColumn(self, column: str) -> list:
        """
        An empty stub method to get data from the selected column

        :param column:
        :type column: str

        :return: List of data from a selected column
        :rtype: list
        """

        return [data for data in self.cur.execute(f'SELECT {column} FROM {self.table_name}').fetchall()]

    def getProductsByCategory(self, category_: str) -> list:
        """

        """

        return [data for data in self.cur.execute(
            f'SELECT title FROM {self.table_name} WHERE type_=?', (category_,)
        ).fetchall()]

    def getDataByTitle(self, title: str) -> list:
        """

        """

        return [data for data in self.cur.execute(f'SELECT * FROM {self.table_name} WHERE title=?', (title,)).fetchone()]

    def getData(self) -> list:
        """
        An empty stub method to get all data from the selected table

        :return: List of data from a table
        :rtype: list
        """

        return [data for data in self.cur.execute(f'SELECT * FROM {self.table_name}').fetchall()]

    def clearTable(self) -> None:
        """

        """

        self.cur.execute(f'DELETE FROM {self.table_name}')
        self.con.commit()


class ProductsTable(Database):
    """
    Product table class, inherited from :class: Database
    """

    def __init__(self):
        """
        Constructor method
        """

        super().__init__('products', 'products')

    def create(self):
        """
        Creates a table of products in products.db

        :return: None
        :rtype: None
        """

        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS {self.table_name} (
                            product_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                            photo BLOB NOT NULL,
                            title TEXT NOT NULL,
                            description TEXT NOT NULL,
                            type_ TEXT NOT NULL,
                            price INTEGER NOT NULL,
                            date TEXT NOT NULL,
                            FOREIGN KEY (type_) REFERENCES product_types(id))
                        """)

    def add(self, photo: bytes, title: str, description: str, type_: str, price: float):
        """
        Adds one item to the products table

        :param photo: Product photo
        :type photo: bytes
        :param title: The product's name
        :type title: str
        :param description: Product description
        :type description: str
        :param type_: Product type (selected from the product_types table)
        :type type_: str
        :param price: Product price
        :type price: float

        :return: None
        :rtype: None
        """

        self.cur.execute("""
        INSERT INTO products(photo, title, description, type_, price, date) VALUES(?, ?, ?, ?, ?, ?)
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

        super().__init__('products', 'product_types')

    def create(self):
        """
        Creates a table of product types in products.db

        :return: None
        :rtype: None
        """

        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS {self.table_name} (
                            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                            title TEXT NOT NULL)""")

    def add(self, title: str):
        """
        Adds one category of product to the product types table

        :param title: The product type's name
        :type title: str

        :return: None
        :rtype: None
        """

        self.cur.execute("""INSERT INTO product_types (title)
                            VALUES(?)""", (title,))
        self.con.commit()

    def getCategoryId(self, category):
        """

        """

        return self.cur.execute(
            f'SELECT id FROM {self.table_name} WHERE title={category}'
        ).fetchone()

    def getCategoryById(self, id):
        return self.cur.execute(
            f'SELECT title FROM {self.table_name} WHERE id={id}'
        ).fetchone()[0]


class ShoppingCartTable(Database):
    """
    Database and table for the shopping cart class, inherited from :class: Database
    """

    def __init__(self):
        """
        Constructor method
        """

        super().__init__('shopping_cart', 'cart')

    def create(self) -> None:
        """
        Creates a table for shopping cart in shopping_cart.db

        :return: None
        :rtype: None
        """

        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS {self.table_name} (
                            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                            product_title TEXT NOT NULL,
                            count INTEGER NOT NULL,
                            price INTEGER NOT NULL)""")

    def add(self, product_title, count, price) -> None:
        """
        Adds one product to the cart table

        :return: None
        :rtype: None
        """

        self.cur.execute("""INSERT INTO cart (product_title, count, price)
                                    VALUES(?, ?, ?)""", (product_title, count, price))
        self.con.commit()


products = ProductsTable()
product_types = ProductTypesTable()
cart = ShoppingCartTable()
products.create()
product_types.create()
cart.create()
