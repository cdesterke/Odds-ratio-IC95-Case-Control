#!usr/bin/python
# -*-coding:Latin-1 -*

"""
Created on Mon Apr 27 20:23:34 2015
IC95 on Odds ratio for CASE/CONTROL study
@author: Christophe Desterke
email : christophe.desterke@gmail.com
python3.4
"""


import os
import math
continuer = True

while continuer:

	print("	--------------------------------------------------")
	print("	Calculation of  CASE/CONTROL odds ratio with IC95")
	print("	--------------------------------------------------")

	variable = input ("Enter the name of the studied variable: ")

	
#this software allows to determine the odds ratio with the IC95 and the result could be saved in a text file named CASE_CONTROL_RESULTS

#enter the numbers of subjects by group and float type conversion of the variables

	CasePos = input ("Enter the number of POSITIVE CASES: ")
	try:
		CasePos = float (CasePos)
	except ValueError:
		print('	Please enter an integrer number!')
		continue
	
	CaseNeg = input ("Enter the number of NEGATIVE CASES: ")  
	try:
		CaseNeg = float (CaseNeg)
	except ValueError:
		print('	Please enter an integrer number!')
		continue
	
	ControlPos = input ("Enter the number of POSITIVE CONTROLS: ")
	try:
		ControlPos = float (ControlPos)
	except ValueError:
		print(' Please enter an integrer number!')
		continue 
	
	ControlNeg = input ("Enter the number of NEGATIVE CONTROLS: ")
	try:
		ControlNeg = float (ControlNeg)
	except ValueError:
		print('	Please enter an integrer number!')
		continue


#calculation of intermediate variables
	TotalCase = CasePos + CaseNeg
	print('The total number of cases is: ', TotalCase)

	TotalControl = ControlPos + ControlNeg
	print('The total number of controls is: ', TotalControl)

	TotalPos = CasePos + ControlPos
	print('The total number of positive subjects is: ', TotalPos)

	TotalNeg = CaseNeg + ControlNeg
	print('The total number of negative subjects is: ', TotalNeg)



	if ControlPos !=0 and CasePos !=0 and ControlNeg !=0 and CaseNeg !=0 :
#determination of odds ratio
		OR = (CasePos/ControlPos) / (CaseNeg/ControlNeg)
		
	else:
		print('Next time enter a number of subjects different of zero!')
		break
#calculation of intermediate variables
	total = CasePos+CaseNeg+ControlPos+ControlNeg


#percentage of positivity in the group of cases
	freqPosCase = (CasePos / (CasePos + CaseNeg)) * 100
	print('The percentage of positivity in the group case is: ',freqPosCase, 'pourcents')

#percentage of positivity in the group of controls
	freqPosControl = (ControlPos / (ControlPos + ControlNeg)) * 100
	print('The percentage of positivity in the group control is: ',freqPosControl, 'pourcents')

	print("\n")
	
#determination of khi2
	if ControlPos !=0 and CasePos !=0:
		cross = (CasePos*ControlNeg)-(ControlPos*CaseNeg)
		khi=((cross*cross)*total)/((CasePos+ControlPos)*(CaseNeg+ControlNeg)*(CasePos+CaseNeg)*(ControlPos+ControlNeg))
		print("KHI2 is: ", khi)

#interpretation of khi2 test
		if khi >3.841:
			print("----------Khi2 test is SIGNIFICANT p<0.05!")
		else:
			print("----------Khi2 test is NOT significant!")
		
		
#calculation of intermediate for IC95 OR
	lnOR = math.log (OR)
	
	racine = math.sqrt (khi)
	
	slnOR = (1/racine) * lnOR
	
	borneinf = lnOR - (2 * slnOR)
	
	bornesup = lnOR + (2 * slnOR)
	
	IC95inf = math.exp (borneinf)
	
	IC95sup = math.exp (bornesup)
	
	print("\n")
	print('The Odds Ratio Case/control is: ', OR)
	print("Lower interval of IC95 on odds ratio: ", IC95inf)
	print("Higher interval of IC95 on odds ratio: ", IC95sup)
	
#interaction for saving results in an exit file	
	print("\n")
	add =  input('Do you want to add data in the file CASE_CONTROL_RESULTS (y/n)? ')
	if add == "y" or add == "Y":
		
#exit file
		variable = str (variable)
		CasePos = str (CasePos)
		CaseNeg = str (CaseNeg)
		ControlPos = str (ControlPos)
		ControlNeg = str (ControlNeg)
		freqPosCase = str (freqPosCase)
		freqPosControl = str (freqPosControl)
		OR = str (OR)
		khi = str (khi)
		IC95inf = str (IC95inf)
		IC95sup = str (IC95sup)
		
		
		mon_fichier = open ("CASE_CONTROL_RESULTS.txt", "a")
		mon_fichier.write ("\n")
		mon_fichier.write ("#")
		mon_fichier.write ("\n")
		mon_fichier.write ("Study CASE/CONTROL on the variable: " + "\t" + variable + "\n")
		mon_fichier.write ("Number of positive cases: "+ "\t" + CasePos + "\n")
		mon_fichier.write ("Number of negative cases: "+ "\t" + CaseNeg + "\n")
		mon_fichier.write ("Number of positive controls: "+ "\t" + ControlPos + "\n")
		mon_fichier.write ("Number of negative controls: "+ "\t" + ControlNeg + "\n")
		mon_fichier.write ("Percentage of positivity in the group Case: "+ "\t" + freqPosCase + "\n")
		mon_fichier.write ("Percentage of positivity in the group Control: "+ "\t" + freqPosControl + "\n")
		mon_fichier.write ("KHI2 --> significant > 3.841: " + "\t" + khi + "\n")
		mon_fichier.write ("ODDS RATIO CASE/CONTROL: "+ "\t" + OR + "\n")
		mon_fichier.write ("Lower interval of IC95 odds ratio: " + "\t" + IC95inf + "\n")
		mon_fichier.write ("Higher interval of IC95 odds ratio: " + "\t" + IC95sup + "\n")
		
		mon_fichier.close()
		


#interaction with exit of the software	

	quitter =  input('Do you want to exit (y/n)? ')
	if quitter == "y" or quitter == "Y":
		continuer = False
os.system("pause")
