import sys


class Dataset:
    def __init__(self, meta: str, st: str):
        self.parse_metadata(meta)
        self.parse_score_table(st)

    def parse_metadata(self, s: str):
        self.num_books = int(s[0:s.index(' ')])
        s = s[s.index(' ') + 1:]
        self.num_lib = int(s[0:s.index(' ')])
        s = s[s.index(' ') + 1:]
        self.num_days = int(s.strip())

    def parse_score_table(self, s: str):
        self.score_table = []
        while (not s.strip() == ""):
            try:
                idx = s.index(' ')
                self.score_table.append(int(s[0:idx]))
                s = s[idx + 1:]
            except ValueError:
                self.score_table.append(int(s.strip()))
                break

    def __str__(self):
        return "Number of books : {}, Number of Libraries : {}, Number of Days : {}".format(self.num_books,
                                                                                            self.num_lib, self.num_days)


class Library:
    def __init__(self, meta: str, bs: str, ass_data: Dataset):
        self.ass_data = ass_data
        self.parse_metadata(meta)
        self.parse_book_list(bs)
        self.calculate_score()

    def calculate_score(self):
        self.total_score = 0
        for book in self.book_table:
            self.total_score += self.ass_data.score_table[book]

    def parse_metadata(self, s: str):
        self.num_books = int(s[0:s.index(' ')])
        s = s[s.index(' ') + 1:]
        self.num_days = int(s[0:s.index(' ')])
        s = s[s.index(' ') + 1:]
        self.num_ship = int(s.strip())

    def parse_book_list(self, s: str):
        self.book_table = []
        while (not s.strip() == ""):
            try:
                idx = s.index(' ')
                self.book_table.append(int(s[0:idx]))
                s = s[idx + 1:]
            except ValueError:
                self.book_table.append(int(s.strip()))
                break

    def __str__(self):
        return "Number of books : {}, Number of Days : {}, Number of Days to ship : {}, Total Score : {}".format(
            self.num_books,
            self.num_days,
            self.num_ship, self.total_score)

    def __lt__(self, other):
        return self.total_score < other.total_score
    def __le__(self, other):
        return self.total_score <= other.total_score
    def __eq__(self, other):
        return self.total_score == other.total_score
    def __ne__(self, other):
        return self.total_score != other.total_score
    def __gt__(self, other):
        return self.total_score > other.total_score
    def __ge__(self, other):
        return self.total_score >= other.total_score

class Solve:
    def __init__(self, data : Dataset, lib_list : list):
        self.data = data
        self.lib_list = lib_list
    def solve(self):
        time_limit = self.data.num_days
        self.lib_list.sort(key=lambda x: x.total_score, reverse=True)



    def solve_library(self, time_limit, library : Library):
        pass

class SolutionLibrary:
    def __init__(self, id : int, num_send_book : int, books : list):
        self.id = id
        self.num_send_book = num_send_book
        self.books = books
    def __str__(self):
        line1 = "{} {}".format(self.id, self.num_send_book)
        line2 = ""
        for book in self.books:
            line2 += str(book) + " "
        return line1 + "\n" + line2

def problembcode(lib_list):
    selected = []
    for i in lib_list:
        lowest = 1000
        chosen = -1
        i = 0
        for library in lib_list:
            if (library.num_days < lowest) and not (i in selected):
                lowest = library.num_days
                chosen = i
            i += 1
        selected.append(chosen)



    file = open("ans2.txt", "w")
    file.write(str(len(selected)) + "\n")
    i = 0
    for lnum in selected:
        output = ''
        output += str(lnum)
        output += ' '
        output += str(len(library[lnum].book_table))
        output += "\n"
        file.write(output)
        output = ''
        for book in library[lnum].book_table:
            output += str(book)
            output += ' '
        output += "\n"
        file.write(output)

def problemccode(lib_list):
    selected = []
    for i in lib_list:
        lowest = 0
        chosen = -1
        i = 0
        for library in lib_list:
            if (library.total_score/library.num_days > lowest) and not (i in selected):
                lowest = library.num_days
                chosen = i
            i += 1
        selected.append(chosen)


    file = open("ans3.txt", "w")
    file.write(str(len(selected)) + "\n")
    i = 0
    for lnum in selected:
        output = ''
        output += str(lnum)
        output += ' '
        output += str(len(library[lnum].book_table))
        output += "\n"
        file.write(output)
        output = ''
        for book in library[lnum].book_table:
            output += str(book)
            output += ' '
        output += "\n"
        file.write(output)

def problemdcode(lib_list):
    selected = []
    for i in lib_list:
        lowest = 0
        chosen = -1
        i = 0
        for library in lib_list:
            if (library.total_score/library.num_days > lowest) and not (i in selected):
                lowest = library.num_days
                chosen = i
            i += 1
        selected.append(chosen)


    file = open("ans3.txt", "w")
    file.write(str(len(selected)) + "\n")
    i = 0
    for lnum in selected:
        output = ''
        output += str(lnum)
        output += ' '
        output += str(len(library[lnum].book_table))
        output += "\n"
        file.write(output)
        output = ''
        for book in library[lnum].book_table:
            output += str(book)
            output += ' '
        output += "\n"
        file.write(output)


def main(s: str):
    file = open("e.txt")
    container = file.read().splitlines()
    data = Dataset(container[0], container[1])
    print("Data metadata parsed")
    container = container[2:]
    lib_list = []
    while (len(container) >= 2):
        if (not container[0].strip() == "" or not container[1].strip() == ""):
            lib_list.append(Library(container[0], container[1], data))
            container = container[2:]
        else:
            break

    selected = []
    for i in lib_list:
        lowest = 0
        chosen = -1
        i = 0
        for library in lib_list:
            if (library.total_score/library.num_days > lowest) and not (i in selected):
                lowest = library.num_days
                chosen = i
            i += 1
        selected.append(chosen)


    file = open("ans3.txt", "w")
    file.write(str(len(selected)) + "\n")
    i = 0
    for lnum in selected:
        output = ''
        output += str(lnum)
        output += ' '
        output += str(lib_list[lnum].num_books)
        output += "\n"
        file.write(output)
        output = ''
        for book in lib_list[lnum].book_table:
            output += str(book)
            output += ' '
        output += "\n"
        file.write(output)


if __name__ == '__main__':
    main(sys.argv)

