import csv

class csvWriter:
    def __init__(self, path):
        self.path = path
        self.file = open(path, "w")
        self.csv_writer = csv.writer(self.file)
        self.csv_writer.writerow(["round_no", "alive_sheeps"])

    def close(self):
        self.file.close()

    def aliveSheeps(self, roundNumber, aliveSheeps):
        self.csv_writer.writerow([roundNumber, aliveSheeps])