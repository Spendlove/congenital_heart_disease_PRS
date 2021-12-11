wget https://broad-ukb-sumstats-us-east-1.s3.amazonaws.com/round2/additive-tsvs/R00.gwas.imputed_v3.both_sexes.tsv.bgz
wget https://broad-ukb-sumstats-us-east-1.s3.amazonaws.com/round2/additive-tsvs/20002_1077.gwas.imputed_v3.both_sexes.tsv.bgz
wget https://broad-ukb-sumstats-us-east-1.s3.amazonaws.com/round2/additive-tsvs/20002_1078.gwas.imputed_v3.both_sexes.tsv.bgz

mv R00.gwas.imputed_v3.both_sexes.tsv.bgz R00.gwas.imputed_v3.both_sexes.tsv.gz
mv 20002_1077.gwas.imputed_v3.both_sexes.tsv.bgz 20002_1077.gwas.imputed_v3.both_sexes.tsv.gz
mv 20002_1078.gwas.imputed_v3.both_sexes.tsv.bgz 20002_1078.gwas.imputed_v3.both_sexes.tsv.gz

gunzip R00.gwas.imputed_v3.both_sexes.tsv.gz
gunzip 20002_1077.gwas.imputed_v3.both_sexes.tsv.gz
gunzip 20002_1078.gwas.imputed_v3.both_sexes.tsv.gz

gunzip PheCode_395_SAIGE_MACge20.txt.vcf.gz
gunzip PheCode_396_SAIGE_MACge20.txt.vcf.gz


wget ftp://share.sph.umich.edu/UKBB_SAIGE_HRC/PheCode_395_SAIGE_MACge20.txt.vcf.gz
wget ftp://share.sph.umich.edu/UKBB_SAIGE_HRC/PheCode_396_SAIGE_MACge20.txt.vcf.gz

#wget ftp://share.sph.umich.edu/UKBB_SAIGE_HRC/PheCode_747_SAIGE_MACge20.txt.vcf.gz 
#wget ftp://share.sph.umich.edu/UKBB_SAIGE_HRC/PheCode_395.6_SAIGE_MACge20.txt.vcf.gz
#gunzip PheCode_747_SAIGE_MACge20.txt.vcf.gz
#gunzip PheCode_395.6_SAIGE_MACge20.txt.vcf.gz
