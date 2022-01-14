from WebCGPA.models import subsjects
from WebCGPA.form import subjects
from flask import render_template, redirect, url_for, request, flash
from WebCGPA import app, db

@app.route('/', methods=['GET', 'POST']) #home route
def home():
    form = subjects() #the form for entering the marks
    if form.validate_on_submit(): # this if the if form is submited execute the following code
        marks = subsjects(subjectOne=form.subjectOne.data, subjectTwo=form.subjectTwo.data, subjectThree=form.subjectThree.data, subjectFour=form.subjectFour.data) # this is to store in what you've entered into the form into database
        db.session.add(marks)
        db.session.commit()
    total = subsjects.query.all() #this is to show all the total marks
    return render_template("ThePage.html", form=form, total=total)

@app.route('/remove', methods=['GET', 'POST']) # when pressing home button delete the data in the database
def remove():
    subsjects.query.delete()
    db.session.commit()
    return redirect(url_for('home'))
    