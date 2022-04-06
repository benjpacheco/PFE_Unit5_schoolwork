import my
import os

def findMentions(item):
    counts = {}
    with open(item, encoding='utf-8') as tweets:
        for line in tweets:
             for word in my.cleanedup(line).split():
                 if word in counts:
                    counts[word] += 1
                 else:
                    counts[word] = 1
    mentions = []
    for word in counts:
        if word[0] == '@':
            mentions.append([counts[word], word])
    mentions.sort()
    print('   ', mentions[-5:])

# its not a funtion
file_list = []
for filename in os.listdir('.'):
    if filename.endswith((".tweet", "_files")):
        file_list.append(filename)
    for item in file_list:
        findMentions(item)
