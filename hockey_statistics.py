import json

class HockeyStats:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename) as stats:
            data = stats.read()
        # all the stats stay here
        self.stats = json.loads(data)

    # for testing
    def print_file(self):
        print(self.stats)

class HockeyStatsApplication:
    def __init__(self):
        # get the filename to create the stats object
        filename = input("filename: ")
        self.hockeystats = HockeyStats(filename)

    # searching for a specific player
    def search_for_player(self):
        name = input("name: ")
        pass

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