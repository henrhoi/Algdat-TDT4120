from sys import stdin
__author__ = "Henrik Høiness"

class Record:
    value = None
    next = None

    def __init__(self, value):
        self.value = value
        self.next = None




def search(record):
    temp = -1
    while record.next != None:
        if record.value > temp:
            temp = record.value
        record = record.next
    if record.value > temp:
        temp = record.value

    return temp







def main():
    # reading from stdin and creating a linked list
    first = None
    last = None
    for line in stdin:
        penultimate = last
        last = Record(int(line))
        if first is None:
            first = last
        else:
            penultimate.next = last

    # searching and printing out the result
    print(search(first))


if __name__ == "__main__":
    main()
