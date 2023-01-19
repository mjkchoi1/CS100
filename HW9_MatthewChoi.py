def file_copy(in_file, out_file):
    f = open(in_file, 'r')
    w = open(out_file, 'w')
    w.write(f.read())
    f.close()
    w.close()

def file_stats(in_file):
    open_file = open(in_file)
    noLines = 0
    noWords=0
    noChars=0
    for currentLine in openFile:
        words = currentLine.split()
        for currentWord in words
            noWords+=1
        for currentChar in currentLine:
            noChars+=1
        noLines+=1
    print('lines',noLines)
    print('words',noWords)
    print('characters',noChars)


def repeat_words(infile, outfile):
    with open(infile, 'r') as inf, open(outfile, 'w') as outf:
        for line in inf:
            d = []
            for word in line.strip().split():
                word = word.strip().lower()
                if word not in d:
                    d.append(word)
                else:
                    outf.write(word+' ')
            if len(d) > 0:
                outf.write('\n')

