sentence=input("Tell me a sentence: ")
print(sentence.split())
print(len(sentence.split()))
number_words=0
ex_words="S"
for words in sentence:
    if number_words==0:
        number_words=+1
        if words == " "and words !=ex_words :
                number_words= number_words+1
        ex_words=words
print("This sentence contains", number_words, "words!")
