data= ["marios", "didos", "peking chef", "southern china", "dominos"]

times = 0

def find(item, times):
    for i in range(len(data)):
        if item == data[i]:
            times = times + 1
        else:
            times = times
    return (times)


item = input("name a takeaway: ")
result = find(item, times)
print(result)




def find2(item, times):
    for i in data:
        if item == i:
            times += 1
    return ()



names = ["abby", "abby", "abby", "bella", "charlie", "charlie", "donnie", "ella"]

times = 0

def checklist(times, pick_name):
    for i in range(len(names)):
        if pick_name == names[i]:
            times = times + 1
        else:
            times = times
    return times

pick_name = input("pick a name: ")
result = checklist(times, pick_name)
print(result)

#

fruits = ["apple", "banana", "cherry", "orange", "pear"]

items = 0

for x in data:
    items += 1
    print(items)

def find(items, choose):
    for i in data:
        if choose == i:
            items += 1
            print(items)

choose = input("pick a fruit: ")
result = find(items, choose)
print(result)



