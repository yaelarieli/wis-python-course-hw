import numpy as np
import matplotlib.pyplot as plt
import warnings

# function that calculates the cloud matrix by given Qp and Qn CldMtrx = Qp+Qn>0.01 , CldMtrx is a boolean matrix 
def CalcCldMtrx(Qp,Qn):
    CldMtrx = Qp + Qn > 0.01
    return CldMtrx


def FindCore(mtrx, mask, prct):
    Coremtrx = np.zeros_like(mtrx, dtype=bool)
    mtrx = np.where(mask,mtrx,np.nan) # replace the values in mtrx with nan where mask is True

    TH = np.empty(mtrx.shape[0]) 

    for i in range(0,mtrx.shape[0]):  #loop over z levels
        tmp = mtrx[i, :].copy() #copy the column
        Ntmp = np.sum(~np.isnan(tmp)) #find how many non nan values in the tmp
        if Ntmp == 0:
            continue
        elif Ntmp > 10:
            TH[i] = np.nanpercentile(tmp, prct, interpolation='nearest')
        else:
            tmpmin = np.nanmin(tmp)
            TH[i] = tmpmin
            # print('b')
            # print(i)

        tmp = tmp >= TH[i] #compare the values in tmp to the threshold
        Coremtrx[i,:] = tmp #assign the result to Coremtrx
    return Coremtrx


def calcAF( CldMtrx, COREvar, Qv, Qc, T, prs, RH, z):
    g = 9.8  # gravity (m/s)
    Rd = 287  # Gas constant for dry air
    Rvv = 461  # Gas constant for water vapor
    cp = 1000  # heat capacity J/kg/K
    L = 2.5e6  # Latent heat J/kg

    sz = Qc.shape

    C = np.full(sz[0], np.nan)

    # cloud base height
    Zb = 60 

    Coreth = 95
    coreprf = FindCore(COREvar, CldMtrx, Coreth)  # which core to consider for the adiabatic profile

    RHOd = prs / (Rd * T)
    rhov = (1e-3) * Qv * RHOd
    LWC = (1e-3) * Qc * RHOd  # kg/m^3

    A1 = g / T * ((L / (cp * Rvv * T)) - 1 / Rd)
    A2 = 1 / rhov + (L ** 2) / (Rvv * cp * (T ** 2) * RHOd)

    warnings.filterwarnings("ignore", category=RuntimeWarning, message="Mean of empty slice")
    tmp = A1.copy()
    tmp = np.where(coreprf,tmp,np.nan)
    A1z = np.nanmean(tmp, axis=1)

    tmp = A2.copy()
    tmp = np.where(coreprf,tmp,np.nan)
    A2z = np.nanmean(tmp, axis=1)
    

    dLWCdz = A1z / A2z
    Score = np.full(dLWCdz.shape, np.nan)

    tmp = A1[0:Zb-1,:]
    A1z[0:Zb-1] = np.nanmean(tmp, axis=1)


    tmp = A2[0:Zb-1,:]
    A2z[0:Zb-1] = np.nanmean(tmp, axis=1)
    dLWCdz[0:Zb - 1] = A1z[0:Zb - 1] / A2z[0:Zb - 1]

    
    LWC0=0

    for i in range(Zb + 1, len(z)):
        C[i] = np.trapz(dLWCdz[Zb:i], z[Zb:i])

    C = LWC0 + C
    # plt.plot(C,z)
    # plt.show()
    S = (RH - 100)/100
   
    tmp = (COREvar > 0.9) & (CldMtrx==1)
    S = np.where(tmp,S,np.nan) #replace the values in S that are not in the core with nan
    Score = np.nanmean(S,1)

    C1 = np.full(z.shape, np.nan)

    deltaS = np.diff(Score+1)/np.diff(z)
    for i in range (Zb,z.shape[0]):
        C1[i] = np.trapz(-deltaS[Zb:i]/A2z[Zb:i], z[Zb:i])
        
    LWCa = C + C1 
    

    LWCa[LWCa<0] = np.nan #replace the values in LWCa that are less than 0 with nan
 
    # reshpe the LWC to be in the shape of Qp    
    LWCa = np.tile(LWCa[:,np.newaxis],(1,Qv.shape[1]))
    AF = LWC / LWCa
    AF = np.where(AF<1,AF,1) #replace the values in AF that are more than 1 with 1
    AF = np.where(CldMtrx,AF,np.nan) #replace the values in AF that are not in the cloud with nan

    
    

    return AF
    









