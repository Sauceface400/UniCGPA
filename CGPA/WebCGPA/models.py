from WebCGPA import db

#This to craete the database table for all the marks for the 4 subjects
class subsjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subjectOne = db.Column(db.Integer, nullable=False)
    subjectTwo = db.Column(db.Integer, nullable=False)
    subjectThree = db.Column(db.Integer, nullable=False)
    subjectFour = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Subsjects('{self.subjectOne}', '{self.subjectTwo}', '{self.subjectThree}', '{self.subjectFour}')"
