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
        # return a list to match the string comprehension
        return [i for i in self.stats if i["name"].lower() == name.lower()]
    
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
        return player_stats

    # creating the nicely spaced output string
    def make_string(self, players: list) -> str:
        for player in players:
            total_points = player["assists"] + player["goals"]
            return f"{player["name"]:<21}{player["team"]:<5}{player["goals"]:>2} + {player["assists"]:>2} = {total_points:>3}"

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
            # search for a specific player by name
            elif command == "1":
                player = self.search_for_player()
                print(self.make_string(player))


app = HockeyStatsApplication()
app.execute()