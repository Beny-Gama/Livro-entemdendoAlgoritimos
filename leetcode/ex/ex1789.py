# leetcode 1789
word1, word2 = "abce", "pq"
fra = ''
        
for l1, l2 in zip(word1, word2):
    fra += l1 + l2
    
print(fra)