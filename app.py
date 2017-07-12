from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('addExercise.html')

@app.route('/enternew')
def new_student():
   return render_template('addExercise.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      print(request.form)
      try:
         # get all of the data from the form
         val = request.form['bodyPart']
         val2 = request.form['Exercise']
         print(val)
         print(val2)

         with sql.connect("types.db") as con:
            cur = con.cursor()

            cur.execute("INSERT INTO types (type) VALUES (?)",[val])

            con.commit()
            message = "Record successfully added"
      except Exception as err:
         con.rollback()
         print(err)
         message = "error in insert operation"

      finally:
         return render_template("result.html",msg = message)
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
