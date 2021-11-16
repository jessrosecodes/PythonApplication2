import random
import numpy as numpy
###################################################################### START LAYER ONE #################################################################################
############################ USER Inputs ######################################
test = 1001             #number of total tests
n = 255                 #number being divided by in the mod calculation
calcs = 20              #total number of calculations for each test
rannumrangestart = 1    #starting range of random number
rannumrangeend = 100  #ending range of random number
rannumdiv = 80            # number random number will be divided by
########################### Inputs User shouldn't change ############
rannum = 0              #starting value of randon number
sum = 0                 #starting value of sum
checksum = 0            #starting value of checksum
############################ USER Inputs ######################################
###########################    SYNTAX  ##############################
fltrannum = float("{0:.4f}".format(rannum))
fltsum = float("{0:.4f}".format(sum))
fltchecksum = float("{0:.4f}".format(checksum))
###########################    SYNTAX  ##############################
###########################   EQNS    ##############################
#list2 = []                                                                      # list allows us to append, unlike array; comment out if using 1 list
list1 = []                                                                       # comment if using more than one list
###########################    EQNS    ##############################
#print ("i: 0","RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)
###################################################################### END   LAYER ONE  #################################################################################
for k in range(1,test):
    for i in range(1, calcs):                                                   # generates iterations 0 to calcs; indented inside the forloop is INSIDE forloop
      rng = random.Random()           
      number = rng.randrange(rannumrangestart, rannumrangeend)
      rannum = (number / rannumdiv)
      sum += rannum
      checksum += sum
      fltrannum = float("{0:.4f}".format(rannum))
      fltsum = float("{0:.4f}".format(sum))
      fltchecksum = float("{0:.4f}".format(checksum))
      #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)        # prints the full list of calculations leading up to ANS1, ANS2, ANS3 
      #End of for loop
    #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)          # prints the last like of values used to calc ANS1, ANS2, ANS3 
    ans1 = fltsum % rannumdiv                                                   # ans1 = mod of sum
    ans2 = fltchecksum % rannumdiv                                              # ans2 = mod of sum of sums = mod of checksums
    fltans1 = float("{0:.4f}".format(ans1))
    fltans2 = float("{0:.4f}".format(ans2))
    #list1 = []                                                                 # use if using two lists: list1 (inside of for loop) appends to list2 (outside of for loop)
    #list1.append(fltans1)                                                      # therefore storing the data into a separate list; need to do this if we are storing any more
    list1.append(fltans2)                                                      # than one column of nubmers (ANS1, ANS2, ANS3)
    #list2.append(list1)
# End of for loop
    for item in list1:
        print(item)
   #     from collections import Counter
   #     d = Counter(list1)
   #     new_list = list([item for item in d if d[item]>1])
   #     print(new_list)
   #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)