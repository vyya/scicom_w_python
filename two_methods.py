class PartyAnymal:
    x = 0
    name = ''
    
    def __init__(self, nam):
        self.name = nam
        print(f"{self.name} constructed")

    def party(self):
        self.x = self.x + 1
        print(f"{self.name} party count {self.x}")

q = PartyAnymal('Quincy')
j = PartyAnymal('Jack')
q.party()
j.party()
q.party()
