import random
import numpy as numpy

test = 1000
my_checksum = numpy.array([1,test])

for k in range(1,test):
  rannum = 0
  sum = 0
  checksum = 0
  fltrannum = float("{0:.4f}".format(rannum))
  fltsum = float("{0:.4f}".format(sum))
  fltchecksum = float("{0:.4f}".format(checksum))
  print ("i: 0","RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)
      
  for i in range(1, 20):    #generates iterations 0 to 20
    rng = random.Random()           
    number = rng.randrange(1, 10000)
    rannum = (number / 1000)
    sum += rannum
    checksum += sum
    fltrannum = float("{0:.4f}".format(rannum))
    fltsum = float("{0:.4f}".format(sum))
    fltchecksum = float("{0:.4f}".format(checksum))
    #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)
    
  my_checksum = numpy.array([1,test])
  print(my_checksum)
  #my_checksum[k] = fltchecksum
  #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)