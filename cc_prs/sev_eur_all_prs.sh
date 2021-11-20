#$ -V
#$ -S /bin/bash
#$ -N sev_eur_all_prs
#$ -cwd
#$ -o /u/home/s/sarahjs3/project-arboleda/congenital_heart_disease_PRS/other/outfiles/sev_prs.$JOB_ID.out
#$ -j y
#$ -m ea
#$ -l h_data=8G,h_rt=4:00:00,highp

. /u/local/Modules/default/init/modules.sh 
module load gcc/10.2.0
module load R/4.1.0-DS

Rscript PRSice/PRSice.R --dir . --prsice PRSice/bin/PRSice --base fix2.Lifted.common.heart_arrhythmia.txt --A1 A1 --A2 A2 --stat BETA --target eur --thread 1 --beta --quantile 10 --pheno sev.pheno.txt --pheno-col PHENO --nonfounders --print-snp --binary-target F --out sev_eur_HEART_ARR  --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5 #--all-score

Rscript PRSice/PRSice.R --dir . --prsice PRSice/bin/PRSice --base fix2.Lifted.common.heart_arrhythmia.txt --A1 A1 --A2 A2 --stat BETA --target eur --thread 1 --beta --quantile 10 --pheno sev.pheno.txt --pheno-col PHENO --nonfounders --print-snp --binary-target F --out sev_eur_HEART_ARR  --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5 --extract sev_eur_HEART_ARR.valid

Rscript PRSice/PRSice.R --dir . --prsice PRSice/bin/PRSice --base fix2.Lifted.common.abnormalities_of_heart_beat.txt --A1 A1 --A2 A2 --stat BETA --target eur --thread 1 --beta --quantile 10 --pheno sev.pheno.txt --pheno-col PHENO --nonfounders --print-snp --binary-target F --out sev_eur_HEART_BEAT  --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5

Rscript PRSice/PRSice.R --dir . --prsice PRSice/bin/PRSice --base fix2.Lifted.common.abnormalities_of_heart_beat.txt --A1 A1 --A2 A2 --stat BETA --target eur --thread 1 --beta --quantile 10 --pheno sev.pheno.txt --pheno-col PHENO --nonfounders --print-snp --binary-target F --out sev_eur_HEART_BEAT  --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5 --extract sev_eur_HEART_BEAT.valid

Rscript PRSice/PRSice.R --dir . --prsice PRSice/bin/PRSice --base fix2.Lifted.common.heart_valve_problem_or_heart_murmur.txt --A1 A1 --A2 A2 --stat BETA --target eur --thread 1 --beta --quantile 10 --pheno sev.pheno.txt --pheno-col PHENO --nonfounders --print-snp --binary-target F --out sev_eur_HEART_VALVE --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5

Rscript PRSice/PRSice.R --dir . --prsice PRSice/bin/PRSice --base fix2.Lifted.common.heart_valve_problem_or_heart_murmur.txt --A1 A1 --A2 A2 --stat BETA --target eur --thread 1 --beta --quantile 10 --pheno sev.pheno.txt --pheno-col PHENO --nonfounders --print-snp --binary-target F --out sev_eur_HEART_VALVE --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5 --extract sev_eur_HEART_VALVE.valid