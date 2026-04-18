languages = ["Python\n", "Java\n", "C++\n"]

with open("data.txt", "w") as file:
    file.writelines(languages)