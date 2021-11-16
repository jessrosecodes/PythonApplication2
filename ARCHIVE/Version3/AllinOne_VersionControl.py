import random
import numpy as numpy
import pandas as pd
import time
import csv
from collections import Counter
###################################################################### START LAYER ONE #################################################################################
############################ USER Inputs ######################################
testnum = 5
########################################################################################################################################################################
test = 1001             #number of total tests
n = 255                 #number being divided by in the mod calculation
calcs = 21              #total number of calculations for each test
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
list2 = []                                                                      # list allows us to append, unlike array; comment out if using 1 list
list1 = []                                                                       # comment if using more than one list
###########################    EQNS    ##############################
#print ("i: 0","RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)
###################################################################### END   LAYER ONE  #################################################################################
df1 = pd.DataFrame(columns = ['Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Val_kTest', 'Val_nthIt','Val_RN','Val_A', 'Val_B'])
df2 = pd.DataFrame(columns = ['CSVData','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','FinalVal_kthTest', 'FinalVal_nthIt','FinalVal_RN','FinalVal_A', 'FinalVal_B','Ans_ModA','Ans_ModB','TestResult'])
for k in range(1,test):
    #df1 = pd.DataFrame(columns = ['Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Val_kTest', 'Val_nthIt','Val_RN','Val_A', 'Val_B'])
    #dictionary1 = {'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend, 'Input_RNRangeDiv': rannumdiv, 'Val_kTest': test, 'Val_nthIt': calcs, 'Val_RN': fltrannum, 'Val_A': fltsum, "Val_B": fltchecksum}
    #df1 = pd.DataFrame(columns = ['Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Val_kTest', 'Val_nthIt','Val_RN','Val_A', 'Val_B'])
    for i in range(1, calcs):                                                   # generates iterations 0 to calcs; indented inside the forloop is INSIDE forloop
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
      dictionary1 = {'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend, 'Input_RNRangeDiv': rannumdiv, 'Val_kthTest': k, 'Val_nthIt': i, 'Val_RN': fltrannum, 'Val_A': fltsum, "Val_B": fltchecksum}
      df1 = df1.append(dictionary1,ignore_index=True)
      #dataframe1 = pd.DataFrame(dictionary1, index=[k*i])
    #dataframe1.to_csv("DustinTestData2{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))
      #End of for loop
    #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)          # prints the last like of values used to calc ANS1, ANS2, ANS3 
    ans1 = fltsum % rannumdiv                                                   # ans1 = mod of sum
    ans2 = fltchecksum % rannumdiv                                              # ans2 = mod of sum of sums = mod of checksums
    fltans1 = float("{0:.4f}".format(ans1))
    fltans2 = float("{0:.4f}".format(ans2))
    list1 = []                                                                 # use if using two lists: list1 (inside of for loop) appends to list2 (outside of for loop)
    list1.append(fltans1)                                                      # therefore storing the data into a separate list; need to do this if we are storing any more
    list2.append(fltans2)                                                      # than one column of nubmers (ANS1, ANS2, ANS3)
    list2.append(list1)
    # 'CSVData','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','FinalVal_kthTest', 'FinalVal_nthIt','FinalVal_RN','FinalVal_A', 'FinalVal_B','Ans_ModA','Ans_ModB','TestResult']
    dictionary2 = {'CSVData':[0],'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend,'Input_RNRangeDiv': rannumdiv,'Input_ModDiv':n, 'FinalVal_kthTest': calcs, 'FinalVal_nthIt': test, 'FinalVal_RN': fltrannum, 'FinalVal_A': fltsum, 'FinalVal_B': fltchecksum,'Ans_ModA': fltans1,'Ans_ModB': fltans2,'TestResult':[0]}
    df2 = df2.append(dictionary2,ignore_index=True)
df1.to_csv("DustinTestData1{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))
df2.to_csv("DustinTestData2{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S"))
# End of for loop
    #for item in list1:
    #    from collections import Counter
    #    d = Counter(list1)
    #    new_list = list([item for item in d if d[item]>1])
        #print(new_list)
        #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)
        #dictionary2 = {'Total_Test_Number': test,'Total_Iterations_Num': calcs, 'RN_Range_Start': rannumrangestart,'RN_Range_End':rannumrangeend, 'RN_Range_Div': rannumdiv, 'Mod_Ans_Div': n, 'ANS_A': fltans1, 'ANS_B': fltans2}
        #dataframe2 = pd.DataFrame(dictionary2, index=[k])
        #dataframe2.to_csv("DustinTestData2{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))
        #dictionary3 = {'list1': list1}
        #dataframe3 = pd.DataFrame(dictionary3, index=[k,i])
        #dataframe3.to_csv("DustinTestData3{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))

#import random
#import numpy as numpy
#import pandas as pd
#import time
#import csv
#from collections import Counter
####################################################################### START LAYER ONE #################################################################################
############################# USER Inputs ######################################
#testnum = 1
#test = 1001             #number of total tests
#n = 255                 #number being divided by in the mod calculation
#calcs = 21              #total number of calculations for each test
#rannumrangestart = 1    #starting range of random number
#rannumrangeend = 100    #ending range of random number
#rannumdiv = 80            # number random number will be divided by
############################ Inputs User shouldn't change ############
#rannum = 0              #starting value of randon number
#sum = 0                 #starting value of sum
#checksum = 0            #starting value of checksum
############################# USER Inputs ######################################
############################    SYNTAX  ##############################
#fltrannum = float("{0:.4f}".format(rannum))
#fltsum = float("{0:.4f}".format(sum))
#fltchecksum = float("{0:.4f}".format(checksum))
############################    SYNTAX  ##############################
############################   EQNS    ##############################
#list2 = []                                                                      # list allows us to append, unlike array; comment out if using 1 list
##list1 = []                                                                       # comment if using more than one list
############################    EQNS    ##############################
##print ("i: 0","RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)
####################################################################### END   LAYER ONE  #################################################################################
#for k in range(1,test):
#    for i in range(1, calcs):                                                   # generates iterations 0 to calcs; indented inside the forloop is INSIDE forloop
#      rng = random.Random()           
#      number = rng.randrange(rannumrangestart, rannumrangeend)
#      rannum = (number / rannumdiv)
#      sum += rannum
#      checksum += sum
#      fltrannum = float("{0:.4f}".format(rannum))
#      fltsum = float("{0:.4f}".format(sum))
#      fltchecksum = float("{0:.4f}".format(checksum))
#      #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)        # prints the full list of calculations leading up to ANS1, ANS2, ANS3 
#      #End of for loop
#    #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)          # prints the last like of values used to calc ANS1, ANS2, ANS3 
#    ans1 = fltsum % rannumdiv                                                   # ans1 = mod of sum
#    ans2 = fltchecksum % rannumdiv                                              # ans2 = mod of sum of sums = mod of checksums
#    fltans1 = float("{0:.4f}".format(ans1))
#    fltans2 = float("{0:.4f}".format(ans2))
#    list1 = []                                                                 # use if using two lists: list1 (inside of for loop) appends to list2 (outside of for loop)
#    list1.append(fltans1)                                                      # therefore storing the data into a separate list; need to do this if we are storing any more
#    list1.append(fltans2)                                                      # than one column of nubmers (ANS1, ANS2, ANS3)
#    list2.append(list1)
## End of for loop
#    for item in list1:
#        from collections import Counter
#        d = Counter(list1)
#        new_list = list([item for item in d if d[item]>1])
#        print(new_list)
#    print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)
##dictionary2 = {'Total_Test_Number': test,'Total_Iterations_Num': calcs, 'RN_Range_Start': rannumrangestart,'RN_Range_End':rannumrangeend, 'RN_Range_Div': rannumdiv, 'Mod_Ans_Div': n, 'ANS_A': fltans1, 'ANS_B': fltans2}
##dataframe2 = pd.DataFrame(dictionary2, index=[k])
##dataframe2.to_csv("DustinTestData2{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))
##dictionary3 = {'list1': list1}
##dataframe3 = pd.DataFrame(dictionary3, index=[k,i])
##dataframe3.to_csv("DustinTestData3{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))



#import random
#import numpy as numpy
#import pandas as pd
#import time
#import csv
#from collections import Counter
####################################################################### START LAYER ONE #################################################################################
############################# USER Inputs ######################################
#testnum = 1
#test = 5                #number of total tests
#n = 255                 #number being divided by in the mod calculation
#calcs = 21              #total number of calculations for each test
#rannumrangestart = 1    #starting range of random number
#rannumrangeend = 100    #ending range of random number
#rannumdiv = 80            # number random number will be divided by
############################ Inputs User shouldn't change ############
#rannum = 0              #starting value of randon number
#sum = 0                 #starting value of sum
#checksum = 0            #starting value of checksum
############################# USER Inputs ######################################
############################    SYNTAX  ##############################
#fltrannum = float("{0:.4f}".format(rannum))
#fltsum = float("{0:.4f}".format(sum))
#fltchecksum = float("{0:.4f}".format(checksum))
############################    SYNTAX  ##############################
############################   EQNS    ##############################
#list2 = []                                                                      # list allows us to append, unlike array; comment out if using 1 list
##list1 = []                                                                       # comment if using more than one list
############################    EQNS    ##############################
##print ("i: 0","RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)
####################################################################### END   LAYER ONE  #################################################################################
#for k in range(1,test):
#    for i in range(1, calcs):                                                   # generates iterations 0 to calcs; indented inside the forloop is INSIDE forloop
#      rng = random.Random()           
#      number = rng.randrange(rannumrangestart, rannumrangeend)
#      rannum = (number / rannumdiv)
#      sum += rannum
#      checksum += sum
#      fltrannum = float("{0:.4f}".format(rannum))
#      fltsum = float("{0:.4f}".format(sum))
#      fltchecksum = float("{0:.4f}".format(checksum))
#      #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)        # prints the full list of calculations leading up to ANS1, ANS2, ANS3 
#      #End of for loop
#    #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)          # prints the last like of values used to calc ANS1, ANS2, ANS3 
#    ans1 = fltsum % rannumdiv                                                   # ans1 = mod of sum
#    ans2 = fltchecksum % rannumdiv                                              # ans2 = mod of sum of sums = mod of checksums
#    fltans1 = float("{0:.4f}".format(ans1))
#    fltans2 = float("{0:.4f}".format(ans2))
#    list1 = []                                                                 # use if using two lists: list1 (inside of for loop) appends to list2 (outside of for loop)
#    list1.append(fltans1)                                                      # therefore storing the data into a separate list; need to do this if we are storing any more
#    list1.append(fltans2)                                                      # than one column of nubmers (ANS1, ANS2, ANS3)
#    list2.append(list1)
## End of for loop
#    for item in list1:
#        from collections import Counter
#        d = Counter(list1)
#        new_list = list([item for item in d if d[item]>1])
        
#        #print(new_list)
#    print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum, "MODA & MODB", list2)
#    dictionary2 = {'Total_Test_Number': test,'Total_Iterations_Num': calcs, 'RN_Range_Start': rannumrangestart,'RN_Range_End':rannumrangeend, 'RN_Range_Div': rannumdiv, 'Mod_Ans_Div': n, 'ANS_A': fltans1, 'ANS_B': fltans2}
#    dataframe2 = pd.DataFrame(dictionary2, index=[k])
#    dataframe2.to_csv("DustinTestData2{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))
#    dictionary3 = {'list1': list1}
#    dataframe3 = pd.DataFrame(dictionary3, index=[k,i])
#    dataframe3.to_csv("DustinTestData3{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))
#import random
#import numpy as numpy
#import pandas as pd
#import time
#import csv
#from collections import Counter
#import array as arr
####################################################################### START LAYER ONE #################################################################################
############################# USER Inputs ######################################
#test = 1001             #number of total tests
#n = 255                 #number being divided by in the mod calculation
#calcs = 20              #total number of calculations for each test
#rannumrangestart = 1    #starting range of random number
#rannumrangeend = 100  #ending range of random number
#rannumdiv = 80            # number random number will be divided by
############################ Inputs User shouldn't change ############
#rannum = 0              #starting value of randon number
#sum = 0                 #starting value of sum
#checksum = 0            #starting value of checksum
############################# USER Inputs ######################################
############################    SYNTAX  ##############################
#fltrannum = float("{0:.4f}".format(rannum))
#fltsum = float("{0:.4f}".format(sum))
#fltchecksum = float("{0:.4f}".format(checksum))
############################    SYNTAX  ##############################
############################   EQNS    ##############################
#list2 = []                                                                      # list allows us to append, unlike array; comment out if using 1 list
#list1 = []
#listA = []
#listB = []
##listC = []
##listD = []
##listE = []
##listF = []

## comment if using more than one list
############################    EQNS    ##############################
##print ("i: 0","RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)
####################################################################### END   LAYER ONE  #################################################################################
#for k in range(1,test):
#    listA.append(k)
#    for i in range(1, calcs):   # generates iterations 0 to calcs; indented inside the forloop is INSIDE forloop
#        listB.append(i)
#        rng = random.Random()           
#        number = rng.randrange(rannumrangestart, rannumrangeend)
#        rannum = (number / rannumdiv)
#        sum += rannum
#        checksum += sum
#        fltrannum = float("{0:.4f}".format(rannum))
#        fltsum = float("{0:.4f}".format(sum))
#        fltchecksum = float("{0:.4f}".format(checksum))
#      #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)        # prints the full list of calculations leading up to ANS1, ANS2, ANS3 
#      #End of for loop
#    #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)          # prints the last like of values used to calc ANS1, ANS2, ANS3
#    ans1 = fltsum % rannumdiv                                                   # ans1 = mod of sum
#    ans2 = fltchecksum % rannumdiv                                              # ans2 = mod of sum of sums = mod of checksums
#    fltans1 = float("{0:.4f}".format(ans1))
#    fltans2 = float("{0:.4f}".format(ans2))                                                             # use if using two lists: list1 (inside of for loop) appends to list2 (outside of for loop)
#    list1.append(fltans1)                                                      # therefore storing the data into a separate list; need to do this if we are storing any more
#    list2.append(fltans2)                                                      # than one column of nubmers (ANS1, ANS2, ANS3)
#    #Cols = ["Input_TotalNumTests", "Input_TotalNumIts","Input_RNRangeStart","Input_RNRangeEnd","Input_RNRangeDiv","Input_Mod_Div","(k)Test_Val","(n)thIt_Val","RN_Val","ANS(A)_Val","ANS(B)_Val","MOD(A)_ANS","MOD(B)_ANS"]
#    #Rows = [listA,
#    #    listB,
#    #    list1,
#    #    list2]
##dictionary2 = {'Total_Test_Number': test,'Total_Iterations_Num': calcs, 'RN_Range_Start': rannumrangestart,'RN_Range_End':rannumrangeend, 'RN_Range_Div': rannumdiv, 'Mod_Ans_Div': n, 'ANS_A': fltans1, 'ANS_B': fltans2}
##dataframe2 = pd.DataFrame(dictionary2, index=[test])
##dataframe2.to_csv("DustinTestData_2{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))
##Cols = ["Input_TotalNumTests", "Input_TotalNumIts","Input_RNRangeStart","Input_RNRangeEnd","Input_RNRangeDiv","Input_Mod_Div","(k)Test_Val","(n)thIt_Val","RN_Val","ANS(A)_Val","ANS(B)_Val","MOD(A)_ANS","MOD(B)_ANS"]
##Rows = [listA,
##        ListB,
##        list1,
##        list2]
#with open('shows.csv', 'w') as f:
#    using csv.writer method from CSV package
        
#        write = csv.writer(f)
#        write.writerow(Cols)
#        write.writerows(Rows)
#        list2.append(list1)
 
#    End of for loop
#    for item in list1:
#        from collections import Counter
#        d = Counter(list1)
#        new_list = list([item for item in d if d[item]>1])
#    dictionary3 = {'list1': list1}
#    dataframe3 = pd.DataFrame(dictionary3, index=[5])
#    dataframe3.to_csv("DustinTestData_3{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))

#import random
#import numpy as numpy
#import pandas as pd
#import time
#import csv
#from collections import Counter
#import array as arr
####################################################################### START LAYER ONE #################################################################################
############################# USER Inputs ######################################
#testnum = 1
#test = 1001             #number of total tests
#n = 255                 #number being divided by in the mod calculation
#calcs = 21              #total number of calculations for each test
#rannumrangestart = 1    #starting range of random number
#rannumrangeend = 100    #ending range of random number
#rannumdiv = 80            # number random number will be divided by
############################ Inputs User shouldn't change ############
#rannum = 0              #starting value of randon number
#sum = 0                 #starting value of sum
#checksum = 0            #starting value of checksum
############################# USER Inputs ######################################
############################    SYNTAX  ##############################
#fltrannum = float("{0:.4f}".format(rannum))
#fltsum = float("{0:.4f}".format(sum))
#fltchecksum = float("{0:.4f}".format(checksum))
############################    SYNTAX  ##############################
############################   EQNS    ##############################
#list2 = []                                                                      # list allows us to append, unlike array; comment out if using 1 list
##list1 = []
#listA = []                                                                       # comment if using more than one list
############################    EQNS    ##############################
##print ("i: 0","RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)
####################################################################### END   LAYER ONE  #################################################################################
#for k in range(1,test):
#    for i in range(1, calcs):                                                   # generates iterations 0 to calcs; indented inside the forloop is INSIDE forloop
#        rng = random.Random()           
#        number = rng.randrange(rannumrangestart, rannumrangeend)
#        rannum = (number / rannumdiv)
#        sum += rannum
#        checksum += sum
#        fltrannum = float("{0:.4f}".format(rannum))
#        fltsum = float("{0:.4f}".format(sum))
#        fltchecksum = float("{0:.4f}".format(checksum))
#        print(k, ",", i,",", fltrannum, ",", fltsum, ",", fltchecksum)
#        #print ("testnumber:",k, "i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)        # prints the full list of calculations leading up to ANS1, ANS2, ANS3 
#      #End of for loop
#               # prints the last like of values used to calc ANS1, ANS2, ANS3 
#    ans1 = fltsum % rannumdiv                                                   # ans1 = mod of sum
#    ans2 = fltchecksum % rannumdiv                                              # ans2 = mod of sum of sums = mod of checksums
#    fltans1 = float("{0:.4f}".format(ans1))
#    fltans2 = float("{0:.4f}".format(ans2))
#    list1 = []                                                                 # use if using two lists: list1 (inside of for loop) appends to list2 (outside of for loop)
#    list1.append(fltans1)                                                      # therefore storing the data into a separate list; need to do this if we are storing any more
#    list1.append(fltans2)                                                      # than one column of nubmers (ANS1, ANS2, ANS3)
#    list2.append(list1)
#    #print(k, ",", i,",", fltrannum, ",", fltsum, ",", fltchecksum)
#    dictionary1 = {k, ",", i,",", fltrannum, ",", fltsum, ",", fltchecksum}
#    dataframe1 = pd.DataFrame(dictionary1)
#    dataframe1.to_csv("DustinTestData_1{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))
#    #print ("testnumber:",k, "i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum,"MODA:", fltans1, "MODB:", fltans2)   
## End of for loop
#    for item in list1:
#        from collections import Counter
#        d = Counter(list1)
#        new_list = list([item for item in d if d[item]>1])
#        #print(new_list)
#    #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)