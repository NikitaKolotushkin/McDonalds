#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import sqlite3


def to_binary(file):
    with open(file, mode='rb') as f:
        bin_ = f.read()
    return bin_


class Database():
    def __init__(self, db_name):
        self.con = sqlite3.connect(r'databases/' + f'{db_name}.db')
        self.cur = self.con.cursor()

    def create(self):
        pass

    def add(self, *args):
        pass


class ProductsTable(Database):
    def __init__(self):
        super().__init__('products')

    def create(self):
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

    def add(self, photo, title, description, type, price, date):
        self.cur.execute(f"""INSERT INTO products(photo, title, description, type, price, date)
                            VALUES({photo, title, description, type, price, datetime.datetime.now()})
                        """)
        self.con.commit()


class ProductTypesTable(Database):
    def __init__(self):
        super().__init__('products')

    def create(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS product_types (
                            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                            title TEXT NOT NULL)
                        """)

    def add(self, title):
        self.cur.execute(f"""INSERT INTO proudct_types (title)
                            VALUES({title})
                        """)
        self.con.commit()


if __name__ == '__main__':
    products = ProductsTable()
    products.create()
    ingredients = ProductTypesTable()
    ingredients.create()