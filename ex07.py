def main():
   
    from sys import argv

    in_file = argv[1]

    open_file = open(in_file) 

    all_text = open_file.read()
    all_text = all_text.lower()
    without_newlines = all_text.replace('\n',' ')
    without_newlines = without_newlines.rstrip()
    words = without_newlines.split(' ')
   
    word_count = {}

    for each in words:

        each = each.strip(".?,:;!-")

        if each in word_count:
            word_count[each] += 1
        else:
            word_count[each] = 1

    frequency = {}
    for k, v in word_count.items():
        
        if v in frequency:
            frequency[v].append(k)
        else:
            frequency[v] = [k]

    f_view = frequency.keys()
    f_view.sort(reverse=True)
    for key in f_view:
        print key, sorted(frequency[key])




if __name__ == "__main__":
    main()