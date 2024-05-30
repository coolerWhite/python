file_open = 'zip'

with open(file_open, 'rb') as open_file:
    btext = open_file.read()

btext[:7]