# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:42:13 2021

@author: KM
"""

import pandas as pd
'import numpy as np'
import re
from matplotlib import pyplot as plt
import seaborn as sns
import os
# import statistics as stats
# import openpyxl as xl;
# import xlsxwriter

# ---------------- Load the data ----------------------

data21 = pd.read_excel(r'Z:\Kasia Muter\3RACE WT hen msh polyA\Minion_SAM_files\Minion06_S21.xlsx') 
df21 = pd.DataFrame(data21, columns= ['Unnamed: 5','Unnamed: 9'])
df21_all = pd.DataFrame(data21)
df21 = df21[10:]
print (df21)
df21['len'] = df21['Unnamed: 9'].str.len()

data22 = pd.read_excel(r'Z:\Kasia Muter\3RACE WT hen msh polyA\Minion_SAM_files\Minion06_S22.xlsx') 
df22 = pd.DataFrame(data22, columns= ['Unnamed: 5','Unnamed: 9'])
df22_all = pd.DataFrame(data22)
df22 = df22[10:]
print (df22)
df22['len'] = df22['Unnamed: 9'].str.len()

data23 = pd.read_excel(r'Z:\Kasia Muter\3RACE WT hen msh polyA\Minion_SAM_files\Minion04_S23.xlsx') 
df23 = pd.DataFrame(data23, columns= ['Unnamed: 5','Unnamed: 9'])
df23_all = pd.DataFrame(data23)
df23 = df23[10:]
print (df23)
df23['len'] = df23['Unnamed: 9'].str.len()

data24 = pd.read_excel(r'Z:\Kasia Muter\3RACE WT hen msh polyA\Minion_SAM_files\Minion04_S24.xlsx') 
df24 = pd.DataFrame(data24, columns= ['Unnamed: 5','Unnamed: 9'])
df24_all = pd.DataFrame(data24)
df24 = df24[10:]
print (df24)
df24['len'] = df24['Unnamed: 9'].str.len()

data25 = pd.read_excel(r'Z:\Kasia Muter\3RACE WT hen msh polyA\Minion_SAM_files\Minion05_S25.xlsx') 
df25 = pd.DataFrame(data25, columns= ['Unnamed: 5','Unnamed: 9'])
df25_all = pd.DataFrame(data25)
df25 = df25[10:]
print (df25)
df25['len'] = df25['Unnamed: 9'].str.len()

data26 = pd.read_excel(r'Z:\Kasia Muter\3RACE WT hen msh polyA\Minion_SAM_files\Minion06_S26.xlsx') 
df26 = pd.DataFrame(data26, columns= ['Unnamed: 5','Unnamed: 9'])
df26_all = pd.DataFrame(data26)
df26 = df26[10:]
print (df26)
df26['len'] = df26['Unnamed: 9'].str.len()

# =============================================================================
# 
# df = [df21, df22, df23, df24, df25, df26]
# df = pd.concat(df)
# tails = pd.DataFrame(columns=['seq'])
# 
# for i in range(len(df)):
#     tmp_CIGAR = df.iloc[i,0]
#     tmp_seq = df.iloc[i,1]
#     tmp_CIGAR1 = re.split('(\d+)',tmp_CIGAR)
#     last_L = tmp_CIGAR1[-1:]
#     last_N = tmp_CIGAR1[-2:-1]
#     
#     if last_L == ['S']:
#         last_N = int(last_N[0])
#         tails = tails.append({'seq': tmp_seq[-last_N:]}, ignore_index=True)
# 
# tails['len'] = tails['seq'].str.len()
# tails = tails.drop(tails[tails['len'] < 5].index)
# 
# tails['AT'] = tails['seq'].str.count('A') + tails['seq'].str.count('T')
# tails['A'] = tails['seq'].str.count('A')
# 
# tails['percentage'] = tails['AT']/tails['len']
# 
# tails['percentageA'] = tails['A']/tails['len']
# tails95A = tails.drop(tails[tails['percentageA'] < 0.95].index)
# tails5A = tails.drop(tails[tails['percentageA'] >= 0.95].index)
# 
# tails99AT = tails.drop(tails[tails['percentage'] <= 0.99].index)
# 
# tails99AT['begining'] = tails99AT.seq.astype(str).str[:1]
# tails99AT['end'] = tails99AT.seq.astype(str).str[-1:]
# 
# beginT = sum(tails99AT['begining']=='T')
# endT = sum(tails99AT['end']=='T')
# begin_and_end_T = sum((tails99AT['begining']=='T') & (tails99AT['end']=='T'))
# 
# msh_mean_tail = tails['len'].mean()
# 
# MSHs = ['MSH polyA begin with T',
#         'MSH polyA end with T', 
#         'MSH polyA begin and end with T', 
#         'MSH polyA begin and end with A']
#   
# percent = [beginT/len(tails99AT), 
#            endT/len(tails99AT), 
#            begin_and_end_T/len(tails99AT),
#            1- (beginT/len(tails99AT) + endT/len(tails99AT) + begin_and_end_T/len(tails99AT))]
# 
# fig = plt.figure(figsize =(10, 7))
# plt.pie(percent, labels = MSHs, shadow=True, startangle=90, autopct='%1.1f%%',
#         colors = ['royalblue','coral','limegreen','silver'])
#   
# plt.show()
# 
# onlyA = pd.DataFrame(columns=['seq'])           
# pattern = re.compile("A*")
# 
# for i in range(len(tails99AT)):
#     if pattern.fullmatch( tails99AT.iloc[i,0]):
#         onlyA = onlyA.append({'seq': tails99AT.iloc[i,0]}, ignore_index=True)
# 
# beginTseq = tails99AT[tails99AT.begining == 'T']
# endTseq = tails99AT[tails99AT.end == 'T']
# onlyA['len'] = onlyA['seq'].str.len()
# 
# plt.figure(figsize=(10,7), dpi= 80)
# sns.distplot(beginTseq['len'], color="dodgerblue", label="begin with T")
# sns.distplot(endTseq['len'], color="orange", label="ends with T")
# sns.distplot(onlyA['len'], color="deeppink", label="onlyA")
# plt.legend();
# =============================================================================

for j in range(1,7):
    
    # keep only softclipped seqences
    locals()["df2"+str(j)+'_new'] = pd.DataFrame(columns=['Unnamed: 5','Unnamed: 9','len'])
    for i in range(len(locals()["df2"+str(j)])):
        tmp_CIGAR = locals()["df2"+str(j)].iloc[i,0]
        tmp_seq = locals()["df2"+str(j)].iloc[i,1]
        tmp_CIGAR1 = re.split('(\d+)',tmp_CIGAR)
        last_L = tmp_CIGAR1[-1:]
        last_N = tmp_CIGAR1[-2:-1]
        if last_L == ['S']:
            last_N = int(last_N[0])
            locals()["df2"+str(j)+'_new'] = locals()["df2"+str(j)+'_new'].append(pd.concat([locals()["df2"+str(j)].iloc[i,],pd.Series(tmp_seq[-last_N:], name=locals()["df2"+str(j)].iloc[i,].name)]))
            #df21_new = df21_new({'seq': tmp_seq[-last_N:]})
    
    # filter data
    locals()["df2"+str(j)+'_new'] = locals()["df2"+str(j)+'_new'].rename(columns = {0: 'seq'})
    locals()["df2"+str(j)+'_new']['len'] = locals()["df2"+str(j)+'_new']['seq'].str.len() #długosc sekwencji
    locals()["df2"+str(j)+'_new'] = locals()["df2"+str(j)+'_new'].drop(locals()["df2"+str(j)+'_new'][locals()["df2"+str(j)+'_new']['len'] < 5].index) #usuwanie ogonow o dlugosci mniejszej niz 5
    locals()["df2"+str(j)+'_new']['A'] = locals()["df2"+str(j)+'_new']['seq'].str.count('A') #policzenie ile "A" jest w sekwencji
    locals()["df2"+str(j)+'_new']['AT'] = locals()["df2"+str(j)+'_new']['seq'].str.count('A') + locals()["df2"+str(j)+'_new']['seq'].str.count('T') #policzenie ile jest "A" i "T" w sekw.
    locals()["df2"+str(j)+'_new']['ATpercentage'] = locals()["df2"+str(j)+'_new']['AT']/locals()["df2"+str(j)+'_new']['len'] #procent "A" i "T" w sekw.
    locals()["df2"+str(j)+'_new'] = locals()["df2"+str(j)+'_new'].drop(locals()["df2"+str(j)+'_new'][locals()["df2"+str(j)+'_new']['ATpercentage'] <= 0.99].index) #wyrzucenie sekw. które mają mniej niż 99% "A" i "T"
    
    # split to patterns
    locals()["df2"+str(j)+'_onlyA'] = pd.DataFrame(columns = locals()["df2"+str(j)+'_new'].columns)
    p1 = re.compile('[A]+')
    
    for k in range(len(locals()["df2"+str(j)+'_new'])): 
        if p1.fullmatch(locals()["df2"+str(j)+'_new'].iloc[k,3]):
            locals()["df2"+str(j)+'_onlyA'] = locals()["df2"+str(j)+'_onlyA'].append(locals()["df2"+str(j)+'_new'].iloc[k,])
     
    locals()["df2"+str(j)+'_TthenA']= pd.DataFrame(columns = locals()["df2"+str(j)+'_new'].columns)
    p2 = re.compile('[T]+[A]+')
    
    for k in range(len(locals()["df2"+str(j)+'_new'])): 
        if p2.fullmatch(locals()["df2"+str(j)+'_new'].iloc[k,3]):
            locals()["df2"+str(j)+'_TthenA'] = locals()["df2"+str(j)+'_TthenA'].append(locals()["df2"+str(j)+'_new'].iloc[k,])
     
    locals()["df2"+str(j)+'_AthenT'] = pd.DataFrame(columns = locals()["df2"+str(j)+'_new'].columns)
    p3 = re.compile('[A]+[T]+')
    
    for k in range(len(locals()["df2"+str(j)+'_new'])): 
        if p3.fullmatch(locals()["df2"+str(j)+'_new'].iloc[k,3]):
            locals()["df2"+str(j)+'_AthenT'] = locals()["df2"+str(j)+'_AthenT'].append(locals()["df2"+str(j)+'_new'].iloc[k,])
            
    locals()["df2"+str(j)+'_mix'] = pd.DataFrame(columns = locals()["df2"+str(j)+'_new'].columns)
    
    for k in range(len(locals()["df2"+str(j)+'_new'])): 
        if (bool(p1.fullmatch(locals()["df2"+str(j)+'_new'].iloc[k,0])) == False) & (bool(p2.fullmatch( locals()["df2"+str(j)+'_new'].iloc[k,0])) == False) & (bool(p3.fullmatch(locals()["df2"+str(j)+'_new'].iloc[k,0])) == False):
            locals()["df2"+str(j)+'_mix'] = locals()["df2"+str(j)+'_mix'].append(locals()["df2"+str(j)+'_new'].iloc[k,])
    
    # save fasta files
    ofile = open('df2'+str(j)+'_onlyA.txt', 'w') 
    for x in range(len(locals()["df2"+str(j)+'_all'].iloc[locals()["df2"+str(j)+'_onlyA'].index,9])):
        if (x < len(locals()["df2"+str(j)+'_all'].iloc[locals()["df2"+str(j)+'_onlyA'].index,9])-1):
            ofile.write(">" + str(locals()["df2"+str(j)+'_onlyA'].index[x]) + "\n" + locals()["df2"+str(j)+'_all'].iloc[locals()["df2"+str(j)+'_onlyA'].index[x],9] + "\n")
        else:
            ofile.write(">" + str(locals()["df2"+str(j)+'_onlyA'].index[x]) + "\n" + locals()["df2"+str(j)+'_all'].iloc[locals()["df2"+str(j)+'_onlyA'].index[x],9])
    ofile.close()
    os.rename('df2'+str(j)+'_onlyA.txt', 'df2'+str(j)+'_onlyA_F.fasta')
    
    ofile = open('df2'+str(j)+'_TthenA.txt', 'w')
    for x in range(len(locals()["df2"+str(j)+'_all'].iloc[locals()["df2"+str(j)+'_TthenA'].index,9])):
        if (x < len(locals()["df2"+str(j)+'_all'].iloc[locals()["df2"+str(j)+'_TthenA'].index,9])-1):
            ofile.write(">" + str(locals()["df2"+str(j)+'_TthenA'].index[x]) + "\n" + locals()["df2"+str(j)+'_all'].iloc[locals()["df2"+str(j)+'_TthenA'].index[x],9] + "\n")
        else:
            ofile.write(">" + str(locals()["df2"+str(j)+'_TthenA'].index[x]) + "\n" + locals()["df2"+str(j)+'_all'].iloc[locals()["df2"+str(j)+'_TthenA'].index[x],9])
    ofile.close()
    os.rename('df2'+str(j)+'_TthenA.txt', 'df2'+str(j)+'_TthenA_F.fasta')
    
    ofile = open('df2'+str(j)+'_AthenT.txt', 'w') 
    for x in range(len(locals()["df2"+str(j)+'_all'].iloc[locals()["df2"+str(j)+'_AthenT'].index,9])):
        if (x < len(locals()["df2"+str(j)+'_all'].iloc[locals()["df2"+str(j)+'_AthenT'].index,9])-1):
            ofile.write(">" + str(locals()["df2"+str(j)+'_AthenT'].index[x]) + "\n" + locals()["df2"+str(j)+'_all'].iloc[locals()["df2"+str(j)+'_AthenT'].index[x],9] + "\n")
        else:
            ofile.write(">" + str(locals()["df2"+str(j)+'_AthenT'].index[x]) + "\n" + locals()["df2"+str(j)+'_all'].iloc[locals()["df2"+str(j)+'_AthenT'].index[x],9])
    ofile.close()
    os.rename('df2'+str(j)+'_AthenT.txt', 'df2'+str(j)+'_AthenT_F.fasta')
    
    ofile = open('df2'+str(j)+'_mix.txt', 'w') 
    for x in range(len(locals()["df2"+str(j)+'_all'].iloc[locals()["df2"+str(j)+'_mix'].index,9])):
        if (x < len(locals()["df2"+str(j)+'_all'].iloc[locals()["df2"+str(j)+'_mix'].index,9])-1):
            ofile.write(">" + str(locals()["df2"+str(j)+'_mix'].index[x]) + "\n" + locals()["df2"+str(j)+'_all'].iloc[locals()["df2"+str(j)+'_mix'].index[x],9] + "\n")
        else:
            ofile.write(">" + str(locals()["df2"+str(j)+'_mix'].index[x]) + "\n" + locals()["df2"+str(j)+'_all'].iloc[locals()["df2"+str(j)+'_mix'].index[x],9])
    ofile.close()
    os.rename('df2'+str(j)+'_mix.txt', 'df2'+str(j)+'_mix_F.fasta')
    
    

# =============================================================================
# wb21 = xl.load_workbook(r"Z:\Kasia Muter\3RACE WT hen msh polyA\Minion_SAM_files\Minion06_S21.xlsx")
# res1 = wb21.worksheets[0]
# 
# workbook = xlsxwriter.Workbook('Z:\Kasia Muter\3RACE WT hen msh polyA\Minion_SAM_files\Minion01_S21_onlyA.xlsx')
# worksheet = workbook.add_worksheet()
# #worksheet.write(12, 1, df21.iloc[df21_onlyA.index,])
# #workbook.close()
# 
# df21_all.iloc[df21_onlyA.index,].to_excel("Minion01_S21_onlyA.xlsx",sheet_name='Minion01_S21_onlyA', startrow = 11, index = False, header = False)  
# 
# filename1 = r"Z:\Kasia Muter\3RACE WT hen msh polyA\Minion_SAM_files\Minion01_S21_onlyA.xlsx"
# wb21_A = xl.load_workbook(filename1)
# res2 = wb21_A.active
# 
# mr = 11
# mc = res1.max_column
# 
# for i in range (1, mr + 1):
#     for j in range (1, mc + 1):
#         # reading cell value from source excel file
#         c = res1.cell(row = i, column = j)
#   
#         # writing the read value to destination excel file
#         res2.cell(row = i, column = j).value = c.value
#   
# # saving the destination excel file
# wb21_A.save(str(filename1))
# 
# =============================================================================

# create fasta file

# 21

# ofile = open("df21_onlyA.txt", "w")
# for i in range(len(df21_all.iloc[df21_onlyA.index,9])):
#     if (i < len(df21_all.iloc[df21_onlyA.index,9])-1):
#         ofile.write(">" + str(df21_onlyA.index[i]) + "\n" + df21_all.iloc[df21_onlyA.index[i],9] + "\n")
#     else:
#         ofile.write(">" + str(df21_onlyA.index[i]) + "\n" + df21_all.iloc[df21_onlyA.index[i],9])
# ofile.close()
# os.rename("df21_onlyA.txt", 'df21_onlyA_f.fasta')

# ofile = open("21_TthenA.txt", "w")
# for i in range(len(df21_all.iloc[df21_TthenA.index,9])):
#     if (i < len(df21_all.iloc[df21_TthenA.index,9])-1):
#         ofile.write(">" + str(df21_TthenA.index[i]) + "\n" + df21_all.iloc[df21_TthenA.index[i],9] + "\n")
#     else:
#         ofile.write(">" + str(df21_TthenA.index[i]) + "\n" + df21_all.iloc[df21_TthenA.index[i],9])
# ofile.close()
# os.rename("21_TthenA.txt", '21_TthenA_f.fasta')


# ------------------- WT vs.hen ----------------------

WT_matrix = [df21, df23, df25]
WT_matrix = pd.concat(WT_matrix)
WT_matrix.rename(columns={'Unnamed: 5' : 'CIGAR', 'Unnamed: 9' : 'seq'})

WT_tails = pd.DataFrame(columns=['seq', 'whole_seq'])

for i in range(len(WT_matrix)):
    tmp_CIGAR = WT_matrix.iloc[i,0]
    tmp_seq = WT_matrix.iloc[i,1]
    tmp_CIGAR1 = re.split('(\d+)',tmp_CIGAR)
    last_L = tmp_CIGAR1[-1:]
    last_N = tmp_CIGAR1[-2:-1]
    
    if last_L == ['S']:
        last_N = int(last_N[0])
        
        WT_tails = WT_tails.append({'seq': tmp_seq[-last_N:], 'whole_seq':WT_matrix.iloc[i,1]}, ignore_index=True)
        #WT_tails.iloc[i,1] = WT_matrix.iloc[i,1]
        

hen_matrix = [df22, df24, df26]
hen_matrix = pd.concat(hen_matrix)
hen_matrix.rename(columns={'Unnamed: 5' : 'CIGAR', 'Unnamed: 9' : 'seq'})

#hen_tails = pd.DataFrame(columns=['seq'])
hen_tails = pd.DataFrame(columns=['seq', 'whole_seq'])


for i in range(len(hen_matrix)):
    tmp_CIGAR = hen_matrix.iloc[i,0]
    tmp_seq = hen_matrix.iloc[i,1]
    tmp_CIGAR1 = re.split('(\d+)',tmp_CIGAR)
    last_L = tmp_CIGAR1[-1:]
    last_N = tmp_CIGAR1[-2:-1]
    
    if last_L == ['S']:
        last_N = int(last_N[0])
        hen_tails = hen_tails.append({'seq': tmp_seq[-last_N:], 'whole_seq':hen_matrix.iloc[i,1]}, ignore_index=True)
        #hen_tails = hen_tails.append({'seq': tmp_seq[-last_N:]}, ignore_index=True)


WT_tails['len'] = WT_tails['seq'].str.len() #długosc sekwencji
WT_tails = WT_tails.drop(WT_tails[WT_tails['len'] < 5].index) #usuwanie ogonow o dlugosci mniejszej niz 5
WT_tails['A'] = WT_tails['seq'].str.count('A') #policzenie ile "A" jest w sekwencji
WT_tails['AT'] = WT_tails['seq'].str.count('A') + WT_tails['seq'].str.count('T') #policzenie ile jest "A" i "T" w sekw.
WT_tails['ATpercentage'] = WT_tails['AT']/WT_tails['len'] #procent "A" i "T" w sekw.
WT_tails = WT_tails.drop(WT_tails[WT_tails['ATpercentage'] <= 0.99].index) #wyrzucenie sekw. które mają mniej niż 99% "A" i "T"


hen_tails['len'] = hen_tails['seq'].str.len() #długosc sekwencji
hen_tails = hen_tails.drop(hen_tails[hen_tails['len'] < 5].index) #usuwanie ogonow o dlugosci mniejszej niz 5
hen_tails['A'] = hen_tails['seq'].str.count('A') #policzenie ile "A" jest w sekwencji
hen_tails['AT'] = hen_tails['seq'].str.count('A') + hen_tails['seq'].str.count('T') #policzenie ile jest "A" i "T" w sekw.
hen_tails['ATpercentage'] = hen_tails['AT']/hen_tails['len'] #procent "A" i "T" w sekw.
hen_tails = hen_tails.drop(hen_tails[hen_tails['ATpercentage'] <= 0.99].index) #wyrzucenie sekw. które mają mniej niż 99% "A" i "T"

# unique seqences of WT and hen
WT_tails_unique = WT_tails.drop_duplicates(subset = ["seq"])
hen_tails_unique = hen_tails.drop_duplicates(subset = ["seq"])

# mean length of polyA tails of WT and hen
WT_mean_tail = WT_tails['len'].mean()
hen_mean_tail = hen_tails['len'].mean()

# ------------ only A seqences ---------------
WT_onlyA_tails = WT_tails[WT_tails['A'] == WT_tails['len']]
hen_onlyA_tails = hen_tails[hen_tails['A'] == hen_tails['len']]

# mean length of onlyA polyA tails of WT and hen
WT_mean_onlyA_tails = WT_onlyA_tails['len'].mean()
hen_mean_onlyA_tails = hen_onlyA_tails['len'].mean()

# ------------- A and T seqences ---------------------
WT_AT_tails = WT_tails[WT_tails['A'] != WT_tails['len']]
hen_AT_tails = hen_tails[hen_tails['A'] != hen_tails['len']]

# mean length of A and T polyA tails of WT and hen
WT_mean_AT_tails = WT_AT_tails['len'].mean()
hen_mean_AT_tails = hen_AT_tails['len'].mean()

# begin T and then only A
WT_TthenA = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])
hen_TthenA = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])

pattern = re.compile('[T]+[A]+')

for i in range(len(WT_AT_tails)): 
    if pattern.fullmatch( WT_AT_tails.iloc[i,0]):
        WT_TthenA = WT_TthenA.append(WT_AT_tails.iloc[i,])
        
for i in range(len(hen_AT_tails)): 
    if pattern.fullmatch( hen_AT_tails.iloc[i,0]):
        hen_TthenA = hen_TthenA.append(hen_AT_tails.iloc[i,])
        
# only A but ends with T
WT_AthenT = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])
hen_AthenT = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])

pattern = re.compile('[A]+[T]+')

for i in range(len(WT_AT_tails)): 
    if pattern.fullmatch( WT_AT_tails.iloc[i,0]):
        WT_AthenT = WT_AthenT.append(WT_AT_tails.iloc[i,])
        
for i in range(len(hen_AT_tails)): 
    if pattern.fullmatch( hen_AT_tails.iloc[i,0]):
        hen_AthenT = hen_AthenT.append(hen_AT_tails.iloc[i,])

# mix T inside the seqence
p1 = re.compile('[T]+[A]+')
p2 = re.compile('[A]+[T]+')
p3 = re.compile('[A]+')

WT_AandTmix = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])
hen_AandTmix = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])

for i in range(len(WT_AT_tails)): 
    if (bool(p1.fullmatch( WT_AT_tails.iloc[i,0])) == False) & (bool(p2.fullmatch( WT_AT_tails.iloc[i,0])) == False) & (bool(p3.fullmatch( WT_AT_tails.iloc[i,0])) == False):
        WT_AandTmix = WT_AandTmix.append(WT_AT_tails.iloc[i,])
 
for i in range(len(hen_AT_tails)): 
    if (bool(p1.fullmatch( hen_AT_tails.iloc[i,0])) == False) & (bool(p2.fullmatch( hen_AT_tails.iloc[i,0])) == False) & (bool(p3.fullmatch( hen_AT_tails.iloc[i,0])) == False):
        hen_AandTmix = hen_AandTmix.append(hen_AT_tails.iloc[i,])
        
    
# --------------------------- ABBUNDANCE OF PATTERNS --------------------------------------

# TAAAA...
pattern = re.compile('T[A]+')
WT_1TthenA = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])
hen_1TthenA = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])

for i in range(len(WT_AT_tails)): 
    if pattern.fullmatch( WT_AT_tails.iloc[i,0]):
        WT_1TthenA = WT_1TthenA.append(WT_AT_tails.iloc[i,])
        
for i in range(len(hen_AT_tails)): 
    if pattern.fullmatch( hen_AT_tails.iloc[i,0]):
        hen_1TthenA = hen_1TthenA.append(hen_AT_tails.iloc[i,])
        
# TTAAAAA....        
pattern = re.compile('TT[A]+')
WT_2TthenA = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])
hen_2TthenA = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])

for i in range(len(WT_AT_tails)): 
    if pattern.fullmatch( WT_AT_tails.iloc[i,0]):
        WT_2TthenA = WT_2TthenA.append(WT_AT_tails.iloc[i,])
for i in range(len(hen_AT_tails)): 
    if pattern.fullmatch( hen_AT_tails.iloc[i,0]):
        hen_2TthenA = hen_2TthenA.append(hen_AT_tails.iloc[i,])
        
# TTTAAAAA....        
pattern = re.compile('TTT[A]+')
WT_3TthenA = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])
hen_3TthenA = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])

for i in range(len(WT_AT_tails)): 
    if pattern.fullmatch( WT_AT_tails.iloc[i,0]):
        WT_3TthenA = WT_3TthenA.append(WT_AT_tails.iloc[i,])
for i in range(len(hen_AT_tails)): 
    if pattern.fullmatch( hen_AT_tails.iloc[i,0]):
        hen_3TthenA = hen_3TthenA.append(hen_AT_tails.iloc[i,])

# TTTTAAAAA....
pattern = re.compile('TTTT[A]+')
hen_4TthenA = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])
for i in range(len(hen_AT_tails)): 
    if pattern.fullmatch( hen_AT_tails.iloc[i,0]):
        hen_4TthenA = hen_4TthenA.append(hen_AT_tails.iloc[i,])
        

        
# ...AAAT
WT_Athen1T = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])
hen_Athen1T = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])

pattern = re.compile('[A]+T')

for i in range(len(WT_AT_tails)): 
    if pattern.fullmatch( WT_AT_tails.iloc[i,0]):
        WT_Athen1T = WT_Athen1T.append(WT_AT_tails.iloc[i,])
        
for i in range(len(hen_AT_tails)): 
    if pattern.fullmatch( hen_AT_tails.iloc[i,0]):
        hen_Athen1T = hen_Athen1T.append(hen_AT_tails.iloc[i,])
        
# ...AAATT
WT_Athen2T = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])
hen_Athen2T = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])

pattern = re.compile('[A]+TT')

for i in range(len(WT_AT_tails)): 
    if pattern.fullmatch( WT_AT_tails.iloc[i,0]):
        WT_Athen2T = WT_Athen2T.append(WT_AT_tails.iloc[i,])
        
for i in range(len(hen_AT_tails)): 
    if pattern.fullmatch( hen_AT_tails.iloc[i,0]):
        hen_Athen2T = hen_Athen2T.append(hen_AT_tails.iloc[i,])
        
# ...AAATTT
WT_Athen3T = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])
hen_Athen3T = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])

pattern = re.compile('[A]+TTT')

for i in range(len(WT_AT_tails)): 
    if pattern.fullmatch( WT_AT_tails.iloc[i,0]):
        WT_Athen3T = WT_Athen3T.append(WT_AT_tails.iloc[i,])
        
for i in range(len(hen_AT_tails)): 
    if pattern.fullmatch( hen_AT_tails.iloc[i,0]):
        hen_Athen3T = hen_Athen3T.append(hen_AT_tails.iloc[i,])
        
# ...AAATTTT
WT_Athen4T = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])
hen_Athen4T = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])

pattern = re.compile('[A]+TTTT')

for i in range(len(WT_AT_tails)): 
    if pattern.fullmatch( WT_AT_tails.iloc[i,0]):
        WT_Athen4T = WT_Athen4T.append(WT_AT_tails.iloc[i,])
        
for i in range(len(hen_AT_tails)): 
    if pattern.fullmatch( hen_AT_tails.iloc[i,0]):
        hen_Athen4T = hen_Athen4T.append(hen_AT_tails.iloc[i,])
        
# ...AAATTTTT
WT_Athen5T = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])
hen_Athen5T = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])

pattern = re.compile('[A]+TTTTT')

for i in range(len(WT_AT_tails)): 
    if pattern.fullmatch( WT_AT_tails.iloc[i,0]):
        WT_Athen5T = WT_Athen5T.append(WT_AT_tails.iloc[i,])
        
for i in range(len(hen_AT_tails)): 
    if pattern.fullmatch( hen_AT_tails.iloc[i,0]):
        hen_Athen5T = hen_Athen5T.append(hen_AT_tails.iloc[i,])
        
# ...AAATTTTTT
WT_Athen6T = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])
hen_Athen6T = pd.DataFrame(columns = ['seq', 'len', 'A', 'AT', 'ATpercentage'])

pattern = re.compile('[A]+TTTTTT')

for i in range(len(WT_AT_tails)): 
    if pattern.fullmatch( WT_AT_tails.iloc[i,0]):
        WT_Athen6T = WT_Athen6T.append(WT_AT_tails.iloc[i,])
        
for i in range(len(hen_AT_tails)): 
    if pattern.fullmatch( hen_AT_tails.iloc[i,0]):
        hen_Athen6T = hen_Athen6T.append(hen_AT_tails.iloc[i,])
        



# circle plot

WT_circle_names = ['WT only A',
        'WT A then 1T: ...AAAT', 
        'WT A then 2T: ...AAATT',
        'WT A then 3T: ...AAATTT',
        #'WT A then 4T: ...AAATTTT',
        #'WT A then 5T: ...AAATTTTT',
        'WT A then 6T: ...AAATTTTTT',
        'WT 1T then A: TAAA...', 
        'WT 2T then A: TTAAA...',
        'WT 3T then A: TTTAAA...',
        'WT mix']
  
percent = [len(WT_onlyA_tails)/len(WT_tails), 
           len(WT_Athen1T)/len(WT_tails),
           len(WT_Athen2T)/len(WT_tails),
           len(WT_Athen3T)/len(WT_tails),
           #len(WT_Athen4T)/len(WT_tails),
           #len(WT_Athen5T)/len(WT_tails),
           len(WT_Athen6T)/len(WT_tails),
           len(WT_1TthenA)/len(WT_tails),
           len(WT_2TthenA)/len(WT_tails),
           len(WT_3TthenA)/len(WT_tails),
           len(WT_AandTmix)/len(WT_tails)]

fig = plt.figure(figsize =(10, 7))
plt.pie(percent, labels = WT_circle_names, shadow=True, startangle=90, autopct='%1.1f%%',
        colors = ['royalblue','yellow','gold','orange','saddlebrown','limegreen', 'green', 'darkgreen','silver'])
  
plt.show()

hen_circle_names = ['hen only A',
        'hen A then 1T: ...AAAT', 
        'hen A then 2T: ...AAATT', 
        'hen A then 3T: ...AAATTT', 
        'hen A then 4T: ...AAATTTT', 
        'hen A then 5T: ...AAATTTTT', 
        'hen A then 6T: ...AAATTTTTT', 
        'hen 1T then A: TAAA...', 
        'hen 2T then A: TTAAA...', 
        'hen 3T then A: TTTAAA...', 
        'hen 4T then A: TTTTAAA...', 
        'hen mix']
  
percent = [len(hen_onlyA_tails)/len(hen_tails), 
           len(hen_Athen1T)/len(hen_tails),
           len(hen_Athen2T)/len(hen_tails),
           len(hen_Athen3T)/len(hen_tails),
           len(hen_Athen4T)/len(hen_tails),
           len(hen_Athen5T)/len(hen_tails),
           len(hen_Athen6T)/len(hen_tails),
           len(hen_1TthenA)/len(hen_tails),
           len(hen_2TthenA)/len(hen_tails),
           len(hen_3TthenA)/len(hen_tails),
           len(hen_4TthenA)/len(hen_tails),
           len(hen_AandTmix)/len(hen_tails)]

fig = plt.figure(figsize =(10, 7))
plt.pie(percent, labels = hen_circle_names, shadow=True, startangle=90, autopct='%1.1f%%',
        colors = ['royalblue','yellow','gold','orange','coral','chocolate','saddlebrown','limegreen', 'green', 'darkgreen', 'black','silver'])
  
plt.show()

# length plot

plt.figure(figsize=(10,7), dpi= 80)
sns.distplot(WT_onlyA_tails['len'], color="dodgerblue", label="WT only A")
sns.distplot(WT_AthenT['len'], color="coral", label="WT A then T")
sns.distplot(WT_TthenA['len'], color="limegreen", label="WT T then A")
sns.distplot(WT_AandTmix['len'], color="silver", label="WT mix")
plt.legend();

plt.figure(figsize=(10,7), dpi= 80)
sns.distplot(hen_onlyA_tails['len'], color="dodgerblue", label="hen only A")
sns.distplot(hen_AthenT['len'], color="coral", label="hen A then T")
sns.distplot(hen_TthenA['len'], color="limegreen", label="hen T then A")
sns.distplot(hen_AandTmix['len'], color="silver", label="hen mix")
plt.legend();

# lengths
WT_onlyA_mean = WT_onlyA_tails['len'].mean()
hen_onlyA_mean = hen_onlyA_tails['len'].mean()

WT_AthenT_mean = WT_AthenT['len'].mean()
hen_AthenT_mean = hen_AthenT['len'].mean()

WT_TthenA_mean = WT_TthenA['len'].mean()
hen_TthenA_mean = hen_TthenA['len'].mean()

WT_AandTmix_mean = WT_AandTmix['len'].mean()
hen_AandTmix_mean = hen_AandTmix['len'].mean()

# -------------------save to fasta files------------------
save_path = 'Z:/Kasia Muter/3RACE WT hen msh polyA/Minion_SAM_files'

# WT onlyA
file_name = "WT_onlyA.txt"
completeName = os.path.join(save_path, file_name)

ofile = open(completeName, "w")
for i in range(len(WT_onlyA_tails)):
    if (i < len(WT_onlyA_tails)-1):
        ofile.write(">" + str(WT_onlyA_tails.index[i]) + "\n" + WT_onlyA_tails['whole_seq'].iloc[i] + "\n")
    else:
        ofile.write(">" + str(WT_onlyA_tails.index[i]) + "\n" + WT_onlyA_tails['whole_seq'].iloc[i])
ofile.close()
os.rename(os.path.join(save_path, file_name), os.path.join(save_path, 'WT_onlyA_F.fasta'))

# WT T then A
file_name = "WT_TthenA.txt"
completeName = os.path.join(save_path, file_name)

ofile = open(completeName, "w")
for i in range(len(WT_TthenA)):
    if (i < len(WT_TthenA)-1):
        ofile.write(">" + str(WT_TthenA.index[i]) + "\n" + WT_TthenA['whole_seq'].iloc[i] + "\n")
    else:
        ofile.write(">" + str(WT_TthenA.index[i]) + "\n" + WT_TthenA['whole_seq'].iloc[i])
ofile.close()
os.rename(os.path.join(save_path, file_name), os.path.join(save_path, 'WT_TthenA_F.fasta'))

# WT A then T
file_name = "WT_AthenT.txt"
completeName = os.path.join(save_path, file_name)

ofile = open(completeName, "w")
for i in range(len(WT_AthenT)):
    if (i < len(WT_AthenT)-1):
        ofile.write(">" + str(WT_AthenT.index[i]) + "\n" + WT_AthenT['whole_seq'].iloc[i] + "\n")
    else:
        ofile.write(">" + str(WT_AthenT.index[i]) + "\n" + WT_AthenT['whole_seq'].iloc[i])
ofile.close()
os.rename(os.path.join(save_path, file_name), os.path.join(save_path, 'WT_AthenT_F.fasta'))

# WT AT mix
file_name = "WT_AT_mix.txt"
completeName = os.path.join(save_path, file_name)

ofile = open(completeName, "w")
for i in range(len(WT_AandTmix)):
    if (i < len(WT_AandTmix)-1):
        ofile.write(">" + str(WT_AandTmix.index[i]) + "\n" + WT_AandTmix['whole_seq'].iloc[i] + "\n")
    else:
        ofile.write(">" + str(WT_AandTmix.index[i]) + "\n" + WT_AandTmix['whole_seq'].iloc[i])
ofile.close()
os.rename(os.path.join(save_path, file_name), os.path.join(save_path, 'WT_AT_mix_F.fasta'))

# hen onlyA
file_name = "hen_onlyA.txt"
completeName = os.path.join(save_path, file_name)

ofile = open(completeName, "w")
for i in range(len(hen_onlyA_tails)):
    if (i < len(hen_onlyA_tails)-1):
        ofile.write(">" + str(hen_onlyA_tails.index[i]) + "\n" + hen_onlyA_tails['whole_seq'].iloc[i] + "\n")
    else:
        ofile.write(">" + str(hen_onlyA_tails.index[i]) + "\n" + hen_onlyA_tails['whole_seq'].iloc[i])
ofile.close()
os.rename(os.path.join(save_path, file_name), os.path.join(save_path, 'hen_onlyA_F.fasta'))

# hen T then A
file_name = "hen_TthenA.txt"
completeName = os.path.join(save_path, file_name)

ofile = open(completeName, "w")
for i in range(len(hen_TthenA)):
    if (i < len(hen_TthenA)-1):
        ofile.write(">" + str(hen_TthenA.index[i]) + "\n" + hen_TthenA['whole_seq'].iloc[i] + "\n")
    else:
        ofile.write(">" + str(hen_TthenA.index[i]) + "\n" + hen_TthenA['whole_seq'].iloc[i])
ofile.close()
os.rename(os.path.join(save_path, file_name), os.path.join(save_path, 'hen_TthenA_F.fasta'))

# hen A then T
file_name = "hen_AthenT.txt"
completeName = os.path.join(save_path, file_name)

ofile = open(completeName, "w")
for i in range(len(hen_AthenT)):
    if (i < len(hen_AthenT)-1):
        ofile.write(">" + str(hen_AthenT.index[i]) + "\n" + hen_AthenT['whole_seq'].iloc[i] + "\n")
    else:
        ofile.write(">" + str(hen_AthenT.index[i]) + "\n" + hen_AthenT['whole_seq'].iloc[i])
ofile.close()
os.rename(os.path.join(save_path, file_name), os.path.join(save_path, 'hen_AthenT_F.fasta'))

# hen AT mix
file_name = "hen_AT_mix.txt"
completeName = os.path.join(save_path, file_name)

ofile = open(completeName, "w")
for i in range(len(hen_AandTmix)):
    if (i < len(hen_AandTmix)-1):
        ofile.write(">" + str(hen_AandTmix.index[i]) + "\n" + hen_AandTmix['whole_seq'].iloc[i] + "\n")
    else:
        ofile.write(">" + str(hen_AandTmix.index[i]) + "\n" + hen_AandTmix['whole_seq'].iloc[i])
ofile.close()
os.rename(os.path.join(save_path, file_name), os.path.join(save_path, 'hen_AT_mix_F.fasta'))
