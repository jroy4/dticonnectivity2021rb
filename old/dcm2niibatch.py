#!/usr/bin/env python3
#coding: utf8

import os
import sys

prospective = 'reback-prospective'
retroSpective = 'reback-retrospective'

num_Inputs_Required = 2

def main():
  os.system('cd ~/Desktop/Research/Reback-DTI')

  #removed this when I realized that retrospective has a slightly different file structure
  # if len(sys.argv) < num_Inputs_Required:
  #   print('Youre using less than 2 arguments. By default, we will convert DICOMS in {}'.format(prospective))
  #   spective = os.path.join(os.getcwd(), prospective)
  # elif(sys.argv[1] == 'p'):
  #   spective = os.path.join(os.getcwd(), prospective)
  # elif(sys.argv[1] == 'r'):
  #   spective = os.path.join(os.getcwd(), retroSpective)
  # else:
  #   print('Invalid argument...')
  #   print('Format should be: \'python3 dcm2niibatch.py [p/r]\'' )
  #   print('Your options are [p] for prospective or [r] for retroSpective')
  #   print('Scrub')
  #   sys.exit()

  spective = os.path.join(os.getcwd(), prospective)

  print('\n')

  if(not os.path.isdir(spective)):
    print("I don't see the directory {}".format(spective))
    print('Look into that...I quit...ur a scrub')
    sys.exit()
  patients = [os.path.join(spective,X) for X in os.listdir(spective) if os.path.isdir(os.path.join(spective,X))]


  DICOMS = []
  for patient in patients:
      samples = [os.path.join(patient, X) for X in os.listdir(patient) if os.path.isdir(os.path.join(patient, X))]
      for sample in samples:
          dicom_dirs = [os.path.join(sample, X) for X in os.listdir(sample) if os.path.isdir(os.path.join(sample, X)) and X == 'DICOM']
          DICOMS.extend(dicom_dirs)



  commands = []
  for i in DICOMS:
      command = '/Applications/MRIcroGL.app/Contents/Resources/dcm2niix -f "%f_%p_%t_%s" -p y -z y ' + i
      commands.append(command)

  for i in commands:
      print('Running command: ')
      print(i)
      os.system(i)
      print('\n\n')

main()