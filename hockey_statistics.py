import json

class HockeyStats:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename) as stats:
            data = stats.read()
        # all the stats stay here
        self.stats = json.loads(data)

    # search for a player by name
    def search_for_player(self, name):
        for i in self.stats:
            if i["name"].lower() == name.lower():
                return i
            
class HockeyStatsApplication:
    def __init__(self):
        # get the filename to create the stats object
        if True:
            filename = "partial.json"
        else:
            filename = input("filename: ")
        self.hockeystats = HockeyStats(filename)

    # searching for a specific player by name
    def search_for_player(self):
        name = input("name: ")
        player_stats = self.hockeystats.search_for_player(name)
        print(player_stats)

    # list the possible commands
    def help(self):
        print("0 quit\n1 search for player\n2 teams\n3 countries\n4 players in team\n5 players from country\n6 most points\n7 most goals\n")

    def execute(self):
        # start taking commands
        self.help()
        while True:
            command = input("command: ")
            # exit
            if command == "0":
                break
            # search for a specific player
            elif command == "1":
                self.search_for_player()


app = HockeyStatsApplication()
app.execute()