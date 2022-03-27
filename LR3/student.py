

"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def isEqual(self, otherStudent):
        """Compares two Student class objects to check if they are equal"""
        return (self.name == otherStudent.name)
    
    def isLessThan(self, otherStudent):

        return (self.name < otherStudent.name)

    def isGreaterThanOrEqual(self, otherStudent):

        return (self.name >= otherStudent.name)


def main():
    """A simple test."""
    student = Student("Ken", 5)
    for i in range(1, 6):
        student.setScore(i, 100)

    student2 = Student("John Ethan", 5)
    print(student2)
    for i in range(1, 6):
        student2.setScore(i, 96)

    student3 = Student("Ken", 5)
    print(student3)
    for i in range(1, 6):
        student3.setScore(i, 100)

    if student.isEqual(student3):
        print("Equal")
    else:
        print("Not Equal")

    if student2.isLessThan(student):
        print("Less Than")

    if student.isGreaterThanOrEqual(student2):
        print("Greater Than Or Equal")


if __name__ == "__main__":
    main()


