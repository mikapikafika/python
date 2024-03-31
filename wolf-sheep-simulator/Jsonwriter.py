import json
import logging


class Jsonwriter:
    def __init__(self, path):
        self.path = path

    def write(self, text):
        with open(self.path, "a") as file:
            file.write(text)

    def position_info(self, round_number, wolf_position, sheep_positions):
        round_data = {
            "round_no": round_number,
            "wolf_pos": wolf_position,
            "sheep_pos": sheep_positions
        }
        json_data = json.dumps(round_data, indent=1)
        self.write(json_data + "\n")
        logging.debug("Data written to pos.json file")
