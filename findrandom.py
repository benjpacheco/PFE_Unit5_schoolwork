import os

def contains(filename, pattern):
    with open(filename, encoding='utf-8') as file:
        for line in file:
            if pattern in line:
                return True
        
    return False


for filename in os.listdir('.'):
    if contains(filename, 'random'):
        print(filename, 'contains random')
        
