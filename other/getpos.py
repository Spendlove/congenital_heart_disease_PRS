import sys
import gzip
mydict={}
myin=gzip.open("/u/scratch/s/sarahjs3/resources/gencode.v35.annotation.gtf.gz","rt")
for line in myin.readlines():
    if line[0]!="#":
        line2=line.strip().split("\t")
        line3=line.strip().split()
        chrm=line2[0][3:]
        start=int(line2[3])
        end=int(line2[4])
        annotations=line3
        name=""
        if len(annotations)>8:
            name=line3[9]
        if name !="": 
            if name in mydict:
                stuff2=mydict[name]
                s=stuff2[1]
                e=stuff2[2]
                result=[chrm,s,e]
                if start < s:
                    result[1]=start
                if end > e:
                    result[2]=end
                mydict[name]=result
            else:
                mydict[name]=[chrm,start,end]
infiles=["allrpkm.csv"]
outfiles=["100pos2.txt"]
for i in range(0,len(outfiles)):
    g2=open(infiles[i],"r")
    o2=open(outfiles[i],"w")
    for line in g2.readlines(): 
        gene=line.strip().split(",")[0]
        gene2="\""+gene+"\""+";"
        if gene2 in mydict:
            stuff3=mydict[gene2]
            mystart=int(stuff3[1])-10000
            if mystart<0:
                mystart=0
            mychrm=stuff3[0]
            if mychrm!="Y" and mychrm!="M" and mychrm!="X":
                o2.write(stuff3[0]+" "+str(mystart)+" "+str(int(stuff3[2])+10000)+" "+gene+"\n")
    g2.close()
    o2.close()
myin.close()
