#$ -V
#$ -S /bin/bash
#$ -N pheweb_eur_100_prs
#$ -cwd
#$ -o /u/home/s/sarahjs3/project-arboleda/congenital_heart_disease_PRS/other/outfiles/pheweb_fetal_prs.$JOB_ID.out
#$ -j y
#$ -m ea
#$ -l h_data=32G,h_rt=8:00:00,highp

. /u/local/Modules/default/init/modules.sh 
module load gcc/10.2.0
module load R/4.1.0-DS

#Rscript ../cc_prs/PRSice/PRSice.R --dir . --prsice ../cc_prs/PRSice/bin/PRSice --base fix2.Lifted.common.heart_valve_disorders.txt --chr chrom --A1 ALT --A2 REF --stat beta --snp snp --bp chromEnd --pvalue pval --target eur100 --thread 1 --beta --quantile 10 --nonfounders --print-snp --binary-target T --out eur100_Valve_Dis  --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5 

#Rscript ../cc_prs/PRSice/PRSice.R --dir . --prsice ../cc_prs/PRSice/bin/PRSice --base fix2.Lifted.common.heart_valve_disorders.txt --chr chrom --A1 ALT --A2 REF --stat beta --snp snp --bp chromEnd --pvalue pval --target eur100 --thread 1 --beta --quantile 10 --nonfounders --print-snp --binary-target T --out eur100_Valve_Dis  --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5 --extract eur100_Valve_Dis.valid

#Rscript ../cc_prs/PRSice/PRSice.R --dir . --prsice ../cc_prs/PRSice/bin/PRSice --base fix2.Lifted.common.abnormal_heart_sounds.txt --chr chrom --A1 ALT --A2 REF --stat beta --snp snp --bp chromEnd --pvalue pval --target eur100 --thread 1 --beta --quantile 10 --nonfounders --print-snp --binary-target T --out eur100_Heart_Sounds  --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5 

#Rscript ../cc_prs/PRSice/PRSice.R --dir . --prsice ../cc_prs/PRSice/bin/PRSice --base fix2.Lifted.common.abnormal_heart_sounds.txt --chr chrom --A1 ALT --A2 REF --stat beta --snp snp --bp chromEnd --pvalue pval --target eur100 --thread 1 --beta --quantile 10 --nonfounders --print-snp --binary-target T --out eur100_Heart_Sounds  --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5  --extract eur100_Heart_Sounds.valid


#Rscript ../cc_prs/PRSice/PRSice.R --dir . --prsice ../cc_prs/PRSice/bin/PRSice --base fix2.Lifted.common.heart_valve_disorders.txt --chr chrom --A1 ALT --A2 REF --stat beta --snp snp --bp chromEnd --pvalue pval --target eur100 --thread 1 --beta --quantile 10 --pheno ../cc_prs/sev.pheno.txt --pheno-col PHENO --nonfounders --print-snp --binary-target F --out sev_eur100_Valve_Dis  --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5 

Rscript ../cc_prs/PRSice/PRSice.R --dir . --prsice ../cc_prs/PRSice/bin/PRSice --base fix2.Lifted.common.heart_valve_disorders.txt --chr chrom --A1 ALT --A2 REF --stat beta --snp snp --bp chromEnd --pvalue pval --target eur100 --thread 1 --beta --quantile 10 --pheno ../cc_prs/sev.pheno.txt --pheno-col PHENO --nonfounders --print-snp --binary-target F --out sev_eur100_Valve_Dis  --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5 --extract sev_eur100_Valve_Dis.valid

#Rscript ../cc_prs/PRSice/PRSice.R --dir . --prsice ../cc_prs/PRSice/bin/PRSice --base fix2.Lifted.common.abnormal_heart_sounds.txt --chr chrom --A1 ALT --A2 REF --stat beta --snp snp --bp chromEnd --pvalue pval --target eur100 --thread 1 --beta --quantile 10 --pheno ../cc_prs/sev.pheno.txt --pheno-col PHENO --nonfounders  --print-snp --binary-target F --out sev_eur100_Heart_Sounds  --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5 

Rscript ../cc_prs/PRSice/PRSice.R --dir . --prsice ../cc_prs/PRSice/bin/PRSice --base fix2.Lifted.common.abnormal_heart_sounds.txt --chr chrom --A1 ALT --A2 REF --stat beta --snp snp --bp chromEnd --pvalue pval --target eur100 --thread 1 --beta --quantile 10 --pheno ../cc_prs/sev.pheno.txt --pheno-col PHENO --nonfounders  --print-snp --binary-target F --out sev_eur100_Heart_Sounds  --bar-levels 0.00000005,0.00000001,0.0000001,0.000001,0.00001,0.0001,0.001,0.01,0.02,0.03,0.04,0.05 --perm 10000 --seed  5 --extract sev_eur100_Heart_Sounds.valid
