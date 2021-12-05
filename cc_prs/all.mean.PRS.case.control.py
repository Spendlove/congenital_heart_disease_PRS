
#inputfiles=["eur40_HEART_BEAT.best","eur90_MALF_HEART.best","eur40_CARD_SEPTA.best","eur100_ARR.best","eur40_HEART_VALVE.best"]
#names=["alleur40_HEART_VALVE","alleur40_HEART_BEAT","alleur90_MALF_HEART"]

allfiles=["eur_HEART_VALVE","eur100_HEART_VALVE","eur100_Heart_Sounds","eur_Heart_Sounds","sev_eur100_HEART_VALVE","sev_eur_HEART_VALVE","sev100_eur_Heart_Sounds","sev_eur_Heart_Sounds","eur_HEART_BEAT","eur100_HEART_BEAT","sev_eur_HEART_BEAT","sev_eur100_HEART_BEAT","eur_Valve_Dis","eur100_Valve_Dis","sev_eur_Valve_Dis","sev_eur100_Valve_Dis","eur_HEART_ARR","eur100_HEART_ARR","sev_eur100_HEART_ARR","sev_eur_HEART_ARR"]

testfiles=["Neale_Alt/eur_HEART_ARR.best","Neale_Alt/eur_HEART_VALVE.best","../prs/eur_HEART_VALVE.best","Neale_Ref/eur_HEART_VALVE.best","../prs/eur_HEART_ARR.best","Neale_Ref/eur_HEART_ARR.best","Neale_Alt/eur_HEART_BEAT.best","../prs/eur_HEART_BEAT.best","Neale_Ref/eur_HEART_BEAT.best","eur_Heart_Sounds.best","PheWeb_Alt/eur_Heart_Sounds.best","PheWeb_Ref/eur_Heart_Sounds.best","PheWeb_Alt/eur_Valve_Dis.best","PheWeb_Ref/eur_Valve_Dis.best","eur_Valve_Dis.best"]

#indir="Neale_Alt/"

for name in testfiles:
    print("++++++++++++++++++++++++++++++++++++++")
    print(name)
    case=0.0
    control=0.0
    n=0.0
    first=True
    with open(name,"r") as myin:
        for line in myin.readlines():
            if first==True:
                first=False
            else:
                n+=1
                line2=line.strip().split()
                trans=line2[1].split("_")[2]
                score=float(line2[3])
                if trans=="T":
                    case+=score
                elif trans=="U":
                    control+=score
                else:
                    print("huh")
    print("Case: "+str(case/n))
    print("Control: "+str(control/n))

#for name in allfiles:
#    hv_n=0.0
#    mydict={}
#    thresholds=[]
#    first=True
#    myout=open(name+".mean_score","w")
#    with open(indir+name+".all_score","r") as myin:
#        for line in myin.readlines():
#            if first==True:
#                line2=line.strip().split()
#                hv_case=0.0
#                hv_control=0.0
#                thresholds=line2[2:len(line2)]
#                for pt in thresholds:
#                    mydict[pt]=[hv_case,hv_control]
#                first=False
#            else:
#                hv_n+=1
#                line2=line.strip().split()
#                trans=line2[1].split("_")[2]
#                scores=line2[2:len(line2)]
#                index=0
#                for s in scores:
#                    s=float(s)
#                    pt=thresholds[index]
#                    index+=1
#                    if trans=="T":
#                        mydict[pt][0]+=s
#                    elif trans=="U":
#                        mydict[pt][1]+=s
#                    else:
#                        print("huh "+trans)
#    print("--------HV-------------")
#    myout.write("P-value_Threshold Case_Mean_PRS Control_Mean_PRS\n")
#    for pt in thresholds:
#        pt2=pt.split("_")[1]
#        myout.write(str(pt2)+" "+str(mydict[pt][0])+" "+str(mydict[pt][1])+"\n")
##print("case: "+str(hv_case/hv_n))
##print("control: "+str(hv_control/hv_n))
