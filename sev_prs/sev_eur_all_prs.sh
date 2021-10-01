#$ -V
#$ -S /bin/bash
#$ -N sev_eur_all_prs
#$ -cwd
#$ -o /u/home/s/sarahjs3/eeskin2/projects/CHD_PRS/sev_prs/sev_prs.$JOB_ID.out
#$ -j y
#$ -m a
#$ -l h_data=8G,h_rt=4:00:00,highp

. /u/local/Modules/default/init/modules.sh 
module load R/3.5.0

Rscript ../prs/PRSice/PRSice.R --dir . --prsice ../prs/PRSice/bin/PRSice --base ../prs/fix.Lifted.common.heart_arrhythmia.txt --A1 A1 --A2 A2 --stat BETA --target ../prs/eur --thread 1 --beta --quantile 10 --pheno sev.pheno.txt --pheno-col PHENO --nonfounders  --binary-target F --out sev_eur_HEART_ARR  --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5 #--all-score

Rscript ../prs/PRSice/PRSice.R --dir . --prsice ../prs/PRSice/bin/PRSice --base ../prs/fix.Lifted.common.heart_arrhythmia.txt --A1 A1 --A2 A2 --stat BETA --target ../prs/eur --thread 1 --beta --quantile 10 --pheno sev.pheno.txt --pheno-col PHENO --nonfounders  --binary-target F --out sev_eur_HEART_ARR  --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5 --extract sev_eur_HEART_ARR.valid

Rscript ../prs/PRSice/PRSice.R --dir . --prsice ../prs/PRSice/bin/PRSice --base ../prs/fix.Lifted.common.abnormalities_of_heart_beat.txt --A1 A1 --A2 A2 --stat BETA --target ../prs/eur --thread 1 --beta --quantile 10 --pheno sev.pheno.txt --pheno-col PHENO --nonfounders  --binary-target F --out sev_eur_HEART_BEAT  --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5

Rscript ../prs/PRSice/PRSice.R --dir . --prsice ../prs/PRSice/bin/PRSice --base ../prs/fix.Lifted.common.abnormalities_of_heart_beat.txt --A1 A1 --A2 A2 --stat BETA --target ../prs/eur --thread 1 --beta --quantile 10 --pheno sev.pheno.txt --pheno-col PHENO --nonfounders  --binary-target F --out sev_eur_HEART_BEAT  --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5 --extract sev_eur_HEART_BEAT.valid

Rscript ../prs/PRSice/PRSice.R --dir . --prsice ../prs/PRSice/bin/PRSice --base ../prs/fix.Lifted.common.heart_valve_problem_or_heart_murmur.txt --A1 A1 --A2 A2 --stat BETA --target ../prs/eur --thread 1 --beta --quantile 10 --pheno sev.pheno.txt --pheno-col PHENO --nonfounders --binary-target F --out sev_eur_HEART_VALVE --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5

Rscript ../prs/PRSice/PRSice.R --dir . --prsice ../prs/PRSice/bin/PRSice --base ../prs/fix.Lifted.common.heart_valve_problem_or_heart_murmur.txt --A1 A1 --A2 A2 --stat BETA --target ../prs/eur --thread 1 --beta --quantile 10 --pheno sev.pheno.txt --pheno-col PHENO --nonfounders --binary-target F --out sev_eur_HEART_VALVE --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5 --extract sev_eur_HEART_VALVE.valid
