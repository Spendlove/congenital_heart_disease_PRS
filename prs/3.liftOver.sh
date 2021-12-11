#$ -V
#$ -S /bin/bash
#$ -N lift
#$ -cwd
#$ -o /u/home/s/sarahjs3/project-arboleda/congenital_heart_disease_PRS/prs/outfiles/lift.$JOB_ID.out
#$ -j y
#$ -m bea
#$ -l h_data=32G,h_rt=8:00:00,highp


liftover=/u/home/s/sarahjs3/project-arboleda/congenital_heart_disease_PRS/software/liftOver
chainfile=/u/home/s/sarahjs3/project-arboleda/congenital_heart_disease_PRS/software/hg19ToHg38.over.chain.gz

$liftover -bedPlus=3 noheader.common.heart_arr.txt $chainfile Lifted.common.heart_arrhythmia.txt Unlifted.common.heart_arrhythmia.txt
$liftover -bedPlus=3 noheader.common.heart_valve.txt $chainfile Lifted.common.heart_valve_problem_or_heart_murmur.txt Unlifted.common.heart_valve_problem_or_heart_murmur.txt
$liftover -bedPlus=3 noheader.common.heart_beat.txt $chainfile Lifted.common.abnormalities_of_heart_beat.txt Unlifted.common.abnormalities_of_heart_beat.txt

$liftover -bedPlus=3 noheader.common.heart_sounds.txt $chainfile Lifted.common.abnormal_heart_sounds.txt Unlifted.common.abnormal_heart_sounds.txt
$liftover -bedPlus=3 noheader.common.valve_dis.txt $chainfile Lifted.common.heart_valve_disorders.txt Unlifted.common.heart_valve_disorders.txt

##$liftover -bedPlus=3 noheader.common.congenital_abnormalities.txt $chainfile Lifted.noheader.common.congenital_abnormalities.txt Unlifted.noheader.common.congenital_abnormalities.txt
##$liftover -bedPlus=3 noheader.common.valve_replaced.txt $chainfile Lifted.noheader.common.valve_replaced.txt Unlifted.noheader.common.valve_replaced.txt

text='1i\chrom\tchromStart\tchromEnd\tvariant\tminor_allele\tminor_AF\texpected_case_minor_AC\tlow_confidence_variant\tn_complete_samples\tAC\tytx\tbeta\tse\ttstat\tpval'
sed -e $text Lifted.common.heart_arrhythmia.txt > fix.Lifted.common.heart_arrhythmia.txt
sed -e $text Lifted.common.heart_valve_problem_or_heart_murmur.txt > fix.Lifted.common.heart_valve_problem_or_heart_murmur.txt
sed -e $text Lifted.common.abnormalities_of_heart_beat.txt > fix.Lifted.common.abnormalities_of_heart_beat.txt
text2='1i\chrom\tchromStart\tchromEnd\tCHROM\tPOS\tID\tREF\tALT\tac\taf\tnum_cases\tnum_controls\tbeta\tsebeta\tTstat\tpval\tpval_SAIGE_NoSPA\tIs_Converged\tvarT\tvarTstar\tsnp'
sed -e $text2 Lifted.common.abnormal_heart_sounds.txt > fix.Lifted.common.abnormal_heart_sounds.txt 
sed -e $text2 Lifted.common.heart_valve_disorders.txt > fix.Lifted.common.heart_valve_disorders.txt

#sed -e $text2 Lifted.noheader.common.congenital_abnormalities.txt > fix.Lifted.common.congenital_abnormalities.txt
#sed -e $text2 Lifted.noheader.common.valve_replaced.txt > fix.Lifted.common.valve_replaced.txt

