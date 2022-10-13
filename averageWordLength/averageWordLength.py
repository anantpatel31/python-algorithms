# return the average word length of a given sentence
sentence1 = input("Type a sentence: ")

def solution(sentence):
    
    # removing punctuation
    for p in "!?',;.":
        sentence = sentence.replace(p, '')
    words = sentence.split()
    return round(sum(len(word) for word in words)/len(words),2)
    
# we need to convert float into string in order to concatenate 
print("Average of " + str(solution(sentence1)) + " characters per word.");