"""Count words in file."""


# create a function 
def get_word_count(textfile):

# set up a counter of how many times each space separated word occurs
    count = 0
    word_counts = {}

# create variable that opens up the file we passed in -- test.txt
    opened_file = open(textfile)

# create a for loop and have it loop through each list
    for line in opened_file:
        line = line.rstrip()
        words = line.split()

        for word in words:
            word_counts[word] = word_counts.get(word,0) + 1
    for word, count in word_counts.items():
        print(word, count)

#   count the word in final data set (the word and its count number)
#   print word and its word count

#   have it return word and it's count number

print(get_word_count('test.txt'))

