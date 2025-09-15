from pyvi import ViTokenizer, ViPosTagger

f = open("Vietnamese.txt", mode ="r", encoding="utf-8")
text= f.readlines()

words=dict({})
for l in text:
    l= ViTokenizer.tokenize(l)
    ws=l.split()
    for w in ws:
        if w in words:
            words[w] = words[w]+1
        else:
            words.update({w:1})
f.close()

for w in words.keys():
    print(f"{w} xuất hiện {words[w]}")

print(f"\n Số từ trong bộ dữ liệu {len(words.keys())}")


