import csv


class Creds:

    # credentials
    username = ""
    access_key_id = ""
    secret_key = ""

    def __init__(self, creds_file):

        with open(creds_file) as file:
            reader = csv.reader(file, delimiter=",")

            header = next(reader)
            creds_line = next(reader)

            self.username = creds_line[0]
            self.access_key_id = creds_line[2]
            self.secret_key = creds_line[3]
