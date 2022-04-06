import os

def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz@1234567_'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def findMentions(filename):
    counts = {}
    with open(filename, encoding='utf-8') as tweets:
        for line in tweets:
            for word in cleanedup(line).split():
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
    mentions = []
    for word in counts:
        if word[0] == '@':
            mentions.append([counts[word], word])
    mentions.sort()
    for at in mentions[-5:]:
        print('   ', at[1], at[0])
        
for file in os.listdir('.'):
    if file[-6:] == '.tweet':
        print(file)
        findMentions(file)
        print(' ')






