def main():
   
    from sys import argv

    in_file = argv[1]

    open_file = open(in_file) 

    all_text = open_file.read()

    words = all_text.split(' ')

    word_count = {}

    for each in words:
        each
        if each in word_count:
            word_count[each] += 1
        else:
            word_count[each] = 1

    print word_count['cats']

if __name__ == "__main__":
    main()