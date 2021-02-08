sentence = input("Please Enter your sentence to analyze: ")
result = dict()
list_sentence = list(sentence)
for i in list_sentence:
    result.update({i : list_sentence.count(i)})
print(result)
