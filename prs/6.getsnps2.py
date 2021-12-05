
allfiles=["eur_HEART_VALVE","eur100_HEART_VALVE","eur100_Heart_Sounds","eur_Heart_Sounds","sev_eur100_HEART_VALVE","sev_eur_HEART_VALVE","sev_eur100_Heart_Sounds","sev_eur_Heart_Sounds","eur_HEART_BEAT","eur100_HEART_BEAT","sev_eur_HEART_BEAT","sev_eur100_HEART_BEAT","eur_Valve_Dis","eur100_Valve_Dis","sev_eur_Valve_Dis","sev_eur100_Valve_Dis","eur_HEART_ARR","eur100_HEART_ARR","sev_eur100_HEART_ARR","sev_eur_HEART_ARR"]
gwas_dict={"eur_HEART_VALVE":"fix2.Lifted.common.heart_valve_problem_or_heart_murmur.txt","eur100_HEART_VALVE":"fix2.Lifted.common.heart_valve_problem_or_heart_murmur.txt","sev_eur100_HEART_VALVE":"fix2.Lifted.common.heart_valve_problem_or_heart_murmur.txt","sev_eur_HEART_VALVE":"fix2.Lifted.common.heart_valve_problem_or_heart_murmur.txt","eur100_Heart_Sounds":"fix2.Lifted.common.abnormal_heart_sounds.txt","eur_Heart_Sounds":"fix2.Lifted.common.abnormal_heart_sounds.txt","sev_eur100_Heart_Sounds":"fix2.Lifted.common.abnormal_heart_sounds.txt","sev_eur_Heart_Sounds":"fix2.Lifted.common.abnormal_heart_sounds.txt","eur_HEART_BEAT":"fix2.Lifted.common.abnormalities_of_heart_beat.txt","eur100_HEART_BEAT":"fix2.Lifted.common.abnormalities_of_heart_beat.txt","sev_eur_HEART_BEAT":"fix2.Lifted.common.abnormalities_of_heart_beat.txt","sev_eur100_HEART_BEAT":"fix2.Lifted.common.abnormalities_of_heart_beat.txt","eur_Valve_Dis":"fix2.Lifted.common.heart_valve_disorders.txt","eur100_Valve_Dis":"fix2.Lifted.common.heart_valve_disorders.txt","sev_eur_Valve_Dis":"fix2.Lifted.common.heart_valve_disorders.txt","sev_eur100_Valve_Dis":"fix2.Lifted.common.heart_valve_disorders.txt","eur_HEART_ARR":"fix2.Lifted.common.heart_arrhythmia.txt","eur100_HEART_ARR":"fix2.Lifted.common.heart_arrhythmia.txt","sev_eur100_HEART_ARR":"fix2.Lifted.common.heart_arrhythmia.txt","sev_eur_HEART_ARR":"fix2.Lifted.common.heart_arrhythmia.txt"}
gwas=["fix2.Lifted.common.heart_valve_problem_or_heart_murmur.txt","fix2.Lifted.common.abnormal_heart_sounds.txt","fix2.Lifted.common.abnormalities_of_heart_beat.txt","fix2.Lifted.common.heart_valve_disorders.txt","fix2.Lifted.common.heart_arrhythmia.txt"]

gwas_dict2={}
for name in gwas:
    first=True
    with open(name,"r") as myin:
        for line in myin.readlines():
            if first:
                first=False
                gwas_dict2[name]={}
            else:
                line2=line.strip().split("\t")
                alt=line2[2]
                snp=line2[4]
                p=line2[5]
                beta=line2[6]
                mystring=""
                if snp not in gwas_dict2[name]:
                    mystring=mystring+alt+":"+p+":"+beta
                    gwas_dict2[name][snp]=mystring
                else:
                    mystring=gwas_dict2[name][snp]+"_"+alt+":"+p+":"+beta
                    gwas_dict2[name][snp]=mystring

