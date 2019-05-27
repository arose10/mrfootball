import WSC

x = []
y = []

# Load the data & split it by line breaks
with open("data/train.txt") as t:
    new = t.read().split('\n')

# Split the data again but this time by a tab. This will make 0 the sequence & 1 the label
for i in range(len(new)):
    grab = new[i].split('\t')
    x.append(grab[0])
    y.append(grab[1])

# _sdd = WSC.CreateSeqDomainDictionary(x)

# print(_sdd)

dic = WSC.LoadSeq("config/SeqDomain.txt")
test = WSC.GetAllSeqCount("data/train.txt", dic)

print([test,y])