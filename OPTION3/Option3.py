import random
import numpy as numpy
import pandas as pd
import time
import csv
from collections import Counter
###################################################################### START LAYER ONE #################################################################################
############################ USER Inputs ######################################
########################################################################################################################################################################
test = 10             #number of total tests
n = 255                 #number being divided by in the mod calculation
calcs = 5              #total number of calculations for each test
rannumrangestart = 1    #starting range of random number
rannumrangeend = 100    #ending range of random number
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
trialnum = []
list2 = []                                                                      # ONE list, TWO cols method
lista = []                                                                      # TWO lists, ONE col (each) method
listb = []
###########################    EQNS    ##############################
#print ("i: 0","RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)
###################################################################### END   LAYER ONE  #################################################################################

###############################################       TestData OPTION1 #########################################################
#df1 = pd.DataFrame(columns = ['INDEX_Results','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','Val_kthTest', 'Val_nthIt','Val_RN','Val_A', 'Val_B'])
#df2 = pd.DataFrame(columns = ['INDEX_Results','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','PIVOT_FinalVal_kthTest', 'PIVOT_FinalVal_nthIt','PIVOT_FinalVal_RN','PIVOT_FinalVal_A', 'PIVOT_FinalVal_B','PIVOT_ModA','PIVOT_ModB','PIVOT_TestResult'])

###############################################       TestData OPTION2 #########################################################
#df1 = pd.DataFrame(columns = ['INDEX_TestResults','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','Val_kthTest', 'Val_nthIt','Val_RN','Val_A', 'Val_B'])
#df2 = pd.DataFrame(columns = ['INDEX_TestResults','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','Val_kthTest', 'Val_nthIt','Val_RN','Val_A', 'Val_B','PIVOT_FinalVal_kthTest', 'PIVOT_FinalVal_nthIt','PIVOT_FinalVal_RN','PIVOT_FinalVal_A', 'PIVOT_FinalVal_B','PIVOT_ModA','PIVOT_ModB','PIVOT_TestResult'])

###############################################       TestData OPTION3 #########################################################

df1 = pd.DataFrame(columns = ['INDEX_TestResults','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','Val_kthTest', 'Val_nthIt','Val_RN','Val_A', 'Val_B','PIVOT_FinalVal_kthTest', 'PIVOT_FinalVal_nthIt','PIVOT_FinalVal_RN','PIVOT_FinalVal_A', 'PIVOT_FinalVal_B','PIVOT_ModA','PIVOT_ModB','PIVOT_TestResult'])
df2 = pd.DataFrame(columns = ['INDEX_TestResults','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','Val_kthTest', 'Val_nthIt','Val_RN','Val_A', 'Val_B','PIVOT_FinalVal_kthTest', 'PIVOT_FinalVal_nthIt','PIVOT_FinalVal_RN','PIVOT_FinalVal_A', 'PIVOT_FinalVal_B','PIVOT_ModA','PIVOT_ModB','PIVOT_TestResult'])

for k in range(0,test):
    #df1 = pd.DataFrame(columns = ['Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Val_kTest', 'Val_nthIt','Val_RN','Val_A', 'Val_B'])
    #dictionary1 = {'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend, 'Input_RNRangeDiv': rannumdiv, 'Val_kTest': test, 'Val_nthIt': calcs, 'Val_RN': fltrannum, 'Val_A': fltsum, "Val_B": fltchecksum}
    #df1 = pd.DataFrame(columns = ['Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Val_kTest', 'Val_nthIt','Val_RN','Val_A', 'Val_B'])
    for i in range(0, calcs):                                                   # generates iterations 0 to calcs; indented inside the forloop is INSIDE forloop
      rng = random.Random()           
      number = rng.randrange(rannumrangestart, rannumrangeend)
      rannum = (number / rannumdiv)
      sum += rannum
      checksum += sum
      fltrannum = float("{0:.4f}".format(rannum))
      fltsum = float("{0:.4f}".format(sum))
      fltchecksum = float("{0:.4f}".format(checksum))
###############################################       TestData OPTION1 #########################################################
      #dictionary1 = {'INDEX_Results':[0],'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend, 'Input_RNRangeDiv': rannumdiv, 'Input_ModDiv':n,'Val_kthTest': k, 'Val_nthIt': i, 'Val_RN': fltrannum, 'Val_A': fltsum, "Val_B": fltchecksum}
      #df1 = df1.append(dictionary1,ignore_index=True)

###############################################       TestData OPTION2 #########################################################
      #dictionary1 = {'INDEX_TestResults':[0],'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend, 'Input_RNRangeDiv': rannumdiv, 'Input_ModDiv':n,'Val_kthTest': k, 'Val_nthIt': i, 'Val_RN': fltrannum, 'Val_A': fltsum, 'Val_B': fltchecksum}
      #df1 = df1.append(dictionary1,ignore_index=True)

