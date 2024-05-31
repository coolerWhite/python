# with open("file.txt", "r") as open_file:
#     with open("file-change.txt", "w") as change_file:
#         for line in open_file:
#             change_file.write(line)
#             print(line)
    
### функция

def line_reader(file):
    with open(file, "r") as open_file:
        for line in open_file:
            print(line)
            yield line

reader = line_reader("file.txt")

with open("file-big.txt", "w") as big_file:
    for line in reader:
        big_file.write(line)