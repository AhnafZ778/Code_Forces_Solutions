import sys
import heapq


input = sys.stdin.readline

number = int(input())

words = []
for _ in range(number):
    word = input()
    word = word.strip()
    words.append(word)

present_words = set()

for i in words:
    present_words.update(i)

adjacency_list = [[] for _ in range(26)]
indegree = [0] * 26

for i in range(number - 1):
    word_1, word_2 = words[i], words[i + 1]
    least = min(len(word_1), len(word_2))
    count = 0
    while count < least and word_1[count] == word_2[count]:
        count += 1
    if count == least:
        if len(word_1) > len(word_2):
                print(-1)
                exit()
        continue        
    a = ord(word_1[count])-97
    b = ord(word_2[count])-97
    adjacency_list[a].append(b)
    indegree[b] += 1

min_heap = []

for i in present_words:
    num = ord(i)-97
    if indegree[num] == 0:
        heapq.heappush(min_heap, num)
        
order = []

remaining = {ord(i)-97 for i in present_words}


while min_heap:
    u = heapq.heappop(min_heap)
    if u not in remaining:
        continue
    order.append(u)
    remaining.remove(u)
    for i in adjacency_list[u]:
        indegree[i] -= 1
        if indegree[i] == 0 and i in remaining:
            heapq.heappush(min_heap, i)
        
if remaining:
    print(-1)
        
else:
    for i in order:
        print(chr(i+97), end = "")