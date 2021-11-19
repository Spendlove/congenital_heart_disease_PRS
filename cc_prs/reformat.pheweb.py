
import sys
out1=open("noheader.common.heart_valve_disorders.txt","w")
out2=open("noheader.common.abnormal_heart_sounds.txt","w")
first=True
firstline="chrom\tchromStart\tchromEnd\tCHROM\tPOS\tID\tREF\tALT\tac\taf\tnum_cases\tnum_controls\tbeta\tsebeta\tTstat\tpval\tpval_SAIGE_NoSPA\tIs_Converged\tvarT\tvarTstar\tsnp\n"
with open("PheCode_395_SAIGE_MACge20.txt.vcf","r") as myin:
    for line in myin.readlines():
        line2=line.strip().split("\t")
        af=line2[6]
        snp="chr"+line2[0].strip()+":"+line2[1].strip()
        bp=line2[1].strip()
        if first:
            first=False
            #out1.write(firstline)
        else:
            info="chr"+line2[0].strip()+"\t"+str(int(bp)-1)+"\t"+str(int(bp))+"\t"
            line3=info+line.strip()+"\t"+snp+"\n"
            if float(af)>=0.05:
                out1.write(line3)
first=True
with open("PheCode_396_SAIGE_MACge20.txt.vcf","r") as myin:
    for line in myin.readlines():
        line2=line.strip().split("\t")
        af=line2[6]
        snp="chr"+line2[0].strip()+":"+line2[1].strip()
        bp=line2[1].strip()
        if first:
            first=False
            #out2.write(firstline)
        else:
            info="chr"+line2[0].strip()+"\t"+str(int(bp)-1)+"\t"+str(int(bp))+"\t"
            line3=info+line.strip()+"\t"+snp+"\n"
            if float(af)>=0.05:
                out2.write(line3)
