# store all instances to their corresponding column
dateTime = []
p = []
T = []
Tpot = []
Tdew = []
rh = []
VPmax = []
VPact = []
VPdef = []
sh = []
H2OC = []
rho = []
wv = []
maxwv = []
wd = []

dateTime2 = []
p2 = []
T2 = []
Tpot2 = []
Tdew2 = []
rh2 = []
VPmax2 = []
VPact2 = []
VPdef2 = []
sh2 = []
H2OC2 = []
rho2 = []
wv2 = []
maxwv2 = []
wd2 = []
# calculated mean for each column
pavg = 0
Tavg = 0
Tpotavg = 0
Tdewavg = 0
rhavg = 0
VPmaxavg = 0
VPactavg = 0
VPdefavg = 0
shavg = 0 
H2OCavg = 0
rhoavg = 0
wvavg = 0
maxwvavg = 0
wdavg = 0

pavg2 = 0
Tavg2 = 0
Tpotavg2 = 0
Tdewavg2 = 0
rhavg2 = 0
VPmaxavg2 = 0
VPactavg2 = 0
VPdefavg2 = 0
shavg2 = 0 
H2OCavg2 = 0
rhoavg2 = 0
wvavg2 = 0
maxwvavg2 = 0
wdavg2 = 0
# depending on which csv to cluster, but by default we are going to use this data set
csv = "jena_climate_2009_2016.txt"
# clustered columns
c1 = "T (degC)"
c2 = "wd (deg)"