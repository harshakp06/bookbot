def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    # print(type(text))
    # num_words = get_num_words(text)
    # print(f"{num_words} words found in the document")
    # report = chars_dict(text)
    print_report(text)



def get_num_words(te):
    words = te.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            # print(lowered,)
            chars[lowered] += 1
            # print(chars)
        else:
            chars[lowered] = 1
    return chars

def print_report(text):

    print("--- Begin report of books/frankenstein.txt ---")

    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    report = chars_dict(text)

    report = dict(sorted(report.items(), key=lambda item:item[1], reverse=True))
    
    # print(report)

    for x,y in report.items():
        # print(x, ":",y)
        # print(y, type(y))
        if not x.isalpha():
            continue
        print(f'The {x}  character was found {y} times')
    print('--- End report ---')
      




main()