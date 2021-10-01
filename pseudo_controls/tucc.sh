#$ -V
#$ -S /bin/bash
#$ -N tucc
#$ -cwd
#$ -o /u/home/s/sarahjs3/eeskin2/CHD/results/outfiles/tucc.$JOB_ID.$TASK_ID.out
#$ -j y
#$ -m n
#$ -l h_data=4G,h_rt=24:00:00,highp
#$ -t 1-2887:1

dir=/u/home/s/sarahjs3/eeskin2/CHD
plink=$dir/development_plink/plink
outdir=$dir/results
indir=$dir/polymutt
intervalfile=$dir/format_hg38_chr_cut1000000.txt

chr=0
region=`expr $SGE_TASK_ID - 1`
if [ $region -lt 3886 ]
then
    echo $region
    while IFS=' ', read cc ff ll rr;do
        if [ $rr == $region ]
            then
                chr=$cc
            fi
    done < $intervalfile
fi
echo $chr

infile=$indir/$chr/$region/chd.snv.qc2.polymutt.$chr.$region
$plink --noweb --bfile $infile --tucc 'write-bed' --out $outdir/chd.snv.qc2.polymutt.tucc.$chr.region.$region 

/u/flashscratch/s/sarahjs3/resources/bin/bam_to_fastq/bam_to_fastq_2
/u/flashscratch/s/sarahjs3/resources/bin/bam_to_fastq/bam_to_fastq_2
