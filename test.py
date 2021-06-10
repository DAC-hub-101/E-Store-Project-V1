import csv
import pandas as pd
import matplotlib.pyplot as plt
car_list = []
with open('Products.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        car_list[row[0]] = Car(row[4])