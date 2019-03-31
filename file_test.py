# coding=gbk

# f = open("test.txt", "r", encoding='UTF-8')
# g = f.read();
# print(g)
# f.close();
# 
# w = open("test1.txt", "w", encoding='UTF-8')
# w.write("app")
# w.write("\n")
# w.write("123")
# w.write("\n")
# w.write(g)
# w.close()
# 
# f = open("test1.txt", "r", encoding='UTF-8')
# g = f.read();
# print(g)
# f.close();


ex_test1 = []
f = open("dddd.csv", "rb")
data = f.read()
print(data)
rows = data.split('\n')
for row in rows:
    split_row = row.split(",")
    ex_test1.appent(split_row)
print(ex_test1)




# 
# sample = "john,plastic,joe "
# split_list = sample.split(",")
# print(split_list)