text = input().upper()
text_list = list(set(text))
count_num = []
for i in text_list:
    num = text.count(i)
    count_num .append(num)
if count_num.count(max(count_num)) >= 2 : 
    print("?")
else : print(text_list[(count_num.index(max(count_num)))])
