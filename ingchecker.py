import my

counts = {}

with open('pap.txt') as book:
    for line in book:
        for word in my.cleanedup(line).split():
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
ingWords = []

for word in counts:
    if word[-3:] == 'ing':
        ingWords.append([counts[word], word])

ingWords.sort()
print(ingWords[-5:])
