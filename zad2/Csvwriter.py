import csv
import logging


class Csvwriter:
    def __init__(self, path):
        self.path = path
        with open(self.path, "w", newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["round_no", "alive_sheep"])

    def alive_sheep(self, round_number, alive_sheep):
        with open(self.path, "a", newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([round_number, alive_sheep])
        logging.debug("Data written to alive.csv file")
