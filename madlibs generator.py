with open("story.txt","r") as f:
    story=f.read()
    print(story)
words=set()
start_of_word=-1
for i,char in enumerate(story):
    if char=="<":
        start_of_word=i
    if char==">" and start_of_word!=-1:
        word=story[start_of_word:i+1]
        start_of_word=-1
        words.add(word)
print(words)
answers={}
for word in words:
    answer=input("enter a word for "+word+":")
    answers[word]=answer
for answer in answers:
    story=story.replace(answer,answers[answer])

print(story)





