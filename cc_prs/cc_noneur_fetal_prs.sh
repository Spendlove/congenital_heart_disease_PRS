#$ -V
#$ -S /bin/bash
#$ -N cc_noneur100_all_prs
#$ -cwd
#$ -o /u/home/s/sarahjs3/eeskin2/projects/CHD_PRS/prs/cc_prs.$JOB_ID.out
#$ -j y
#$ -m a
#$ -l h_data=8G,h_rt=4:00:00,highp

. /u/local/Modules/default/init/modules.sh 
module load R/3.5.0

Rscript PRSice/PRSice.R --dir . --prsice PRSice/bin/PRSice --base fix.Lifted.common.heart_valve_problem_or_heart_murmur.txt --A1 A1 --A2 A2 --stat BETA --target noneur100 --thread 1 --beta --quantile 10 --pheno pheno.txt --pheno-col PHENO --nonfounders --binary-target T --out noneur100_HEART_VALVE --bar-levels 0.00385005 --seed 5 --fastscore

Rscript PRSice/PRSice.R --dir . --prsice PRSice/bin/PRSice --base fix.Lifted.common.heart_valve_problem_or_heart_murmur.txt --A1 A1 --A2 A2 --stat BETA --target noneur100 --thread 1 --beta --quantile 10 --pheno pheno.txt --pheno-col PHENO --nonfounders --binary-target T --out noneur100_HEART_VALVE --bar-levels 0.00385005 --seed 5 --fastscore --extract noneur100_HEART_VALVE.valid
