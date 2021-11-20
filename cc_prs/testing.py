start_old=set()
end_old=set()
start_new=set()
end_new=set()


minor_dict={}

oldfiles1=["/u/home/s/sarahjs3/eeskin2/CHD/new/Lifted.common.heart_valve_problem_or_heart_murmur.bed","/u/home/s/sarahjs3/eeskin2/CHD/new/Lifted.common.heart_arrhythmia.bed","/u/home/s/sarahjs3/eeskin2/CHD/new/Lifted.common.abnormalities_of_heart_beat.txt"]
oldfiles2=["fix2.Lifted.common.heart_valve_problem_or_heart_murmur.txt","fix2.Lifted.common.heart_arrhythmia.txt","fix2.Lifted.common.abnormalities_of_heart_beat.txt"]
oldfiles0=["/u/home/s/sarahjs3/eeskin2/CHD/NealeLab/chd/both/20002_1078.gwas.imputed_v3.both_sexes.txt","/u/home/s/sarahjs3/eeskin2/CHD/NealeLab/chd/both/20002_1077.gwas.imputed_v3.both_sexes.txt","/u/home/s/sarahjs3/eeskin2/CHD/NealeLab/chd/both/R00.gwas.imputed_v3.both_sexes.txt"]

indexes=[0,1,2]
for i in indexes:
    myout=open(oldfiles2[i],"w")
    first=True
    with open(oldfiles0[i],"r") as myin:
        for line in myin.readlines():
            if first:
                first=False
            else:
                line2=line.strip().split()
                snp=line2[0].split(":")
                snp2=snp[0]+":"+snp[1]
                min=line2[1]
                if snp2 in minor_dict:
                    stuff=minor_dict[snp2]
                    if min not in stuff:
                        #print(snp2)
                        minor_dict[snp2].append(min)
                else:
                    minor_dict[snp2]=[min]
    print(minor_dict[snp2])
    first=True
    numdup=0
    with open(oldfiles1[i],"r") as myin:
        for line in myin.readlines():
            if first:
                first=False
                myout.write("CHR\tBP\tA1\tA2\tSNP\tP\tBETA\n")
            else:
                line2=line.strip().split()

                chr=line2[0].strip()[3:]
                start=line2[1].strip()
                end=line2[2].strip()
                P=line2[5].strip()
                Beta=line2[6].strip()

                snp=line2[4].strip().split(":")
                snp2=snp[0]+":"+snp[1]
                a1b=snp[2]
                a2b=snp[3]
                a1=line2[7].strip()
                a2=line2[8].strip()
                minor=minor_dict[snp2]
                start_old.add("chr"+chr+":"+start)
                end_old.add("chr"+chr+":"+end)

                snpid="chr"+chr+":"+start
                A1=""
                A2=""
                if len(minor)>1:
                    for i in range(0,len(minor)):
                        if a1==minor[i] and a2!=minor[i]:
                            if A1!="":
                                numdup+=1    
                            #    print("prob1"+line+"_"+minor[i]+"_"+A1)
                            else:
                                A1=a1
                                A2=a2
                        elif a2==minor[i] and a1!=minor[i]:
                            if A1!="":
                                temp=""
                                #numdup+=1
                                #print("prob2"+line+"_"+minor[i]+"_"+A1)
                            else:
                                A1=a2
                                A2=a2
                        elif a2==minor[i] and a1==minor[i]:
                            print("prob3"+line+"_"+minor[i]+"_"+A1)
                        elif a2!=minor[i] and a1!=minor[i]:
                            temp=""
                        else:
                            print("prob4??"+line)
                    if A1!="" and A2!="":
                        outline=chr+"\t"+start+"\t"+A1+"\t"+A2+"\t"+snpid+"\t"+P+"\t"+Beta+"\n"
                        myout.write(outline)
                    #else:
                    #    print(minor+"____"+chr+"\t"+start+"\t"+A1+"\t"+A2+"\t"+snpid+"\t"+P+"\t"+Beta+"\n")
                    #    #write to output file putting minor as effective allele. also make list of start and end positions so can count how many overlap with plink bim. also make sure snpid is right. start using start allele
                else:
                    if a1==minor[0] and a2!=minor[0]:
                        A1=a1
                        A2=a2
                    elif a2==minor[0] and a1!=minor[0]:
                        A1=a2
                        A2=a2
                    elif a2!=minor[0] and a1!=minor[0]:
                        print("prob5 none"+minor[0]+"_"+a1+"_"+a2+"_"+a1b+"_"+a2b)
                    else:
                        print("prob5"+minor[0]+"_"+a1+"_"+a2+"_"+a1b+"_"+a2b)
                    if A1!="" and A2!="":
                        outline=chr+"\t"+start+"\t"+A1+"\t"+A2+"\t"+snpid+"\t"+P+"\t"+Beta+"\n"
                        myout.write(outline)
                    #else:
                        #print(minor)
                        #print(minor[0]+"_"+a1+"_"+a2+"_"+a1b+"_"+a2b)
                        #print(A1+"_"+A2+"____"+chr+"\t"+start+"\t"+A1+"\t"+A2+"\t"+snpid+"\t"+P+"\t"+Beta+"\n")
    print(numdup)
    myout.close()
for e in start_old:
    break
print(e)
for e in end_old:
    break
print(e)

newfiles1=["fix.Lifted.common.heart_valve_disorders.txt","fix.Lifted.common.abnormal_heart_sounds.txt"]
newfiles2=["fix2.Lifted.common.heart_valve_disorders.txt","fix2.Lifted.abnormal_heart_sounds.txt"]

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
