import csv


def store_csv(data):
    with open("ReviewAnalysis.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(data)

    file.close()


def load_csv():
    data_l = []
    with open("ReviewAnalysis.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if not len(row) == 0:
                data_l.append(row)
    file.close()
    return data_l


if __name__ == '__main__':
    data_ = ["Bad Movie", 0]
    store_csv(data_)
    data_list = load_csv()
    print(data_list)