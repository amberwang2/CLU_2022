import numpy as np
import os, sys, math, pdb, glob, time, fnmatch, datetime
from astropy.table import Table, vstack, hstack, Column, unique, join

def stop(): pdb.set_trace()

cat=Table.read('CatVisClass_AmberW_20220719.fits')
