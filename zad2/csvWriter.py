import csv


class csvWriter:
    def __init__(self, path):
        self.path = path
        self.file = open(path, "w")
        self.csv_writer = csv.writer(self.file)
        self.csv_writer.writerow(["round_no", "alive_sheep"])

    def close(self):
        self.file.close()

    def aliveSheep(self, round_number, alive_sheep):
        self.csv_writer.writerow([round_number, alive_sheep])
