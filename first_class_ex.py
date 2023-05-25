class Party_Anymal:
    x = 0
    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

an = Party_Anymal()

an.party()
an.party()
an.party()
