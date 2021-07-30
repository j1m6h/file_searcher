import os

print("FILE SEARCHER")
print("Type 'help' for a list of commands... \n")

dir_path = os.path.dirname(os.path.realpath("/"))

while True:
    results = 0

    buf = input("Enter a file name : ")

    if buf == 'help':
        print("exit - Terminate the program")
        continue
    if buf == 'exit':
        break

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if str(file) == str(buf):
                results += 1
                print(f"Found file '{buf}' in {root}")

    if results > 1 or 0:
        print(f"Found ({results}) results.")
    else:
        print(f"Found ({results}) result.")
