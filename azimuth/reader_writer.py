import csv


def read_csv(a_file):
    with open(a_file) as csv_file:  # get radar data
        reader = csv.reader(csv_file, delimiter=',')
        return reader


def write_csv(a_file, a_list):
    with open(a_file, "w", newline='') as csv_file:
        print("Writing .csv: 0%")
        writer = csv.writer(csv_file)
        writer.writerows(a_list)
        print("Writing .csv: 100%")


# For testing
if __name__ == '__main__':
    print(read_csv('input_data/grid.csv'))
