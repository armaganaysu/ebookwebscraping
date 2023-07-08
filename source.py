from urllib.request import urlopen
from bs4 import BeautifulSoup
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
import re

book_number = int(input("How many books would you like to check ? 1 or 2."))
# Specify url of the web page
Enter_input = input("Search(Please enter uppercase and lowercase letters correctly.)  : ")
lists = Enter_input.split()
element = "_".join(lists)
URL = "https://en.wikibooks.org/wiki/" + element + "/Print_version"

source = urlopen(URL).read()
print("Searched book url is: "+URL)



soup = BeautifulSoup(source,'lxml')

# Extract the plain text content from paragraphs
text = ''
for paragraph in soup.find_all('body'):
    text += paragraph.text

# Clean text
text = re.sub(r'\[.*?\]+', '', text)
text = text.replace('\n', '')

file = open("ebookdata.txt","a",encoding="utf-8")
file.write(text)
file.write("*****************************************************************************************************")
file.close()
stop_words = set(stopwords.words('english'))
stop_words.update("0","1","2","3","4","5","6","7","8","9","q","w","e","r","t","y","u","o","p","a","s","d","f","g","h","j","k","l","i","z","x","c","v","b","n","m")
ntext = text.lower()



for element in stop_words:
    ntext = ntext.replace(" " + element + " ", " ")



# Cleaning text and lower casing all words
for char in '”=*/{},[]&^<>_!-"#.½%$();?|~:\ \' \n':
    ntext=ntext.replace(char,' ')
    ''.join(ntext.split())
listToStr = ntext.lower()
# split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s)
word_list = ntext.split()

# Initializing Dictionary
d = {}
# counting number of times each word comes up in list of words (in dictionary)
for word in word_list:
    d[word] = d.get(word, 0) + 1

word_freq = []
for key, value in d.items():
    word_freq.append((value, key))
word_freq.sort(reverse=True)




if(book_number==1):
    intcount_choice = input("Would you like to choose how many frequencies to show? y/n ")
    if intcount_choice == "y" or intcount_choice == "Y":
        intcount = int(input("How many word frequencies do you wish to see?  "))
    elif (intcount_choice == "n" or intcount_choice == "N"):
        print("By default frequency value is accepted as 20.")
        intcount = 20

    print("BOOK-1 ", Enter_input)
    print("NO   WORD   FREQUENCY")
    i = 0
    while (i < intcount):
        if (len(word_freq[i]) > 1):
            print(i + 1, "  ", word_freq[i][1], "  ", word_freq[i][0])
            i += 1
    
    stop=input('Press ENTER to exit')       
    print(stop)
elif(book_number==2):
    # Specify url of the web page
    book_two = input("Search 2nd book(Please enter uppercase and lowercase letters correctly.)  : ")
    booktwo_lists = book_two.split()
    b2element = "_".join(booktwo_lists)
    b2URL = "https://en.wikibooks.org/wiki/" + b2element + "/Print_version"
    b2source = urlopen(b2URL).read()
    print("Searched book url is: " + b2URL)

    b2soup = BeautifulSoup(b2source, 'lxml')

    # Extract the plain text content from paragraphs
    b2text = ''
    for paragraph in b2soup.find_all('body'):
        b2text += paragraph.text

    # Clean text
    b2text = re.sub(r'\[.*?\]+', '', b2text)
    b2text = b2text.replace('\n', '')

    file = open("ebookdata.txt", "a", encoding="utf-8")
    file.write(b2text)
    file.write(
        "\n\n*****************************************************************************************************\n\n")
    file.close()

    b2ntext = b2text.lower()

    for b2element in stop_words:
        b2ntext = b2ntext.replace(" " + b2element + " ", " ")

    # Cleaning text and lower casing all words
    for char in '”=*↑↑/{},[]&^<>_!-"#.½%$~();?|:\ \' \n':
        b2ntext = b2ntext.replace(char, ' ')
        ''.join(b2ntext.split())

    listToStr = b2ntext.lower()
    # split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s)
    b2_word_list = b2ntext.split()

    # Initializing Dictionary
    b2_d = {}
    # counting number of times each word comes up in list of words (in dictionary)
    for word in b2_word_list:
        b2_d[word] = b2_d.get(word, 0) + 1

    b2_word_freq = []
    for key, value in b2_d.items():
        b2_word_freq.append((value, key))
    b2_word_freq.sort(reverse=True)
    
    intcount_choice=input("Would you like to choose how many frequencies to show? y/n ")
    if intcount_choice=="y" or intcount_choice=="Y":
        intcount = int(input("How many word frequencies do you wish to see?  "))
    elif (intcount_choice=="n"or intcount_choice=="N"):
        print("By default frequency value is accepted as 20.")
        intcount=20




    #I am aware that this piece is problematic, but I couldn't think of anything to solve the problem. Sometimes incomplete or incorrect results can be printed.
    j = 0
    print("\nDISTINCT WORDS")
    print("BOOK-1 ", Enter_input)
    print("WORD   FREQUENCY")
    while (j < intcount):
        for strn in word_freq[j]:
            for list_ele in b2_word_freq:
                if j < intcount:
                    if strn != list_ele[1]:
                        print(list_ele[1], "    ", list_ele[0])
                        j += 1

    j = 0
    print("\nDISTINCT WORDS")
    print("BOOK-2 ", book_two)
    print("WORD   FREQUENCY")
    while (j < intcount):
        for strn in word_freq[j]:
            for list_ele in b2_word_freq:
                if j < intcount:
                    if strn != list_ele[1]:
                        print(word_freq[j][1], "    ", word_freq[j][0])
                        j += 1

    j = 0

    print("\nCOMMON WORDS")
    print("WORD   FREQUENCY-1   FREQUENCY-2   SUM")
    while(j<intcount):
        for strn in word_freq[j]:
            for list_ele in b2_word_freq:
                if strn == list_ele[1]:
                    print(list_ele[1],"     ", word_freq[j][0], "      ", list_ele[0], "     ",int(word_freq[j][0])+int(list_ele[0]))
                    j+=1

    stop=input('Press ENTER to exit')       
    print(stop)