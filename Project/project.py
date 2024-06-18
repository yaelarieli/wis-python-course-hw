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
    # Rotate the Qp data by 180 degrees
    # Qp = np.flip(Qp, axis=(0, 1))
    # Qn = np.flip(Qn, axis=(0, 1))
    CldMtrx = CalcCldMtrx(Qp,Qn)


    Qv = ds.Qv
    # Qv = np.flip(Qv, axis=(0, 1))
    RH = ds.RH
    # RH = np.flip(RH, axis=(0, 1))

    T = ds.T
    # T = np.flip(T, axis=(0, 1))
    prs = ds.prs
    # prs = np.flip(prs, axis=(0, 1))
    w = ds.w
    # w = np.flip(w, axis=(0, 1))
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



