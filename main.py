
# data analysis library
import pandas
import pylab as pylabvar
from variables import *
# python library for kmeans
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA # Principal component analysis


# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
f = open("jena_climate_2009_2016.txt", "r")
labels = f.readline()
# Option to minimize the dataset by manipulating the range
for i in range(0,420551): # attain a subset of the data (420552 rows of data)
    b,c,d,e,ff,g,h,i,j,k,l,m,n,o = f.readline().strip().split(',') # attain input after a ','


    if i < str(223409):
        p.append(b)
        T.append(c)
        Tpot.append(d)
        Tdew.append(e)
        rh.append(ff)
        VPmax.append(g)
        VPact.append(h)
        VPdef.append(i)
        sh.append(j)
        H2OC.append(k)
        rho.append(l)
        wv.append(m)
        maxwv.append(n)
        wd.append(o)
    else:
        p2.append(b)
        T2.append(c)
        Tpot2.append(d)
        Tdew2.append(e)
        rh2.append(ff)
        VPmax2.append(g)
        VPact2.append(h)
        VPdef2.append(i)
        sh2.append(j)
        H2OC2.append(k)
        rho2.append(l)
        wv2.append(m)
        maxwv2.append(n)
        wd2.append(o)

f.close()                         # file input
fo = open("outfile.csv", "w")    # output file

# write all the data labels first 
fo.write(labels)

# For acquiring the 2nd cluster of the mean for each column
for i in range(0,233049):
    #dateTime[i]+","+
    fo.write(p[i]+","+T[i]+","+Tpot[i]+","+Tdew[i]+","+rh[i]+","+VPmax[i]+","+VPact[i]+","+VPdef[i]+","+sh[i]+","+H2OC[i]+","+rho[i]+","+wv[i]+","+maxwv[i]+","+wd[i]+"\n")
    pavg += float(p[i])
    Tavg += float(T[i])
    Tpotavg += float(Tpot[i])
    Tdewavg += float(Tdew[i])
    rhavg += float(rh[i])
    VPmaxavg += float(VPmax[i])
    VPactavg += float(VPact[i])
    VPdefavg += float(VPdef[i])
    shavg += float(sh[i]) 
    H2OCavg += float(H2OC[i])
    rhoavg += float(rho[i])
    wvavg += float(wv[i])
    maxwvavg += float(maxwv[i])
    wdavg += float(wd[i])


for i in range(0,187502):
    #dateTime[i]+","+
    fo.write(p[i]+","+T[i]+","+Tpot[i]+","+Tdew[i]+","+rh[i]+","+VPmax[i]+","+VPact[i]+","+VPdef[i]+","+sh[i]+","+H2OC[i]+","+rho[i]+","+wv[i]+","+maxwv[i]+","+wd[i]+"\n")
    pavg2 += float(p[i])
    Tavg2 += float(T[i])
    Tpotavg2 += float(Tpot[i])
    Tdewavg2 += float(Tdew[i])
    rhavg2 += float(rh[i])
    VPmaxavg2 += float(VPmax[i])
    VPactavg2 += float(VPact[i])
    VPdefavg2 += float(VPdef[i])
    shavg2 += float(sh[i]) 
    H2OCavg2 += float(H2OC[i])
    rhoavg2 += float(rho[i])
    wvavg2 += float(wv[i])
    maxwvavg2 += float(maxwv[i])
    wdavg2 += float(wd[i])
fo.close()

# Trying to replicate the results using the simple k mean on weka
def clusterMeans():
    fo = open("mean.csv", "w") # output 
    n = 233049
    j = 187502
    # Acquire Cluster 1 and Cluster 2, which are both averages of the original data set split in two
    fo.write("Cluster 1,Cluster 2\n"+str(pavg/n)+","+str(pavg2/j)+"\n"+str(Tavg/n)+","+str(Tavg2/j)+"\n"+str(Tpotavg/n)+","+str(Tpotavg2/j)+"\n")
    fo.write(str(Tdewavg/n)+","+str(Tdewavg2/j)+"\n"+str(rhavg/n)+","+str(rhavg2/j)+"\n")
    fo.write(str(VPmaxavg/n)+","+str(VPmaxavg2/j)+"\n"+str(VPactavg/n)+","+str(VPactavg2/j)+"\n"+str(VPdefavg/n)+","+str(VPdefavg2/j)+"\n"+str(shavg/n)+",")
    fo.write(str(shavg2/j)+"\n"+str(H2OCavg/n)+","+str(H2OCavg2/j)+"\n")
    fo.write(str(rhoavg/n)+","+str(rhoavg2/j)+"\n"+str(wvavg/n)+","+str(wvavg2/j)+"\n"+str(maxwvavg/n)+","+str(maxwvavg2/j)+"\n")
    fo.write(str(wdavg/n)+","+str(wdavg2/j)+"\n")
    global csv,c1,c2
    csv = "mean.csv"
    c1 = "Cluster 1"
    c2 = "Cluster 2"
    fo.close()

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

def kmean():
    var = pandas.read_csv(csv)
    # set the x axis from the values under the column in c2
    # which corresponds to the column name in the csv file
    x = var[[c1]]
    # set the y axis from the values under the column in c2
    y = var[[c2]] 
    
    z = PCA(n_components=1).fit(x) 
    z1 = z.transform(y)
    z2 = z.transform(x)
    # set to 2 clusters of data; k = 2
    k=KMeans(n_clusters=2) 
    outputk=k.fit(x)
    

    # get all values from rows of column z2 an z1
    pylabvar.scatter(z2[:, 0], z1[:, 0], c=outputk.labels_)
    # set the title for the x axis
    pylabvar.xlabel(c1)
    # set the title for the y axis
    pylabvar.ylabel(c2)
    # display the title of the entire graph    
    pylabvar.title('Plot: jena_climate_2009_2016_clustered')
    # display the analysis
    pylabvar.show()

# clusterMeans()         # optional, I tried to get data like it showed on weka..... 
kmean()                 # takes a while to load...

