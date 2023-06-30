"""
This simple fun to read and case change the text of file
and write content into a new file
"""


def main():
    with open('input.txt', 'r') as ifile, \
            open('output.txt', 'w') as output:
        text = ifile.readlines()
        uppercase = [t.upper() for t in text]
        output.writelines(uppercase)


if __name__ == "__main__":
    main()
