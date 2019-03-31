# coding=gbk

true_test = True
false_test = False

print(type(true_test))

print(8 == 8)
print(8 != 8)
print("a" != "a")
print("a" == "a")
print(["a", "b", "c"] == ["a", "b", "c"])
print(["a", "b", "c"] == ["a1", "b1", "c1"])

intTest = [10, 15, 20]

print(intTest[0] >= intTest[1])

intTest1 = 500
bool1 = (intTest1 > 100)
if 100:
    print("true")
else:
    print("false") 
    
strAgs = ["a", "b", "c"]
for str1 in strAgs:
    if str1 == "a":
        print("在")

if "a" in strAgs:
    print("在")

