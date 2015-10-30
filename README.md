MutationAnalysisPipeline
========================

An automated pipeline for next generation sequence analysis and mutation annotation. 

Install
=======

To install the latest version of the MutationAnalysisPipeline, simply do:

git clone https://github.com/dattagargi/MutationAnalysisPipeline.git

Dependencies
============

The pipeline requires the following installed to work:
1. BWA (http://bio-bwa.sourceforge.net/)
2. Picardtools (http://broadinstitute.github.io/picard/) 
3. Samtools (http://www.htslib.org/)
4. Bcftools (https://samtools.github.io/bcftools/bcftools.html)
5. Annovar (http://annovar.openbioinformatics.org/en/latest/)

Description
===========

This pipeline automates processing of next generation sequence data, from mapping fastq to a reference file 
to functional annotations.
The pipeline can take as input one of the following:
1. Paired end fastq files for an unmapped genome
2. A sam file for a mapped genome
3. A bam file for a mapped genome
4. A vcf file generated via samtools

The input file should be placed in the 'Input' directory, with its genome specified in the 'genome_list.txt' file.
This pipeline can batch process input files from different genomes, as long as the file is present in the 'Input'
directory and the genome name is present in the 'genome_list.txt'. Multiple genomes can be specified in 'genome_list.txt'
as separated by newlines. Be careful to name your input file the same as the name specified in 'genome_list.txt'
For example, if genome_1.sam is in the 'Input' directory, 'genome_1' should be present as a genome in 'genome_list.txt'

The final output from the pipeline is annovar annotations for high quality SNPs of the input genome as compared to H37Rv. 
Intermediate outputs, like sam, bam, mpileup and vcf files created by the pipeline can be accessed as well.

Run the pipeline with the following command:

./run_mutation_pipeline.sh genome_list.txt


Licenses and citation
====================

## BWA-MEM ##
BWA is licensed separately
Li, H. (2013) Aligning sequence reads, clone sequences and assembly contigs with BWA-MEM. arXiv:1303.3997 [q-bio.GN].

## Picardtools ##
Picardtools is licensed separately
http://broadinstitute.github.io/picard/

## Samtools ##
Samtools is licensed separately
Li H.*, Handsaker B.*, Wysoker A., Fennell T., Ruan J., Homer N., Marth G., Abecasis G., Durbin R. and 
1000 Genome Project Data Processing Subgroup (2009) The Sequence alignment/map (SAM) format and SAMtools. 
Bioinformatics, 25, 2078-9. [PMID: 19505943]

## Bcftools ##
Bcftools is licensed separately
Li H.*, Handsaker B.*, Wysoker A., Fennell T., Ruan J., Homer N., Marth G., Abecasis G., Durbin R. and 
1000 Genome Project Data Processing Subgroup (2009) The Sequence alignment/map (SAM) format and SAMtools. 
Bioinformatics, 25, 2078-9. [PMID: 19505943]

## Annovar ##
Annovar is licensed separately
Wang K, Li M, Hakonarson H. ANNOVAR: Functional annotation of genetic variants from next-generation sequencing data.
Nucleic Acids Research, 38:e164, 2010

[1] Davidson RM, Hasan NA, Reynolds PR, Totten S, Garcia B, Levin A, et al. Genome sequencing of Mycobacterium abscessus isolates from patients in the united states and comparisons to globally diverse clinical strains. J Clin Microbiol 2014;52:3573–82. doi:10.1128/JCM.01144-14.
