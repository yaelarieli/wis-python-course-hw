import numpy as np

def FindCore(mtrx, mask, prct):
    Coremtrx = np.zeros_like(mtrx, dtype=bool)
    mtrx = np.where(mask,mtrx,np.nan) # replace the values in mtrx with nan where mask is True

    TH = np.empty(mtrx.shape[-1]) 

    for i in range(0,mtrx.shape[-1]):  #loop over z levels
        tmp = mtrx[:, i].copy() #copy the column
        Ntmp = np.sum(~np.isnan(tmp)) #find how many non nan values in the tmp

        if Ntmp == 0:
            continue
        elif Ntmp > 10:
            TH[i] = np.nanpercentile(tmp, prct, interpolation='nearest')
        else:
            tmpmin = np.nanmin(tmp)
            TH[i] = tmpmin

        tmp = tmp >= TH[i] #compare the values in tmp to the threshold
        Coremtrx[:,i] = tmp #assign the result to Coremtrx

    return Coremtrx
