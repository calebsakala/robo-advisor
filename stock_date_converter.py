#!/usr/bin/env python3

"""This program is intended to take the dates in every file in the stock exchange data,
and convert them to integers so that they can be easily graphed"""

import datetime

"""Defining a function to convert the dates"""

def date_in_days(year, month, day):
	"""The 1900 dating system is used"""

	default_date = datetime.date(1900, 1, 1)
	current_date = datetime.date(year, month, day)
	delta = current_date - default_date
	return delta.days


"""Defining a function to recreate the file with the new dates"""

def recreate_file(old_file_name, new_file_name, convert=date_in_days):
	"""Both files are opened"""

	with open(new_file_name, "w") as newfile:
		with open(old_file_name, "r") as oldfile:

			"""The first line is written to the new file immediately as it is always 
			just a header"""
			newfile.write(oldfile.readline())

			"""Then the date is extracted from every other file"""
			for line in oldfile.readlines():
				date = line.split(',')[0]
				rest_of_line = line.split(',')[1:]
				date_list = date.split('-')
				years = int(date_list[0])
				months = int(date_list[1])
				days = int(date_list[2])

				"""The date is converted to days"""
				date_distance = convert(years, months, days)

				"""And the output is joined back with the rest of the lines in the new file"""
				newfile.write(str(date_distance) + "," + ",".join(rest_of_line))


read_file = input("What stock file would you like to edit? > ")
write_file = input("\nWhat would you like to rename the new file we will create? > ")

recreate_file(read_file, write_file)
