with open("files_practice/my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("files_practice/new_file.txt", mode="w") as file:
    file.write("My homepage")

with open("files_practice/my_file.txt", mode="a") as file:
    file.write("My name is Felipe.\n")
