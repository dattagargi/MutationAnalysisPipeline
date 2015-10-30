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

INPUT_DIR = 'Input/'
OUTPUT_DIR = 'Output/'

def getAnnotations(genome):
  caller = inspect.stack()[1][3]
  if 'main' in caller:
    filename = INPUT_DIR + genome + '.vcf'
  else:
    filename = OUTPUT_DIR + 'vcf/' + genome + '.vcf'
  
  print 'Annovar ' + filename
  command1 = 'perl annovar/convert2annovar.pl -format vcf4 ' + filename + ' > ' + OUTPUT_DIR + 'annovar/avinput/' + genome + '.avinput 2> ' + OUTPUT_DIR + 'annovar/avinput/' + genome + '.avinput.log'
  command2 = 'perl annovar/annotate_variation.pl --buildver H37Rv --outfile ' + OUTPUT_DIR + 'annovar/output/' + genome +  ' ' + OUTPUT_DIR + 'annovar/avinput/' + genome + '.avinput ref_files/' 
  os.system(command1)
  os.system(command2)

if __name__ == "__main__":
  main()
       
