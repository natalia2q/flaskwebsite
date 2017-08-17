# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 18:03:45 2017

@author: Natalia
"""

from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'bank'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# never leave this on in production or someone will break your site.
app.debug = True

@app.route("/")
def index():
    return "Hello world one more time!"
    
    
@app.route("/test")
def test():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM customer")
    data = cursor.fetchone()
    if data is None:
     return "no data"
    else:
     return str(data)  
    
if __name__ == "__main__":
    app.run()