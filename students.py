from abc import ABC
from datetime import datetime
from tkinter import Y

class Student:
    def __init__(self, full_name, email, start_year):
        self.full_name = full_name
        self.email = email
        self.start_year = start_year
    def get_name(self):
        return self.full_name

    def set_name(self, full_name):
        self.fname = full_name
       
    def set_start_year(self, year):
        if year < (datetime.now().strftime("%Y")):
            print(f"Start date can't be passed date.")
        else:
            self.start_year = year


class Athelete(Student): 
    def compete(self):
       print("Athelete compete in diferent sports")

    def win(self):
        print("***", self.full_name, " won a medal ***")


class Artist(Student):
    def compete(self):
        print("Artists compete playing musical instruments")

    def leader(self):
        print(self.full_name, " leads the school's music board")
    