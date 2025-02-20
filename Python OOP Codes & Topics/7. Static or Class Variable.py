class Player:
    team_run = 0#This is static or class variable which is created before creating object and always take RAM slot for it
    total_players = 0
    def __init__(self,name,run):
        self.run = run
        self.name = name
        Player.total_players +=1

    def hit_four(self):
        Player.team_run= Player.team_run +4 #Here we have to call it under it's class name cause it is class variable it takes class reference value for being called
        self.run = self.run +4

    def hit_six(self):
        Player.team_run = Player.team_run +6
        self.run = self.run +6

    def total_player_run(self):
        print("Total run made by",self.name,"is",self.run)

    def total_team_run(self):
        print("Total run made by",Player.total_players,"players for team is",Player.team_run)

print(Player.team_run) # proof that it holds its position before creating class and can be useable
SHAKIB= Player("Shakib Al Hasan",0)
TAMIM = Player("Tamim Iqbal",0)

SHAKIB.hit_six()
SHAKIB.hit_six()
SHAKIB.hit_four()
SHAKIB.hit_four()
SHAKIB.hit_four()

TAMIM.hit_six()
TAMIM.hit_six()
TAMIM.hit_six()
TAMIM.hit_six()
TAMIM.hit_four()
TAMIM.hit_four()

SHAKIB.total_player_run()
TAMIM.total_player_run()
print("Using rawly class variable the team run is",Player.team_run)
print("Using SHAKIB object")
SHAKIB.total_team_run()
print("Using TAMIM object")
TAMIM.total_team_run()
