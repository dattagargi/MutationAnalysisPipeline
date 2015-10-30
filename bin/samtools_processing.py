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
import inspect
from annovar_processing import getAnnotations

INPUT_DIR = 'Input/'
OUTPUT_DIR = 'Output/'

def processSamFiles(genome):
  if 'main' in inspect.stack()[1][3]:
    filename_1 = INPUT_DIR + genome + '.sam'
  else:
    filename_1 = OUTPUT_DIR + genome + '.sam'
  print 'Processing ' + filename_1
  command1 = 'samtools view -bS ' + filename_1 + ' > ' + OUTPUT_DIR + genome + '.bam' 
  os.system(command1)
  processBamFiles(genome)

def processBamFiles(genome):
  if 'main' in inspect.stack()[1][3]:
    filename = INPUT_DIR + genome + '.bam'
  else:
    filename = OUTPUT_DIR + genome + '.bam'
  command1 = 'samtools sort ' + filename + ' ' + genome + '.sorted'
  command2 = 'samtools index ' + genome + '.sorted.bam'
  command3 = 'samtools mpileup -uD -f ref_files/TB_H37Rv_sequence_validated.fa ' + genome + '.sorted.bam > ' + OUTPUT_DIR + 'mpileup/' + genome + '_mpileup'
  command4 = 'bcftools call -mv -Ov -Vindels ' + OUTPUT_DIR + 'mpileup/' +  genome + '_mpileup > ' + OUTPUT_DIR + 'vcf/' + genome + '_unfiltered.vcf'
  command5 = 'vcfutils.pl varFilter -d10 -Q20 ' + OUTPUT_DIR + 'vcf/' + genome  + '_unfiltered.vcf > ' + OUTPUT_DIR + 'vcf/' + genome + '.vcf'
  command6 = 'mv ' + genome + '.sorted.bam* ' + OUTPUT_DIR 
  os.system(command1)
  os.system(command2)
  os.system(command3)
  os.system(command4)
  os.system(command5)
  os.system(command6)

  getAnnotations(genome)

