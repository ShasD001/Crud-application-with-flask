from flask import Flask,render_template,request,redirect,url_for
import sqlite3
 
app=Flask(__name__)
 
 
@app.route('/')
def index():
    conn=sqlite3.connect('studentManagementSystem.db')
    cur=conn.cursor()
 
    sql="select * from student"
    cur.execute(sql)
 
    students=cur.fetchall()
    conn.close()
 
    return render_template('index.html',studentList=students)
 
 
 
@app.route('/add')
def add():
    return render_template('add.html')
 
@app.route('/save',methods=['POST'])
def save():
    stu_name = request.form['name']
    stu_email = request.form['email']
 
    # return f"NAME = {stu_name} EMAIL = {stu_email}"
 
    conn=sqlite3.connect('studentManagementSystem.db')
 
    cur=conn.cursor()
 
    #insert into student(name,email) values(stu_name,stu_email)
    cur.execute("insert into student(name,email) values(?,?)",(stu_name,stu_email))
 
 
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
 
 
 
@app.route('/delete/<int:id>')
def delete(id):
    conn=sqlite3.connect('studentManagementSystem.db')
    cur=conn.cursor()
 
    sql="delete from student where id=?"
    cur.execute(sql,(id,))
 
    conn.commit()
    conn.close()
 
    return redirect('/')
 
 
 
@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    conn=sqlite3.connect('studentManagementSystem.db')
    cur=conn.cursor()
 
    if request.method == 'POST':
        sqlQuery="""
        update student
        set name = ? , email = ?
        where id= ?
        """
        updatedName = request.form['name']
        updatedEmail =request.form['email']
        cur.execute(sqlQuery,(updatedName,updatedEmail,id))
        conn.commit()
        conn.close()
        return redirect('/')
    else:
        sqlQuery= "select * from student where id=?"
        cur.execute(sqlQuery,(id,))
        studentDetail=cur.fetchone()
        conn.close()
        return render_template('edit.html',student=studentDetail)
 
 
 
 
 
 
app.run(host='0.0.0.0',port=5000)