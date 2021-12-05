import sys
file1="eur_HEART_VALVE.snp3"
file2="eur100_HEART_VALVE.snp3"
allsnv=set()
fetalsnb=set()
overlap=set()
first=True
with open(file1,"r") as myin:
    for line in myin.readlines():
        if first:
            first=False
        else:
            line2=line.strip().split("\t")
            if len(line2)>5:
                genes=line2[5].split(" ")
                for g in genes:
                    allsnv.add(g)
first=True
with open(file2,"r") as myin:
    for line in myin.readlines():
        if first:
            first=False
        else:
            line2=line.strip().split("\t")
            if len(line2)>5:
                genes=line2[5].split(" ")
                for g in genes:
                    fetalsnb.add(g)
                    if g in allsnv:
                        overlap.add(g)
print("ALL SNV")
print(len(allsnv))
#print(allsnv)

print("fetal")
print(len(fetalsnb))
#print(fetalsnb)

print("overlap")
print(len(overlap))

myout=open("sigPRSgenes.csv","w")
myout2=open("sigPRSgenes_overlap.csv","w")
for gene in allsnv:
    myout.write("All SNV,"+gene+"\n")
for gene in fetalsnb:
    myout.write("Fetal SNV,"+gene+"\n")
for gene in overlap:
    myout2.write("Overlap,"+gene+"\n")
myout.close()
myout2.close()
