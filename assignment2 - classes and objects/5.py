# Define a class Team with instance object variable a list of team member names. Provide methods to input member names and display member names.

class Team:
    def __init__(self, members):
        self.members = members

    def addMembers(self, newMembers):
        self.members.extend(newMembers)
    
    def displayMembers(self):
        for member in self.members:
            print(member, '\n')

    def getMembers(self):
        return self.members
    
# initialize object
team1 = Team(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
team2 = Team(['H', 'I', 'J', 'K', 'L', 'M'])

team1.displayMembers()
print("-----------------")
team2.displayMembers()

print("-----------------")
team1.addMembers(team2.getMembers())
team1.displayMembers()