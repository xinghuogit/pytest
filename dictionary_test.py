# coding=gbk

names = ["a1", "b1", "c1"]
scores = [51, 61, 71]
scores1 = [0, 1, 2]
name = "a1"
for i in scores1:
    if names[i] == name: 
        print(scores[i])

dictTest = {}
print(type(dictTest))
dictTest["a1"] = 51
dictTest["b1"] = 61
dictTest["b1"] = 67
dictTest["c1"] = 71
print(dictTest.keys())
print(dictTest.values())
print(dictTest)
print(dictTest["a1"])

dictTest1 = {}
dictTest1["a1"] = 51
dictTest1["b1"] = 61
print(dictTest1)

dictTest1 = {
    "a1":51,
    "c1":612444444444444444444444,
    "b1":612444444444444444444444
}
print(dictTest1)

dictTest1["c1"] = dictTest1["c1"] + 5
print(dictTest1)

print("a1" in dictTest1)

names1 = ["a1", "b1", "c1", "b1"]
print(names1)
names1_counts = {}

for item in names1:
    if item in names1_counts:
        names1_counts[item] = names1_counts[item] + 1
    else:
        names1_counts[item] = 1
print(names1_counts) 

