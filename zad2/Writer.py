import json
class Writer:
    def __init__(self, path):
        self.path = path
        self.file = open(path, "w")

    def write(self, text):
        self.file.write(text)

    def close(self):
        self.file.close()

    def roundInfo(self, roundNumber, wolfPosition, sheepPositions):
        roundData = {
            "round_no": roundNumber,
            "wolf_pos": wolfPosition,
            "sheep_pos": sheepPositions
        }
        json_data = json.dumps(roundData, indent=1)
        self.write(json_data + "\n")