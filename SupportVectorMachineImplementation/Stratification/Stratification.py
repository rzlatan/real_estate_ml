import os
import glob
import pandas as pd
import csv

extension = "csv"
target_train_file = "../Data/train_dataset_without_scaling.csv"
all_train_files = [i for i in glob.glob('TRAIN*.{}'.format(extension))]
print(all_train_files)

all_test_files = [i for i in glob.glob('TEST*.{}'.format(extension))]
target_test_file = "../Data/test_dataset_without_scaling.csv"
print(all_test_files)

# Export train set to csv
#
with open(target_train_file, mode='w', newline='', encoding='utf8') as train_file:
    writer = csv.writer(train_file)
    for file in all_train_files:
        with open(file, mode='r', encoding='utf8') as source_file:
            reader = csv.reader(source_file)
            for row in reader:
                writer.writerow(row)

# Combine all test files in the list
#

# Export test set to csv
#
with open(target_test_file, mode='w', newline='', encoding='utf8') as test_file:
    writer = csv.writer(test_file)
    for file in all_test_files:
        with open(file, mode='r', encoding='utf8') as source_file:
            reader = csv.reader(source_file)
            for row in reader:
                writer.writerow(row)