pval={}
pop={}
for name in allfiles:
    with open(name+".summary","r") as myin:
        for line in myin.readlines():
            line2=line.strip().split()
            if line2[0].strip()=="-":
                threshold=line2[2]
                pval[name]=threshold
                if name[3]=="1":
                    pop[name]="eur100"
                elif name[3]=="_":
                    if name[0]=="e":
                        pop[name]="eur"
                    elif name[0]=="s":
                        if name[7]=="1":
                            pop[name]="eur100"
                        elif name[7]=="_":
                            pop[name]="eur"
                        else:
                            print(name)
                else:
                    if name[6]=="1":
                        pop[name]="noneur100"
                    elif name[6]=="_":
                        pop[name]="noneur"
                    else:
                        print(name)


#eurM=set()
#eurF=set()
#noneurM=set()
#noneurF=set()
firstline=True
allgenes=[]
firstline2=True
#for each line in genes.all.txt, go through all the SNPs in each list
with open("genes.all.file") as myin:
    for line in myin.readlines():
        if firstline2:
            firstline2=False
        else:
            line2=line.strip().split("\t")
            chr=line2[2]
            start=float(line2[3])
            end=float(line2[4])
            gene=line2[0]
            info=[gene,chr,start,end]
            allgenes.append(info)
print(len(allgenes))
mydict={'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[],'10':[],'11':[],'12':[],'13':[],'14':[],'15':[],'16':[],'17':[],'18':[],'19':[],'20':[],'21':[],'22':[],'X':[]}
for g in allgenes:
    name=g[0]
    chr=g[1]
    s=g[2]
    e=g[3]
    if chr in mydict:
        mydict[chr].append([name,s,e])
print(len(mydict['17']))
    
#with open("eurM.bim","r") as myin:
#    for line in myin.readlines():
#        line2=line.strip().split()
#        snp=line2[1].strip()
#        eurM.add(snp)
#        if firstline:
#            print(line)
#            print(line2)
#            print(snp)
#            firstline=False
#with open("noneurM.bim","r") as myin:
#    for line in myin.readlines():
#        line2=line.strip().split()
#        snp=line2[1].strip()
#        noneurM.add(snp)
#with open("eur100.bim","r") as myin:
#    for line in myin.readlines():
#        line2=line.strip().split()
#        snp=line2[1].strip()
#        eurF.add(snp)
#with open("noneur100.bim","r") as myin:
#    for line in myin.readlines():
#        line2=line.strip().split()
#        snp=line2[1].strip()
#        noneurF.add(snp)
#print(len(eurM))
#print(len(eurF))
#print(len(noneurM))
#print(len(noneurF))
##print(eurM)
for prefix in allfiles:
    n=0
    sum=0.0
    mypop=pop[prefix]
    infile=prefix+".snp"
    outfile=prefix+".snp3"
    #outfile2=open(prefix+".snpMarlin","w")
    #outfile3=open(prefix+".snpFetal","w")
    myout=open(outfile,"w")
    first=True
    with open(infile,"r") as myin:
        for line in myin.readlines():
            line2=line.strip().split()
            if first:
                myout.write(line.strip()+"\tGenes\tAlt:P:Beta\n")
                first=False
            else:
                chr=line2[0]
                bp=float(line2[2])
                p=float(line2[3])
                snp=line2[1].strip()
                threshold=float(pval[prefix])
                if p < threshold:
                    genename=""
                    for gene in mydict[chr]:
                            if bp > float(gene[1]) and bp < float(gene[2]):
                                genename=genename+gene[0]+" "
                    #if genename!="":
                    #    print(genename)
                    gname=gwas_dict[prefix]
                    stuff=""#("","")
                    if snp in gwas_dict2[gname]:
                        stuff=gwas_dict2[gname][snp]
                    stuff2=stuff.split(":")
                    beta=stuff2[2]
                    n+=1
                    sum+=float(beta)
                    line3=line.strip()+"\t"+genename+"\t"+stuff+"\n"
                    myout.write(line3)
                    #if mypop=="eur":
                    #    if snp in eurM:
                    #        outfile2.write(line)
                    #    if snp in eurF:
                    #        outfile3.write(line)
                    #elif mypop=="noneur":
                    #    if snp in noneurM:
                    #        outfile2.write(line)
                    #    if snp in noneurF:
                    #        outfile3.write(line)
    print(prefix+"\t"+str(sum/n))
    myout.close()
#    outfile2.close()
#    outfile3.close()

