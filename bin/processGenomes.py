'''
The MIT License (MIT)

Copyright (c) 2015 Gargi Datta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

#!/usr/bin/python

import sys
import os
import copy
from bwa_processing import mapFastqFiles
from samtools_processing import processBamFiles, processSamFiles
from annovar_processing import getAnnotations

BWA = 1
SAM = 2
BAM = 3
ANNO = 4
INPUT_DIR = 'Input'
OUTPUT_DIR = 'Output'
EXT_DICT = {'fastq':BWA, 'sam':SAM, 'bam':BAM, 'vcf':ANNO}

def main():
  if len(sys.argv) < 2:
    sys.stderr.write('USAGE: python processGenomes.py <Genome List>\n')
    sys.exit(1)

  in_file = sys.argv[1]
  genome_list = {}
  files = os.listdir(INPUT_DIR)
  with open(in_file, 'r') as infile:
    for line in infile.readlines():
      genome = line.strip()
      exists = False
      for name in files:
        if genome in name and not exists: 
          ext = name.split('.')[1].strip()
          if ext in EXT_DICT.keys():
            genome_list[genome] = EXT_DICT[ext]
            exists = True
      if not exists:
        sys.stderr.write('No corresponding input file found for genome ' + genome + '!\n')

  count = 0
  outfile = open('Mutation-analysis.log', 'w')
  for genome in genome_list.keys():
    step = genome_list[genome]
    if step == 1:
      mapFastqFiles(genome)
    elif step == 2:
      processSamFiles(genome)
    elif step == 3:
      processBamFiles(genome)
    elif step == 4:
      getAnnotations(genome) 

    count = count + 1
    if count % 100 == 0:
      write_data = 'Processed ' + str(count) + ' genomes ...'
      print write_data 
      outfile.write(write_data + '\n')

  outfile.close()

if __name__ == "__main__":
  main()
       
