df1 = pd.DataFrame(columns = ['INDEX_TestResults','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','Val_kthTest', 'Val_nthIt','Val_RN','Val_A', 'Val_B'])

df2 = pd.DataFrame(columns = ['INDEX_TestResults','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','PIVOT_FinalVal_kthTest', 'PIVOT_FinalVal_nthIt','PIVOT_FinalVal_RN','PIVOT_Val_A', 'PIVOT_Val_B','PIVOT_ModA','PIVOT_ModB','PIVOT_TestResult'])





# TestData CSV contains PIVOT columns from TestResults CSV
df1 = pd.DataFrame(columns = ['INDEX_TestResults','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','Val_kthTest', 'Val_nthIt','Val_RN','Val_A', 'Val_B','PIVOT_FinalVal_kthTest', 'PIVOT_FinalVal_nthIt','PIVOT_FinalVal_RN','PIVOT_FinalVal_A', 'PIVOT_FinalVal_B','PIVOT_ModA','PIVOT_ModB','PIVOT_TestResult'])
dictionary1 = {'INDEX_TestResults':df2,'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend, 'Input_RNRangeDiv': rannumdiv, 'Input_ModDiv':n,'Val_kthTest': k, 'Val_nthIt': i, 'Val_RN': fltrannum, 'Val_A': fltsum, 'Val_B': fltchecksum,'PIVOT_FinalVal_kthTest': calcs, 'PIVOT_FinalVal_nthIt': test, 'PIVOT_FinalVal_RN': [0], 'PIVOT_FinalVal_A': [0], 'PIVOT_FinalVal_B': [0],'PIVOT_ModA': [0],'PIVOT_ModB': [0],'PIVOT_TestResult':[0]}
df1 = df1.append(dictionary1,ignore_index=True)

df2 = pd.DataFrame(columns = ['INDEX_TestResults','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','PIVOT_FinalVal_kthTest', 'PIVOT_FinalVal_nthIt','PIVOT_FinalVal_RN','PIVOT_FinalVal_A', 'PIVOT_FinalVal_B','PIVOT_ModA','PIVOT_ModB','PIVOT_TestResult'])
dictionary2 = {'INDEX_TestResults':[0],'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend,'Input_RNRangeDiv': rannumdiv,'Input_ModDiv':n, 'PIVOT_FinalVal_kthTest': calcs, 'PIVOT_FinalVal_nthIt': test, 'PIVOT_FinalVal_RN': fltrannum, 'PIVOT_FinalVal_A': fltsum, 'PIVOT_FinalVal_B': fltchecksum,'PIVOT_ModA': fltans1,'PIVOT_ModB': fltans2,'PIVOT_TestResult':[0]}
df2 = df2.append(dictionary2,ignore_index=True)
 
 
 
# TestResults CSV contains Val columns from TestData CSV
df1 = pd.DataFrame(columns = ['INDEX_TestResults','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','Val_kthTest', 'Val_nthIt','Val_RN','Val_A', 'Val_B','PIVOT_FinalVal_kthTest', 'PIVOT_FinalVal_nthIt','PIVOT_FinalVal_RN','PIVOT_FinalVal_A', 'PIVOT_FinalVal_B','PIVOT_ModA','PIVOT_ModB','PIVOT_TestResult'])
dictionary1 = {'INDEX_TestResults':df2,'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend, 'Input_RNRangeDiv': rannumdiv, 'Input_ModDiv':n,'Val_kthTest': k, 'Val_nthIt': i, 'Val_RN': fltrannum, 'Val_A': fltsum, 'Val_B': fltchecksum}
df1 = df1.append(dictionary1,ignore_index=True)

df2 = pd.DataFrame(columns = ['INDEX_TestResults','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','PIVOT_FinalVal_kthTest', 'PIVOT_FinalVal_nthIt','PIVOT_FinalVal_RN','PIVOT_FinalVal_A', 'PIVOT_FinalVal_B','PIVOT_ModA','PIVOT_ModB','PIVOT_TestResult'])
dictionary2 = {'INDEX_TestResults':[0],'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend,'Input_RNRangeDiv': rannumdiv,'Input_ModDiv':n, 'PIVOT_FinalVal_kthTest': calcs, 'PIVOT_FinalVal_nthIt': test, 'PIVOT_FinalVal_RN': fltrannum, 'PIVOT_FinalVal_A': fltsum, 'PIVOT_FinalVal_B': fltchecksum,'PIVOT_ModA': fltans1,'PIVOT_ModB': fltans2,'PIVOT_TestResult':[0]}
df2 = df2.append(dictionary2,ignore_index=True)


# TestData CSV DOES NOT contains PIVOT columns from TestResults CSV
df1 = pd.DataFrame(columns = ['INDEX_TestResults','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','Val_kthTest', 'Val_nthIt','Val_RN','Val_A', 'Val_B'])
dictionary1 = {'INDEX_TestResults':df2,'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend, 'Input_RNRangeDiv': rannumdiv, 'Input_ModDiv':n,'Val_kthTest': k, 'Val_nthIt': i, 'Val_RN': fltrannum, 'Val_A': fltsum, 'Val_B': fltchecksum}
df1 = df1.append(dictionary1,ignore_index=True)
df2 = pd.DataFrame(columns = ['INDEX_TestResults','Input_TotalNumTests','Input_TotalNumIts','Input_RNRangeStart','Input_RNRangeEnd','Input_RNRangeDiv','Input_ModDiv','PIVOT_FinalVal_kthTest', 'PIVOT_FinalVal_nthIt','PIVOT_FinalVal_RN','PIVOT_FinalVal_A', 'PIVOT_FinalVal_B','PIVOT_ModA','PIVOT_ModB','PIVOT_TestResult'])
dictionary2 = {'INDEX_TestResults':[0],'Input_TotalNumTests': test, 'Input_TotalNumIts': calcs, 'Input_RNRangeStart': rannumrangestart,'Input_RNRangeEnd':rannumrangeend,'Input_RNRangeDiv': rannumdiv,'Input_ModDiv':n, 'PIVOT_FinalVal_kthTest': calcs, 'PIVOT_FinalVal_nthIt': test, 'PIVOT_FinalVal_RN': fltrannum, 'PIVOT_FinalVal_A': fltsum, 'PIVOT_FinalVal_B': fltchecksum,'PIVOT_ModA': fltans1,'PIVOT_ModB': fltans2,'PIVOT_TestResult':[0]}
df2 = df2.append(dictionary2,ignore_index=True)
df1.to_csv("TestData{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))
df2.to_csv("TestResults{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")))      