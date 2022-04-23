import csv
from datetime import datetime

class User():
    def __init__(self, filepath):
        self.file = open(filepath, 'r+')
        self.filepath = filepath

    def get_chat(self):
        reader = csv.reader(self.file)
        for row in reader:
            if (row[0] == user1 or row[0] == user1) and (row[1] == user2 or row[1] == user2):
                print(row)


    def delete_all(self):
        self.file.truncate(0)

class UserData():
    def __init__(self, user_name, filepath):
        self.filepath = filepath
        self.user_name = user_name
        self.file = open(filepath, 'r+')
        self.reader = csv.reader(self.file)
        self.writer = csv.writer(self.file)


    def send_message(self, reciever, text):
        now = datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M:%S")
        row = [self.user_name, reciever, text, now]
        self.writer.writerow(row)


user1 = UserData('Artur', 'chat.csv')

user1.send_message('Ильшат', 'Privet, kak dela?')

chat = User('chat.csv')
chat.get_chat()
chat.delete_all()
