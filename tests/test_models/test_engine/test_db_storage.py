#!/usr/bin/python3
"""Test module for database storage"""
import unittest
from models import storage
from models.user import User
import MySQLdb
import os

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

