"""
Project for wiz Python course

Calculating adiabatic fraction (AF) in a cloud.

@author: yael.arieli@weizmann.ac.il
"""

import sys
import numpy as np
import argparse
from func_for_project import CalcCldMtrx, FindCore,calcAF
import xarray as xr
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='file name')
    args = parser.parse_args()
    filename = args.filename

    try:
        ds = xr.open_dataset(filename)
    except FileNotFoundError:
        sys.exit(f"Error: File '{filename}' not found.")
    except Exception as e:
        sys.exit(f"Error opening file '{filename}': {e}")

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
    AF = calcAF(CldMtrx, w, Qv, Qc, T, prs, RH, z)
    # Create a the figure
    plt.figure(figsize=(20, 10))
    plt.imshow(AF, cmap='hot', interpolation='nearest', origin='lower')
    plt.colorbar()
    plt.title('Adiabatic Fraction')
    plt.xlabel('x')
    plt.ylabel('z')
    x_index = np.arange(AF.shape[1]) * 10
    y_index = np.arange(AF.shape[0]) * 10
    plt.xticks(ticks=np.arange(0, AF.shape[1], 50), labels=x_index[::50])
    plt.yticks(ticks=np.arange(0, AF.shape[0], 50), labels=y_index[::50])
    plt.show()


main()



