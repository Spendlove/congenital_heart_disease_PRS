infiles1=["20002_1078.gwas.imputed_v3.both_sexes.tsv","20002_1077.gwas.imputed_v3.both_sexes.tsv","R00.gwas.imputed_v3.both_sexes.tsv"]
outfiles=["noheader.common.heart_valve.txt","noheader.common.heart_arr.txt","noheader.common.heart_beat.txt"]

indexes=[0,1,2]

for i in indexes:
    first=True
    myout=open(outfiles[i],"w")
    with open(infiles1[i],"r") as myin:
        for line in myin.readlines():
            if first:
                first=False
            else:
                line2=line.strip().split("\t") 
                maf=float(line2[2])
                stuff=line2[0].split(":")
                bp=stuff[1]
                chrm=stuff[0]
                snp="chr"+chrm+":"+bp
                info="chr"+chrm+"\t"+str(int(bp)-1)+"\t"+str(int(bp))+"\t"
                line3=info+line.strip()+"\t"+snp+"\n"
                if maf >= 0.05:
                    myout.write(line3)
                if 1.0-maf < 0.05:
                    print("PROBLEM")
                    print(line)
    myout.close()


infiles2=["PheCode_395_SAIGE_MACge20.txt.vcf","PheCode_396_SAIGE_MACge20.txt.vcf","PheCode_395.6_SAIGE_MACge20.txt.vcf","PheCode_747_SAIGE_MACge20.txt.vcf"]
outfiles2=["noheader.common.valve_dis.txt","noheader.common.heart_sounds.txt","noheader.common.valve_replaced.txt","noheader.common.congenital_abnormalities.txt"]
indexes=[0,1,2,3]

for i in indexes:
    first=True
    myout=open(outfiles2[i],"w")
    with open(infiles2[i],"r") as myin:
        for line in myin.readlines():
            line2=line.strip().split("\t")
            af=line2[6]
            bp=line2[1].strip()
            chrm=line2[0].strip()
            snp="chr"+chrm+":"+bp
            if first:
                first=False
            else:
                info="chr"+chrm+"\t"+str(int(bp)-1)+"\t"+str(int(bp))+"\t"
                line3=info+line.strip()+"\t"+snp+"\n"
                if float(af)>=0.05:
                    if (1.0-float(af)) >=0.05:
                        myout.write(line3)
    myout.close()
