class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test
    #   scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    def calculate(self):
        # Given a list of integers between 0-100 representing the
        # student's scores, this method will return the average
        # grade for their semester between A-O
        cumsum = 0
        for score in self.scores:
            cumsum += score
        average = cumsum/len(self.scores)

        if average < 40:
            grade = 'T'
        elif 40 <= average < 55:
            grade = 'D'
        elif 55 <= average < 70:
            grade = 'P'
        elif 70 <= average < 80:
            grade = 'A'
        elif 80 <= average < 90:
            grade = 'E'
        else:
            grade = 'O'
        return grade

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())