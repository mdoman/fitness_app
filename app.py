from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('addExercise.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         sets = request.form['sets']
         weight = request.form['weight']

         with sql.connect("exercises.db") as con:
            cur = con.cursor()

            cur.execute("INSERT INTO exercises (name,sets,weight) VALUES (?,?,?)",(nm,sets,weight) )

            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"

      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("exercises.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from exercises")

   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
