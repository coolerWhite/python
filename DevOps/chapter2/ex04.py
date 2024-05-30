with open("file.json", "r") as open_file:
    policy = open_file.readlines()

print(policy[4])