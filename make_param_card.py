import sys

f=open('yield.txt',"r")
lines=f.readlines()
x1=[]
for i in lines:
	#print(i.split('\n')[0])
	x1.append(float(i.split('\n')[0]))


f.close()

YIELD = x1[int(sys.argv[3])]
BKG = 0
if int(sys.argv[1]) < 500:
	BKG = 113.41
else:
	BKG = 36.21


 ### YR18 ###
input_text="""max 1  number of channels
jmax 1  number of backgrounds
kmax 2  number of nuisance parameters (sources of systematical uncertainties)
-----------------------------------------------------------------------------
bin                  dm
observation          2
-----------------------------------------------------------------------------
bin                  dm        dm
process              si        bk
process              0         1
#Mmed = 100 G L= 3 ab-1
#rate                 91.52     511.10
#rate                 108.15      694.99
#rate                 8.84      26.40
#rate                 17.24     59.98
## phase 1
#rate                 0.007     23.45
#rate                 10.38     33.85
## phase 2
#rate                  4.09    36.21

rate                 """+str(YIELD)+"""      """+str(BKG)+"""
#rate                97        328363
----------------------------------------------------------------------------
lumi        lnN      1.010     1.010
bg_sum      lnN      -         1.100

#pu          lnN      1.010     1.010
#jet_Scale   lnN      1.010     1.010
#bjets       lnN      1.010     1.010
#MET         lnN      1.100     1.100
"""
inputfile = open("./datacard/{0}_{1}_datacard.txt".format(sys.argv[1],sys.argv[2]),"w")
inputfile.write(input_text)
inputfile.close()

'''
### NO UNC
input_text="""max 1  number of channels
jmax 1  number of backgrounds
kmax 0  number of nuisance parameters (sources of systematical uncertainties)
-----------------------------------------------------------------------------
bin                  dm
observation          2
-----------------------------------------------------------------------------
bin                  dm        dm
process              si        bk
process              0         1
#Mmed = 100 G L= 3 ab-1
#rate                 91.52     511.10
#rate                 108.15      694.99
#rate                 8.84      26.40
#rate                 17.24     59.98
## phase 1
#rate                 0.007     23.45
#rate                 10.38     33.85
## phase 2
#rate                  4.09    36.21

rate                 """+str(YIELD)+"""      113.41
#rate                97        328363
----------------------------------------------------------------------------
#lumi        lnN      1.010     1.010
#bg_sum      lnN      -         1.100

#pu          lnN      1.010     1.010
#jet_Scale   lnN      1.010     1.010
#bjets       lnN      1.010     1.010
#MET         lnN      1.100     1.100
"""


inputfile = open("./datacard/{0}_{1}_no_datacard.txt".format(sys.argv[1],sys.argv[2]),"w")
inputfile.write(input_text)
inputfile.close()
'''


