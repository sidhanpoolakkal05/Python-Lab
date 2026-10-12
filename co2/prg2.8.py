def longestword(word):
    max_length=len(word[0])
    for item in word:
        length=len(item)
        if length>max_length:
            max_length=length
        return max_length
words=input("enter a list of words seperated by spaces:")
words=words.split()
result=longestword(words)
print(f"The length of the longest word is:{result}")
