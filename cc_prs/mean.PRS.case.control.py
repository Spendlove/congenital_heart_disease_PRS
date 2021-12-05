inputfiles=["eur40_HEART_BEAT.best","eur90_MALF_HEART.best","eur40_CARD_SEPTA.best","eur100_ARR.best","eur40_HEART_VALVE.best"]
allfiles=["eur_HEART_VALVE","eurM_HEART_VALVE","eur25_HEART_VALVE","eur50_HEART_VALVE","eur75_HEART_VALVE","eur100_HEART_VALVE","eur_HEART_BEAT","eurM_HEART_BEAT","eur25_HEART_BEAT","eur50_HEART_BEAT","eur75_HEART_BEAT","eur100_HEART_BEAT","eur_MALF_HEART","eurM_MALF_HEART","eur25_MALF_HEART","eur50_MALF_HEART","eur75_MALF_HEART","eur100_MALF_HEART","eur_CARDIAC_SEPTA","eurM_CARDIAC_SEPTA","eur25_CARDIAC_SEPTA","eur50_CARDIAC_SEPTA","eur75_CARDIAC_SEPTA","eur100_CARDIAC_SEPTA","eur_HEART_ARR","eurM_HEART_ARR","eur25_HEART_ARR","eur50_HEART_ARR","eur75_HEART_ARR","eur100_HEART_ARR"]
for name in allfiles:
    print("++++++++++++++++++++++++++++++++++++++")
    print(name)
    case=0.0
    control=0.0
    n=0.0
    first=True
    with open("../prs/"+name+".best","r") as myin:
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
