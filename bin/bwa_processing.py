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
from samtools_processing import processSamFiles

INPUT_DIR = 'Input/'
OUTPUT_DIR = 'Output/'

def mapFastqFiles(genome):
  if 'main' in inspect.stack()[1][3]:
    dir = INPUT_DIR
  else:
    dir = OUTPUT_DIR
  filename_1 = dir + genome + '.fastq'
  filename_2 = dir + genome + '_1.fastq'
  filename_3 = dir + genome + '_2.fastq'
  se_exists = False
  if os.path.isfile(filename_1):
    print 'Single End mapping'
    command1 = 'bwa mem -t#cpus ref_files/TB_H37Rv_sequence_validated.fa ' + filename_1 + ' > ' + OUTPUT_DIR + genome + '_se.sam'
    os.system(command1)
    se_exists = True
  command2 = 'bwa mem -t#cpus ref_files/TB_H37Rv_sequence_validated.fa ' + filename_2 + ' ' + filename_3 + ' > ' + OUTPUT_DIR + genome + '_pe.sam'
  os.system(command2)

  if se_exists:
    'Merging sams'
    command3 = 'run_picard MergeSamFiles INPUT=' + OUTPUT_DIR + genome + '_se.sam' + ' INPUT=' + OUTPUT_DIR + genome + '_pe.sam' +' OUTPUT=' + OUTPUT_DIR + genome + '.sam'
  else:
    command3 = 'mv ' + OUTPUT_DIR + genome + '_pe.sam ' + OUTPUT_DIR + genome + '.sam'
  os.system(command3)
  if se_exists:
    command4 = 'rm -rf ' + OUTPUT_DIR + genome + '_se.sam'
    command5 = 'rm -rf ' + OUTPUT_DIR + genome + '_pe.sam'
    os.system(command4)
    os.system(command5)

  processSamFiles(genome)
