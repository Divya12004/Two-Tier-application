from flask import Flask, render_template
import mysql.connector
import time

app = Flask(__name__)

@app.route("/")
def home():

    for i in range(10):

        try:
            conn = mysql.connector.connect(
                host="mysql",
                user="root",
                password="root123",
                database="mydb"
            )

            conn.close()

            return render_template("index.html")

        except:
            time.sleep(3)

    return "Database Connection Failed"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
