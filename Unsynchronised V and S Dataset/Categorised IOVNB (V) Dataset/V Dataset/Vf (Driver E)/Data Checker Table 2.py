# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:25:59 2020

@author: Alicja
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 16:15:08 2020

@author: onyekpeu
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 00:20:59 2020

@author: onyekpeu
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 23:42:19 2020

@author: onyekpeu
"""
import numpy as np
#import time
import pandas as pd
#from sklearn.model_selection import train_test_split
#import matplotlib.pyplot as plt
#locPreds1=pd.read_csv('S1.csv')
#locPreds2=pd.read_csv('S2.csv')
#locPreds3=np.array(pd.read_csv('S3.csv'))
#locPreds3a=locPreds3[:1233*20]
#locPreds3b=locPreds3[1233*20:1575*20]
#locPreds3c=locPreds3[1575*20:]
#locPreds4=pd.read_csv('S4.csv')
#locPredM=pd.read_csv('M.csv')
#
#locPredstr1=pd.read_csv('StratisApr1.csv')
##locPred11=pd.read_csv('StratisJan2.csv')#Test
#locPredstr3=pd.read_csv('StratisJan3.csv')
#locPredstr5=pd.read_csv('StratisJan5.csv')
#locPredstr4=pd.read_csv('StratisMar4.csv')
#locPredstr6=pd.read_csv('StratisMar5.csv')
#locPredstr7=pd.read_csv('StratisMar7.csv')
#
##locPred11=pd.read_csv('StratisTrial.csv')
#locPredy1=pd.read_csv('Y1.csv')
#locPredy2=pd.read_csv('Y2.csv')
#locPredfb01=pd.read_csv('Vasile_fb01.csv')
#locPredfb02=pd.read_csv('Vasile_fb02.csv')
#locPred15=pd.read_csv('V_tb1.csv')
#locPred16=pd.read_csv('V_tb5.csv')
#locPred17=pd.read_csv('V_ta1.csv')
#locPred18=pd.read_csv('V_ta2.csv')
#locPred19=pd.read_csv('V_ta16.csv')
#locPred20=pd.read_csv('V_ta17.csv')
#locPred21=pd.read_csv('V_ta29.csv')
#locPred22=pd.read_csv('V_ta30.csv')
#
#locPred1=pd.read_csv('vw1.csv')
#locPred2=pd.read_csv('vw2.csv')
#locPred3=pd.read_csv('vw3.csv')
#locPred3=locPred3[80:]
#locPred4=pd.read_csv('vw4.csv')
#locPred4=locPred4[46:]
#locPred5=pd.read_csv('vw5.csv')
#locPred5=locPred5[37:len(locPred5)-1]
#locPred6=pd.read_csv('vw6.csv')
#locPred6=locPred6[6:len(locPred6)-1]
#locPred7=pd.read_csv('vw7.csv')
#locPred7=locPred7[86:len(locPred7)-1]
#locPred8=pd.read_csv('vw8.csv')
#locPred8=locPred8[69:len(locPred8)-1]
#locPred9=pd.read_csv('vw9.csv')
#locPred9=locPred9[48:]
#locPred10=pd.read_csv('vw10.csv')
#locPred10=locPred10[17:len(locPred10)-1]
#locPred11=pd.read_csv('vw11.csv')
#locPred11=locPred11[15:]
#locPred12=pd.read_csv('vw12.csv')
#locPred13=pd.read_csv('vw13.csv')
#locPred14=np.array(pd.read_csv('vw14.csv'))
#locPred14a=locPred14[:3140]
#locPred14b=locPred14[3140:3140+19600]
#locPred14c=locPred14[3140+19600:]
#locPred15=pd.read_csv('vw15.csv')
#locPred16=np.array(pd.read_csv('vw16.csv'))
#locPred16a=locPred16[:6000]
#locPred16b=locPred16[6000:]
#locPred17=pd.read_csv('vw17.csv')
#
##locPredt1=pd.read_csv('Y1.csv')
#locPred2=pd.read_csv('V-vta1.csv')
#locPred2=np.array(locPred2)
##locPred2=locPred2[:1291*20]
#locPred2=locPred2[1291*20:]
#locPred2=locPred2[1321*20:]
##locPredt3=pd.read_csv('StratisJan2.csv')
##locPredt4=pd.read_csv('Vasile_fa01.csv')
##locPredt5=pd.read_csv('Vasile_fa02.csv')
##locPredt6=pd.read_csv('vw14.csv')
##locPrednull=pd.read_csv('tran.csv')
#locPred2=pd.read_csv('Vasile_fa01.csv')
#locPred2=pd.read_csv('Vasile_fb02.csv')
#locPred2=pd.read_csv('Vasile_fa02.csv')
#locPred2=pd.read_csv('Vasile_fb02.csv')

#locPred1=pd.read_csv('V-vta1.csv')
#locPred2=pd.read_csv('V-vta2.csv')
#locPred3=pd.read_csv('V-vta3.csv')
#locPred4=pd.read_csv('V-vta4.csv')
#locPred5=pd.read_csv('V-vta5.csv')
#locPred6=pd.read_csv('V-vta6.csv')
#locPred7=pd.read_csv('V-vta7.csv')
#locPred8=pd.read_csv('V-vta8.csv')
#locPred9=pd.read_csv('V-vta9.csv')
#locPred10=pd.read_csv('V-vta10.csv')
#locPred11=pd.read_csv('V-vta11.csv')
#locPred12=pd.read_csv('V-vta12.csv')
#locPred13=pd.read_csv('V-vta13.csv')
#locPred14=pd.read_csv('V-vta14.csv')
#locPred15=pd.read_csv('V-vta15.csv')
#locPred16=pd.read_csv('V-vta16.csv')
#locPred17=pd.read_csv('V-vta17.csv')
#locPred18=pd.read_csv('V-vta18.csv')
#locPred19=pd.read_csv('V-vta19.csv')
#locPred20=pd.read_csv('V-vta20.csv')
#locPred21=pd.read_csv('V-vta21.csv')
#locPred22=pd.read_csv('V-vta22.csv')
#locPred23=pd.read_csv('V-vta23.csv')
#locPred24=pd.read_csv('V-vta24.csv')
#locPred25=pd.read_csv('V-vta25.csv')
#locPred26=pd.read_csv('V-vta26.csv')
#locPred27=pd.read_csv('V-vta27.csv')
#locPred28=pd.read_csv('V-vta28.csv')
#locPred29=pd.read_csv('V-vta29.csv')
#locPred30=pd.read_csv('V-vta30.csv')

# Vf data set

locPred1=pd.read_csv('Vasile_fa01.csv') #good
locPred1=locPred1[49:len(locPred1)-1]
locPred2=pd.read_csv('Vasile_fa02.csv') #good
locPred2=locPred2[235:len(locPred2)-1]
locPred3=pd.read_csv('FB01_.csv')
locPred3a=locPred3[:17000]
locPred3b=locPred3[17000:20880]
locPred3c=locPred3[20880:27200]
locPred3d=locPred3[27200:]
locPred4=pd.read_csv('Vasile_fb02.csv')

#
#locPred1=pd.read_csv('S1.csv')
#locPred1=locPred1[43:len(locPred1)-1]
#locPred2=pd.read_csv('S2.csv')
#locPred2=locPred2[:len(locPred2)-24]
#locPred3=pd.read_csv('S3.csv')
#locPred3a=locPred3[:24660]
#locPred3a=locPred3a[38:len(locPred3a)-1]
#locPred3b=locPred3[24660:24660+6840]
#locPred3b=locPred3b[26:len(locPred3b)-1]
#locPred3c=locPred3[24660+6840:24660+6840+37220]
#locPred3c=locPred3c[36:len(locPred3c)-1]
#locPred4=pd.read_csv('S4.csv')
#locPred4=locPred4[6:len(locPred4)-3218]
#locPredM=pd.read_csv('M.csv')
#locPredM=locPredM[20:len(locPredM)-1]
#
#locPredY1_a=pd.read_csv('Y1_a.csv')
#locPredY1_b=pd.read_csv('Y1_b.csv')
#locPredY1_c=pd.read_csv('Y1_c.csv')
#locPredY1=np.concatenate((np.array(locPredY1_a), np.array(locPredY1_b), np.array(locPredY1_c)),axis=0)
#locPredY1=locPredY1[55:len(locPredY1)-1]




# tb data starting from below
#locPred1=pd.read_csv('V-vtb1.csv') # no code added
#locPred2=pd.read_csv('V-vtb2.csv') # no code added
#locPred3=pd.read_csv('V-vtb3.csv')
#locPred3=locPred3[48:len(locPred3)-1]
#locPred4=pd.read_csv('V-vtb4.csv')
#locPred4=locPred4[68:len(locPred4)-1]
#locPred5=pd.read_csv('V-vtb5.csv')
#locPred5=locPred5[221:len(locPred5)-1]
#locPred6=pd.read_csv('V-vtb6.csv')
#locPred6=locPred6[9:len(locPred6)-1]
#locPred7=pd.read_csv('V-vtb7.csv') # no code added, points aligning
#locPred8=pd.read_csv('V-vtb8.csv')
#locPred8=locPred8[30:len(locPred8)-1]
#locPred9=pd.read_csv('V-vtb9.csv')
#locPred9=locPred9[4:len(locPred9)-1]
#locPred10=pd.read_csv('V-vtb10.csv') # no code added, set probably to be deleted (Phone data set unavailable - Uche said so)
#locPred11=pd.read_csv('V-vtb11.csv')
#locPred11=locPred11[71:len(locPred11)-1]
#locPred12=pd.read_csv('V-vtb12.csv')
#locPred12=locPred12[42:len(locPred12)-1]
#locPred13=pd.read_csv('V-vtb13.csv') # no code added, Phone data set unavailable - Uche said so)
# tb data finishing here

#locPred14=pd.read_csv('V-vta14.csv')
#locPred15=pd.read_csv('V-vta15.csv')
#locPred16=pd.read_csv('V-vta16.csv')
#locPred17=pd.read_csv('V-vta17.csv')
#locPred18=pd.read_csv('V-vta18.csv')
#locPred19=pd.read_csv('V-vta19.csv')
#locPred20=pd.read_csv('V-vta20.csv')
#locPred21=pd.read_csv('V-vta21.csv')
#locPred22=pd.read_csv('V-vta22.csv')
#locPred23=pd.read_csv('V-vta23.csv')
#locPred24=pd.read_csv('V-vta24.csv')
#locPred25=pd.read_csv('V-vta25.csv')
#locPred26=pd.read_csv('V-vta26.csv')
#locPred27=pd.read_csv('V-vta27.csv')
#locPred28=pd.read_csv('V-vta28.csv')
#locPred29=pd.read_csv('V-vta29.csv')
#locPred30=pd.read_csv('V-vta30.csv')
#locPrednull=pd.read_csv('tran.csv')
##locPredd=[locPred1, locPred2, locPred3, locPred4, locPred5, locPred6, locPred7, locPred8, locPred9, locPred10, locPred11, locPred12, locPred13, locPred14, locPred15, locPred16, locPred17, locPred18, locPred19, locPred20, locPred21, locPred22, locPred31, locPred32, locPred33, locPred34, locPred35, locPred36, locPred37, locPred38, locPred39, locPred40, locPred41, locPred42, locPred43, locPred44, locPred45, locPred46, locPred47, locPred48, locPredt1, locPredt2, locPredt3, locPredt4, locPredt5, locPredt6, locPrednull]
#
locPredd=[locPred1, locPred2, locPred3a, locPred3b, locPred3c, locPred3d]#locPred4#, locPred6, locPred7, locPred8, locPred9, locPred10, locPred11, locPred12, locPred13]#, locPred14, locPred15, locPred16,  locPred17, locPred19, locPred20, locPred21, locPred22, locPred23, locPred24, locPred25, locPred26, locPred27, locPred28, locPred29, locPred30]#, locPrednull]
#

#locPredd=[locPred1, locPred2, locPred3, locPred4, locPred5, locPred6, locPred7, locPred8, locPred9, locPred10, locPred11, locPred12, locPred13, locPred14a, locPred14b, locPred14c, locPred15, locPred16a, locPred16b, locPred17]#, locPred14, locPred15, locPred16, locPred17, locPred18, locPred19, locPred20, locPred21, locPred22, locPred23, locPred24, locPred25, locPred26, locPred27, locPred28, locPred29, locPred30, locPrednull]
#locPredd=[locPred1, locPred2, locPred3, locPred4, locPrednull]# locPred5, locPred6, locPred7, locPred8, locPred9, locPred10, locPred11, locPred12, locPred13, locPrednull]

for gab in range(0,6):
    def sample_freq(data,sf):
        k=[]
        for i in range(0,len(data),sf):
            s=data[i]
            k.append(s)
        return np.array(k)
   
    def longToMetric(long):#,long):
        long=(long/60)*(-1)
        k=long
        k=np.array(k)
        k=np.reshape(k,(len(k),1))
        return k
   
    def latToMetric(lat):
        lat=lat/60
        k=lat
        k=np.array(k)
        k=np.reshape(k,(len(k),1))
        return k
    locPred=np.array(locPredd[gab])
    sf=1
   
    k=np.array(['Name', 'Latitude','Longitude'])
    k=np.reshape(k,(1,len(k)))
   
    dist1=locPred[:,2:3]
    dist2=locPred[:,3:4]
    dist1=latToMetric(dist1)
    dist2=longToMetric(dist2)
#    dist=absolute_disp(dist1, dist2)
    dist1=sample_freq(dist1,sf)
    dist2=sample_freq(dist2,sf)
    Name=np.array(range(1, len(dist1)+1))
    Name=np.reshape(Name,(len(Name),1))
    dist=np.concatenate((Name,dist1,dist2),axis=1)
    dist=np.concatenate((k,dist),axis=0)
    dist_start=dist#[:2500]
    dist_end=dist#[len(dist)-2500:]
 #   gab=float(gab)
    np.savetxt('d_t1_start' + str(gab+1)+'.csv', dist_start, delimiter=',', fmt='%s')
    np.savetxt('d_t1_end' + str(gab+1)+'.csv', dist_end, delimiter=',', fmt='%s')

#    

#for gab in range(31,49):
#    jab=23+(gab-31)
#    def sample_freq(data,sf):
#        k=[]
#        for i in range(0,len(data),sf):
#            s=data[i]
#            k.append(s)
#        return np.array(k)
#    
#    def longToMetric(long):#,long):
#        long=(long/60)*(-1)
#        k=long
#        k=np.array(k)
#        k=np.reshape(k,(len(k),1))
#        return k
#    
#    def latToMetric(lat):
#        lat=lat/60
#        k=lat
#        k=np.array(k)
#        k=np.reshape(k,(len(k),1))
#        return k
#    locPred1=np.array(locPredd[jab])
#    sf=20
#    
#    k=np.array(['Name', 'Latitude','Longitude'])
#    k=np.reshape(k,(1,len(k)))
#    
#    dist1=locPred1[:,2:3]
#    dist2=locPred1[:,3:4]
#    dist1=latToMetric(dist1)
#    dist2=longToMetric(dist2)
#    dist1=sample_freq(dist1,sf)
#    dist2=sample_freq(dist2,sf)
#    Name=np.array(range(1, len(dist1)+1))
#    Name=np.reshape(Name,(len(Name),1))
#    dist=np.concatenate((Name,dist1,dist2),axis=1)
#    dist=np.concatenate((k,dist),axis=0)
##    gab=int(gab)
#    np.savetxt('gv' + str(gab)+'.csv', dist, delimiter=',', fmt='%s')











#
#from math import cos, asin, sqrt
#def distance(lat1, lon1, lat2, lon2):#https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
#    p = 0.017453292519943295     #Pi/180
#    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
#    return 12742 * asin(sqrt(a)) #2*R*asin...
#def sample_freq(data,sf):
#    k=[]
#    for i in range(0,len(data),sf):
#        s=data[i]
#        k.append(s)
#    return np.array(k)
#
#def longToMetric(long):#,long):
#    long=(long/60)*(-1)
#    k=long
#    k=np.array(k)
#    k=np.reshape(k,(len(k),1))
#    return k
#
#def latToMetric(lat):
#    lat=lat/60
#    k=lat
#    k=np.array(k)
#    k=np.reshape(k,(len(k),1))
#    return k
#def absolute_disp(lat, long):# Haversine formula
#    long=(long/60)*(-1)
#    lat=lat/60
#    k=[]
#    for i in range(1, len(lat)):
#        lat1=lat[i-1]
#        lat2=lat[i]
#        lon1=long[i-1]
#        lon2=long[i]
#        kk=distance(lat1, lon1, lat2, lon2)
#        k.append(kk)
#    return np.reshape(k,(len(k),1))
#from vincenty import vincenty
#def absolute_disp1(lat, long):
#    long=(long/60)*(-1)
#    lat=lat/60
#    k=[]
#    for i in range(1, len(lat)):
#        lat1=lat[i-1]
#        lat2=lat[i]
#        lon1=long[i-1]
#        lon2=long[i]
#        kk=vincenty((lat1,lon1), (lat2,lon2))
##        kk=kk*1.60934
#        k.append(kk)
#    return np.reshape(k,(len(k),1))
#locPred=np.array(locPred2)
#sf=20
#
#k=np.array(['Name', 'Latitude','Longitude'])
#k=np.reshape(k,(1,len(k)))
#
#dist1=locPred[:,2:3]
#dist2=locPred[:,3:4]
##dist1=latToMetric(dist1)
##dist2=longToMetric(dist2)
#dist=absolute_disp(dist1, dist2)
#dist_=absolute_disp1(dist1, dist2)
#print(sum(dist))
#print(sum(dist_))
#print(len(locPred)+1)