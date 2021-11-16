import random
import numpy as numpy
import pandas as pd
import time
import csv
from collections import Counter
###################################################################### START LAYER ONE #################################################################################
############################ USER Inputs ######################################
########################################################################################################################################################################
test = 1000             #number of total tests
n = 255                 #number being divided by in the mod calculation
calcs = 20              #total number of calculations for each test
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
df1 = pd.DataFrame(columns = ['INDEX_Results','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','Val_kthTest', 'Val_nthIt','Val_RN','Val_A', 'Val_B'])
df2 = pd.DataFrame(columns = ['INDEX_Results','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','PIVOT_FinalVal_kthTest', 'PIVOT_FinalVal_nthIt','PIVOT_FinalVal_RN','PIVOT_Val_A', 'PIVOT_Val_B','PIVOT_ModA','PIVOT_ModB','PIVOT_TestResult'])
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
      #print ("k:", k, "i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)        # prints the full list of calculations leading up to ANS1, ANS2, ANS3 
      #Cols = ["Input_TotalNumTests", "Input_TotalNumIts","Input_RNRangeStart","Input_RNRangeEnd","Input_RNRangeDiv","Input_Mod_Div","Val_kTest","Val_nthIt","Val_RN","ANS(A)_Val","ANS(B)_Val","MOD(A)_ANS","MOD(B)_ANS"]
      dictionary1 = {'INDEX_Results':df2,'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend, 'Input_RNRangeDiv': rannumdiv, 'Input_ModDiv':n,'Val_kthTest': k, 'Val_nthIt': i, 'Val_RN': fltrannum, 'Val_A': fltsum, "Val_B": fltchecksum}
      df1 = df1.append(dictionary1,ignore_index=True)
      #dataframe1 = pd.DataFrame(dictionary1, index=[k*i])
    #dataframe1.to_csv("DustinTestData2{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))
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
    # The purpose of keeping both methods of list adding in this script is because later down the road when using data frames, (currently I call cariables), it may be more efficient to call variables. won't know until I get there.

    # 'CSVData','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','FinalVal_kthTest', 'FinalVal_nthIt','FinalVal_RN','FinalVal_A', 'FinalVal_B','Ans_ModA','Ans_ModB','TestResult']
    dictionary2 = {'INDEX_Results':[0],'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend,'Input_RNRangeDiv': rannumdiv,'Input_ModDiv':n, 'FinalVal_kthTest': calcs, 'FinalVal_nthIt': test, 'FinalVal_RN': fltrannum, 'FinalVal_A': fltsum, 'FinalVal_B': fltchecksum,'Ans_ModA': fltans1,'Ans_ModB': fltans2,'TestResult':[0]}
    df2 = df2.append(dictionary2,ignore_index=True)
#df1.to_csv("DustinTestData1{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))
#df2.to_csv("DustinTestResults{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))
# End of for loop
    for item in list1:
        from collections import Counter
        d = Counter(list1)
        new_list = list([item for item in d if d[item]>1])
        print(new_list)
        #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)
    for item in lista:
        from collections import Counter
        d = Counter(list1)
        new_list = list([item for item in d if d[item]>1])
        print(new_list)
        #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)

df1.to_csv("TestData{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))
df2.to_csv("TestResults{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))

