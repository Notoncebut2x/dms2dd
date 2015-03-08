#!/usr/bin/python

import csv 
import re												# imports the special modules that we need to run this program.

dms_input = open('syria_border_crossings.csv', 'rb')	# The input file with our coordinates
reader = csv.reader(dms_input)
next(reader, None)										# Skips the Header Row

final_output = open('onelist.csv', 'wb')				# Creates Output CSV
writer = csv.writer(final_output)						# Function to write data to that CSV

for row in reader:
    dms_x_list = ([re.sub("[^0-9]","", row[1])])		# Strips just the numbers out for the x
    for item in dms_x_list:
        x_list = ([float(dms_x_list[0][0:2]) + float(dms_x_list[0][2:4]) * 1/60 + float(dms_x_list[0][4:8]) / 10 * 1/60 * 1/60])
    #print dms_x_list
    dms_y_list = ([re.sub("[^0-9]","", row[2])])		# Strips just the numbers out for the y
    for item in dms_y_list:
        y_list = ([float(dms_y_list[0][0:2]) + float(dms_y_list[0][2:4]) * 1/60 + float(dms_y_list[0][4:8]) / 10 * 1/60 * 1/60])
    #print dms_y_list
    combo= dict(zip(x_list, y_list))					# Converts the two numbers as a dictionary
    #print combo
    for key, value in combo.items():
        writer.writerow([key, value])					# Writes the data in the dictionary to a csv


dms_input.close()
final_output.close()