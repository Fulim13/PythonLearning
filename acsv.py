import csv

# WRITE DATA

# with open("data.csv", "w") as file:
#     # csv.writ emust put iin file object, so cannot use path object
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000.1, 5])
#     writer.writerow([1001.2, 15])

# READ DATA
with open("data.csv") as file:
    # csv.writ emust put iin file object, so cannot use path object
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)

# only can use list or for loop, the reader object only can loop for one time
# list method
# [['transaction_id', 'product_id', 'price'], ['1000.1', '5'], ['1001.2', '15']]


# for loop
# ['transaction_id', 'product_id', 'price']
# ['1000.1', '5']
# ['1001.2', '15']
