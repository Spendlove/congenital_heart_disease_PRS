import sys


allfiles=["eur_HEART_VALVE","eur100_HEART_VALVE","eur100_Heart_Sounds","eur_Heart_Sounds","sev_eur100_HEART_VALVE","sev_eur_HEART_VALVE","sev_eur100_Heart_Sounds","sev_eur_Heart_Sounds","eur_HEART_BEAT","eur100_HEART_BEAT","sev_eur_HEART_BEAT","sev_eur100_HEART_BEAT","eur_Valve_Dis","eur100_Valve_Dis","sev_eur_Valve_Dis","sev_eur100_Valve_Dis","eur_HEART_ARR","eur100_HEART_ARR","sev_eur100_HEART_ARR","sev_eur_HEART_ARR"]

ALLsnvs=set()
allsnvs_info={}

eur_CHD=set()
eur_Fetal=set()
eur=set()
with open("eur.bim","r") as myin:
    for line in myin.readlines():
        line2=line.strip().split()
        snp=line2[1].strip()
        eur.add(snp)
with open("eurM.bim","r") as myin:
    for line in myin.readlines():
        line2=line.strip().split()
        snp=line2[1].strip()
        eur_CHD.add(snp)
with open("eur100.bim","r") as myin:
    for line in myin.readlines():
        line2=line.strip().split()
        snp=line2[1].strip()
        eur_Fetal.add(snp)

snv_sets={}
snv_data={}
snv_genes={}
for name in allfiles:
    file1=name+".snp3"
    first=True
    with open(file1,"r") as myin:
        for line in myin.readlines():
            if first:
                first=False
                snv_sets[name]=set()
                snv_data[name]=[0,0,0]
            else:
                line2=line.strip().split("\t")
                snp=line2[1]
                ALLsnvs.add(snp)
                if snp in allsnvs_info:
                    allsnvs_info[snp].append(name)
                else:
                    allsnvs_info[snp]=[name]
                if snp in eur:
                    snv_data[name][0]+=1
                else:
                    print("PROBLEM! snp"+snp+" not in eur.bim")
                if snp in eur_CHD:
                    snv_data[name][1]+=1
                if snp in eur_Fetal:
                    snv_data[name][2]+=1
                if line2[5]!="-":
                    genes=line2[5].split(" ")
                    for g in genes:
                        if snp in snv_genes:
                            placeholder=""
                        else:
                            snv_genes[snp]=set()
                        snv_genes[snp].add(g)
                        snv_sets[name].add(g)
        print("____________"+name+"_________________")
        print("Num Genes")
        print(len(snv_sets[name]))
        print("All SNVs: "+str(snv_data[name][0])+" CHD SNVs: "+str(snv_data[name][1])+" Fetal SNVs: "+str(snv_data[name][2]))
myout=open("sig_and_nom_PRS_SNVS.txt","w")
myout.write("SNP\tGenes\tPRS_this_SNV_is_present_in\n")

signames=["eur_HEART_VALVE","eur100_HEART_VALVE","eur_Heart_Sounds","sev_eur100_HEART_VALVE","sev_eur_HEART_VALVE","sev_eur_Heart_Sounds","sev_eur100_HEART_ARR"]
signames2={"eur_HEART_VALVE":"CC_Heart_Valve_all_SNVs","eur100_HEART_VALVE":"CC_Heart_Valve_Fetal_cardiac","eur_Heart_Sounds":"CC_Heart_Sounds_all_SNVs","sev_eur100_HEART_VALVE":"Sev_Heart_Valve_Fetal_cardiac","sev_eur_HEART_VALVE":"Sev_Heart_Valve_all_SNVs","sev_eur_Heart_Sounds":"Sev_Heart_Sounds_all_SNVs","sev_eur100_HEART_ARR":"Sev_Heart_ARR_Fetal_cardiac"}
for snp in ALLsnvs:
    info=allsnvs_info[snp]
    mystr=""
    towrite={}
    for name in info:
        mystr2=""
        if name in signames:
            name2=signames2[name]
            if mystr=="":
                mystr=name2
            else:
                mystr=mystr+","+name2
            if snp in snv_genes:
                for g in snv_genes[snp]:
                    if mystr2=="":
                        mystr2=g
                    else:
                        mystr2=mystr2+","+g
            else:
                mystr2="-"
            myline=snp+"\t"+mystr2+"\t"+mystr+"\n"
            towrite[snp]=myline
    for snp in towrite:
        myline=towrite[snp]
        myout.write(myline)

#myout=open("sigPRSgenes.csv","w")
#myout2=open("sigPRSgenes_overlap.csv","w")
#for gene in allsnv:
#    myout.write("All SNV,"+gene+"\n")
#for gene in fetalsnb:
#    myout.write("Fetal SNV,"+gene+"\n")
#for gene in overlap:
#    myout2.write("Overlap,"+gene+"\n")
#myout.close()
#myout2.close()