###############################################       TestData OPTION3 #########################################################
      dictionary1 = {'INDEX_TestResults':[0],'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend, 'Input_RNRangeDiv': rannumdiv, 'Input_ModDiv':n,'Val_kthTest': k, 'Val_nthIt': i, 'Val_RN': fltrannum, 'Val_A': fltsum, 'Val_B': fltchecksum,'PIVOT_FinalVal_kthTest': [0], 'PIVOT_FinalVal_nthIt': [0], 'PIVOT_FinalVal_RN': [0], 'PIVOT_FinalVal_A': [0], 'PIVOT_FinalVal_B': [0],'PIVOT_ModA': [0],'PIVOT_ModB': [0],'PIVOT_TestResult':[0]}
      df1 = df1.append(dictionary1,ignore_index=True)

      #End of for loop
    #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)          # prints the last like of values used to calc ANS1, ANS2, ANS3 
    ans1 = fltsum % rannumdiv                                                   # ans1 = mod of sum
    ans2 = fltchecksum % rannumdiv                                              # ans2 = mod of sum of sums = mod of checksums
    fltans1 = float("{0:.4f}".format(ans1))
    fltans2 = float("{0:.4f}".format(ans2))
    list1 = []                                                                 # ONE list, TWO cols: use if appending two sets of data to ONE list, to make that list a 2d array
    list1.append(fltans1)                                                      # fltans1 is added to list1
    list1.append(fltans2)                                                      # fltans2 is added to list1
    list2.append(list1)                                                        # list1 is appended to list2 and stored to list2 as a 2d (two columns of data) 
    ############################################################################ TWO lists, ONE cols (one set of data added to each separate list) 
    lista.append(fltans1)                                                      # fltans1 is dded to lista
    listb.append(fltans2)                                                      # fltans1 is dded to listb
    #for item in list1:
    #    from collections import Counter
    #    d = Counter(list1)
    #    new_list = list([item for item in d if d[item]>1])
    #    #print(new_list)
    #    print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)
    #for item in lista:
    #    print(item)
    #    from collections import Counter
    #    d = Counter(list1)
    #    new_list = list([item for item in d if d[item]>1])
    #    #print(new_list)
    #    print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)
    # The purpose of keeping both methods of list adding in this script is because later down the road when using data frames, (currently I call cariables), it may be more efficient to call variables. won't know until I get there.
###############################################       TestData OPTION1 #########################################################
    #dictionary2 = {'INDEX_Results':[0],'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend,'Input_RNRangeDiv': rannumdiv,'Input_ModDiv':n, 'PIVOT_FinalVal_kthTest': calcs, 'PIVOT_FinalVal_nthIt': test, 'PIVOT_FinalVal_RN': fltrannum, 'PIVOT_FinalVal_A': fltsum, 'PIVOT_FinalVal_B': fltchecksum,'PIVOT_ModA': fltans1,'PIVOT_ModB': fltans2,'PIVOT_TestResult':[0]}
    #df2 = df2.append(dictionary2,ignore_index=True)
################################################       TestData OPTION2 #########################################################
    #dictionary2 = {'INDEX_TestResults':[0],'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend,'Input_RNRangeDiv': rannumdiv,'Input_ModDiv':n, 'Val_kthTest': [0], 'Val_nthIt': [0], 'Val_RN': [0], 'Val_A': [0], 'Val_B': [0],'PIVOT_FinalVal_kthTest': calcs, 'PIVOT_FinalVal_nthIt': test, 'PIVOT_FinalVal_RN': fltrannum, 'PIVOT_FinalVal_A': fltsum, 'PIVOT_FinalVal_B': fltchecksum,'PIVOT_ModA': fltans1,'PIVOT_ModB': fltans2,'PIVOT_TestResult':[0]}
    #df2 = df2.append(dictionary2,ignore_index=True)
###############################################       TestData OPTION3 #########################################################
    dictionary2 = {'INDEX_TestResults':[0],'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend,'Input_RNRangeDiv': rannumdiv,'Input_ModDiv':n, 'Val_kthTest': [0], 'Val_nthIt': [0], 'Val_RN': [0], 'Val_A': [0], 'Val_B': [0],'PIVOT_FinalVal_kthTest': calcs, 'PIVOT_FinalVal_nthIt': test, 'PIVOT_FinalVal_RN': fltrannum, 'PIVOT_FinalVal_A': fltsum, 'PIVOT_FinalVal_B': fltchecksum,'PIVOT_ModA': fltans1,'PIVOT_ModB': fltans2,'PIVOT_TestResult':[0]}
    df2 = df2.append(dictionary2,ignore_index=True)
# End of for loop
################################################## TestData ALL OPTIONS #######################################################
df1.to_csv("TestData{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))
df2.to_csv("TestResults{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))
