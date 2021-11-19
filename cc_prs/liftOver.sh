#$ -V
#$ -S /bin/bash
#$ -N lift
#$ -cwd
#$ -o /u/home/s/sarahjs3/project-arboleda/congenital_heart_disease_PRS/other/outfiles/lift.$JOB_ID.out
#$ -j y
#$ -m a
#$ -l h_data=32G,h_rt=8:00:00,highp


liftOver=/u/home/s/sarahjs3/project-arboleda/congenital_heart_disease_PRS/software/liftOver
$liftOver 
chainfile=/u/home/s/sarahjs3/project-arboleda/congenital_heart_disease_PRS/software/hg19ToHg38.over.chain.gz
ls noheader.common.heart_valve_disorders.txt
ls $chainfile
$liftOver -bedPlus=3 noheader.common.abnormal_heart_sounds.txt $chainfile Lifted.common.abnormal_heart_sounds.txt Unlifted.common.abnormal_heart_sounds.txt
$liftOver -bedPlus=3 noheader.common.heart_valve_disorders.txt $chainfile Lifted.common.heart_valve_disorders.txt Unlifted.common.heart_valve_disorders.txt


