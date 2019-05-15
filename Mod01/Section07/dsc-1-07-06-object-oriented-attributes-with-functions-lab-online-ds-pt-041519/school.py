class School():
    def __init__(self, name=None, roster={}):
        self.name = name
        self.roster = roster
        
    def add_student(self, student_name, grade):
        if grade in self.roster:
            self.roster[grade].append(student_name)
        else:
            self.roster[grade] = [student_name]
        
        
    def grade(self, year):
        for k in self.roster.items():
            return self.roster[year]
        
    def sort_roster(self):
        for key in self.roster:
            return self.roster[key].sort()
            

    