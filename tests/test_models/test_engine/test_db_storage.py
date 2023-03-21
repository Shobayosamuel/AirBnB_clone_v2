#!/usr/bin/python3
"""Test module for database storage"""
import unittest
from models import storage
from models.user import User
import MySQLdb
import os
from datetime import datetime

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 'db_storage test not supported')
class TestDb_Storage(unittest.TestCase):
    """Class to test the database storage engine"""
    def test_new_user(self):
        conn = MySQLdb.connect(host=os.getenv("HBNB_MYSQL_HOST"),
                               user=os.getenv("HBNB_MYSQL_USER"),
                               db=os.getenv("HBNB_MYSQL_DB"),
                               passwd=os.getenv("HBNB_MYSQL_PWD"),
                               port=3306)
        new_user = User(**{"first_name": "sam",
                           "last_name": "shobs",
                           "email": "shobs@gmail.com",
                           "password": 17000})
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        former_count = cur.fetchall()
        cur.close()
        db.close()
        new_user.save()
        conn = MySQLdb.connect(host=os.getenv("HBNB_MYSQL_HOST"),
                               user=os.getenv("HBNB_MYSQL_USER"),
                               db=os.getenv("HBNB_MYSQL_DB"),
                               passwd=os.getenv("HBNB_MYSQL_PWD"),
                               port=3306)
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        new_count = cur.fetchall()
        self.assertEqual(new_count[0][0], former_count[0][0] + 1)
        cur.close()
        db.close()

    def test_save(self):
        """ object is successfully saved to database """
        new = User(
            email='john2020@gmail.com',
            password='password',
            first_name='John',
            last_name='Zoldyck'
        )
        dbc = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor = dbc.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new.id))
        result = cursor.fetchone()
        cursor.execute('SELECT COUNT(*) FROM users;')
        old_cnt = cursor.fetchone()[0]
        self.assertTrue(result is None)
        self.assertFalse(new in storage.all().values())
        new.save()
        dbc1 = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor1 = dbc1.cursor()
        cursor1.execute('SELECT * FROM users WHERE id="{}"'.format(new.id))
        result = cursor1.fetchone()
        cursor1.execute('SELECT COUNT(*) FROM users;')
        new_cnt = cursor1.fetchone()[0]
        self.assertFalse(result is None)
        self.assertEqual(old_cnt + 1, new_cnt)
        self.assertTrue(new in storage.all().values())
        cursor1.close()
        dbc1.close()
        cursor.close()
        dbc.close()

