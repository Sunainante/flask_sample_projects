from flask import Flask
from flask import render_template
import mysql.connector
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    try:
        con = mysql.connector.connect(host="localhost",user="root",password="gold@1234",database="book_schema")
        cur=con.cursor(dictionary=True)
        print("connection successful")
    except:
        print("some error")   
    cur.execute("UPDATE BOOK SET TITLE="NDBMS" WHERE BOOK_ID = 1" ) 
    result = cur.fetchall()
    print(result)        
    return render_template("index.html")

@app.route("/sample")
def sample():
    return render_template("sample.html")    