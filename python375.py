dataset = []
listof = []
ress = 0
with open("dataset_3380_5.txt") as file1:
    for line in file1:
        dataset.append(line.split("\t"))

data = {k: [] for k in range(1,12,1)}

# print(data.keys())
# print(data.values())



for i in dataset:
    # print (i[1])
    # print(data[int(i[0])])
    listof = data[int(i[0])]
    listof.append(int(i[2]))
    data[int(i[0])]=listof

# data[2]=[]

# print(len(data[2]))
# print(data.items())

for i in range(1,12):
    tmp_e = list(data[i])
    ress = 0
    for j in tmp_e:
        ress += j
    if len(tmp_e) > 0:
        # ress = float(ress)
        ress /= (len(tmp_e))
        data[i]=ress
    else:
        data[i] = "-"
    print(i,data[i])



# print(data.items())