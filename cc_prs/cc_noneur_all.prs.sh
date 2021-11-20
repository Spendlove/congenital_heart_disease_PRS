#$ -V
#$ -S /bin/bash
#$ -N cc_noneur_all_prs
#$ -cwd
#$ -o /u/home/s/sarahjs3/project-arboleda/congenital_heart_disease_PRS/other/outfiles/cc_prs.$JOB_ID.out
#$ -j y
#$ -m ea
#$ -l h_data=8G,h_rt=4:00:00,highp

. /u/local/Modules/default/init/modules.sh 
module load gcc/10.2.0
module load R/4.1.0-DS


Rscript PRSice/PRSice.R --dir . --prsice PRSice/bin/PRSice --base fix2.Lifted.common.heart_valve_problem_or_heart_murmur.txt --A1 A1 --A2 A2 --stat BETA --target noneur --thread 1 --beta --quantile 10 --pheno pheno.txt --pheno-col PHENO --nonfounders --print-snp --binary-target T --out noneur_HEART_VALVE --bar-levels 0.00415005 --seed 5 --fastscore --all-score

Rscript PRSice/PRSice.R --dir . --prsice PRSice/bin/PRSice --base fix2.Lifted.common.heart_valve_problem_or_heart_murmur.txt --A1 A1 --A2 A2 --stat BETA --target noneur --thread 1 --beta --quantile 10 --pheno pheno.txt --pheno-col PHENO --nonfounders --print-snp --binary-target T --out noneur_HEART_VALVE --bar-levels 0.00415005 --seed 5 --fastscore --extract noneur_HEART_VALVE.valid --all-score
