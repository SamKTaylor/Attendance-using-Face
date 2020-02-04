#!/bin/python3.6
from pymongo import Connection
import pandas as pd

connection = Connection()
db = connection.attendance
collection = db.users

collection.insert({"x":1})
