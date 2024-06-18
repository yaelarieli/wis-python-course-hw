import pytest
import xarray as xr
import numpy as np
from func_for_project import calcAF, CalcCldMtrx , FindCore, calcAF


def test_calcAF():
    # Load the data of the test file. This data is of adiabatic field.
    filename = "data_for_AFcalc_test.nc"
    ds = xr.open_dataset(filename)
    Qp = ds.Qp
    Qn = ds.Qn
    CldMtrx = CalcCldMtrx(Qp,Qn)
    Qv = ds.Qv
    RH = ds.RH
    T = ds.T
    prs = ds.prs
    w = ds.w
    z = ds.z
    Qc = Qn+Qp

    # calculate the adiabatic fraction
    AF = calcAF(CldMtrx, w, Qv, Qc, T, prs, RH, z,Zb=60,Coreth=95)
    # Check if all values in the matrix are 1
    assert np.all(AF == 1), "Not all values in the matrix are 1"




