start_old=set()
end_old=set()
start_new=set()
end_new=set()


minor_dict={}

oldfiles1=["fix.Lifted.common.heart_valve_problem_or_heart_murmur.txt","fix.Lifted.common.heart_arrhythmia.txt","fix.Lifted.common.abnormalities_of_heart_beat.txt"]
oldfiles2=["fix2.Lifted.common.heart_valve_problem_or_heart_murmur.txt","fix2.Lifted.common.heart_arrhythmia.txt","fix2.Lifted.common.abnormalities_of_heart_beat.txt"]

indexes=[0,1,2]
for i in indexes:
    myout=open(oldfiles2[i],"w")
    first=True
    with open(oldfiles1[i],"r") as myin:
        for line in myin.readlines():
            if first:
                first=False
                myout.write("CHR BP ALT REF SNP P BETA\n")
            else:
                line2=line.strip().split()
                chr=line2[0]
                start=line2[1]
                end=line2[2]
                stuff=line2[3].split(":")
                c=stuff[0]
                start_old.add(chr+":"+start)
                end_old.add(chr+":"+end)
                ref=stuff[2]
                alt=stuff[3]
                p=line2[14]
                snp=chr+":"+str(end)
                beta=line2[11]
                myout.write(c+"\t"+end+"\t"+alt+"\t"+ref+"\t"+snp+"\t"+p+"\t"+beta+"\n")
    myout.close()
for e in start_old:
    break
print(e)
for e in end_old:
    break
print(e)

newfiles1=["fix.Lifted.common.heart_valve_disorders.txt","fix.Lifted.common.abnormal_heart_sounds.txt"]
newfiles2=["fix2.Lifted.common.heart_valve_disorders.txt","fix2.Lifted.common.abnormal_heart_sounds.txt"]

indexes=[0,1]
for i in indexes:
    myout=open(newfiles2[i],"w")
    first=True
    with open(newfiles1[i],"r") as myin:
        for line in myin.readlines():
            if first:
                first=False
                myout.write("chrom\tchromEnd\tALT\tREF\tsnp\tpval\tbeta\n") 
            else:
                line2=line.strip().split()
                alt=line2[7]
                ref=line2[6]
                chr=line2[0].strip()
                start=line2[1].strip()
                end=line2[2].strip()
                p=line2[15]
                beta=line2[12]

                start_new.add(chr+":"+start)
                end_new.add(chr+":"+end)
            
                snp=chr+":"+end
                snpid=chr+":"+end
                pos=end
                myout.write(chr+"\t"+pos+"\t"+alt+"\t"+ref+"\t"+snpid+"\t"+p+"\t"+beta+"\n")
                #write to output file putting new SNP id.also make list of start and end positions so can count how many overlap with plink bim. start using end allele.
myout.close()
so=0
eo=0
sn=0
en=0
with open("eur.bim") as myin:
    for line in myin.readlines():
        line2=line.strip().split()
        snp=line2[1]
        if snp in start_old:
            so+=1
        if snp in end_old: 
            eo+=1
        if snp in start_new:
            sn+=1
        if snp in end_new:
            en+=1
print("Oldfiles, starting pos")
print(so)
print("Oldfiles, ending position")
print(eo)
print("Newfiles, starting pos")
print(sn)
print("Newfiles, ending position")
print(en)
#print out numbers        
