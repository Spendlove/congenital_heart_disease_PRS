
allfiles=["eur_HEART_VALVE","eur100_HEART_VALVE","eur100_Heart_Sounds","eur_Heart_Sounds","sev_eur100_HEART_VALVE","sev_eur_HEART_VALVE","sev_eur100_Heart_Sounds","sev_eur_Heart_Sounds","eur_HEART_BEAT","eur100_HEART_BEAT","sev_eur_HEART_BEAT","sev_eur100_HEART_BEAT","eur_Valve_Dis","eur100_Valve_Dis","sev_eur_Valve_Dis","sev_eur100_Valve_Dis","eur_HEART_ARR","eur100_HEART_ARR","sev_eur100_HEART_ARR","sev_eur_HEART_ARR"]

cc_status={}
with open("../cc_prs/pheno.txt") as myin:
    for line in myin.readlines():
        line2=line.strip().split()
        pid=line2[1]
        pheno=line2[5]
        if pheno=="2":
            pheno="Case"
        elif pheno=="1":
            pheno="Control"
        cc_status[pid]=pheno
sev_status={}
sev_status2={}
with open("../cc_prs/sev.pheno.txt") as myin:
    for line in myin.readlines():
        line2=line.strip().split()
        pid=line2[1]
        pheno=line2[5]
        sev_status2[pid]=pheno
        if pheno=="0":
            pheno="Control"
        elif pheno=="1":
            pheno="Mild"
        elif pheno=="2":
            pheno="Moderate"
        elif pheno=="3":
            pheno="Severe"
        sev_status[pid]=pheno
for name in allfiles:
    with open(name+".best","r") as myin:
        myout=open(name+".best.edit2.csv","w")
        first=True
        for line in myin.readlines():
            line2=line.strip().split()
            pid=line2[1]
            cc="CC_Status"
            sev="Sev_Status"
            sev2="Sev_Status2"
            if first:
                first=False
            else:
                cc=cc_status[pid]
                sev="NA"
                if pid in sev_status:
                    sev=sev_status[pid]
                    sev=sev_status2[pid]
            line3=",".join(line2)+","+cc+","+sev+","+sev2+"\n"
            myout.write(line3)

