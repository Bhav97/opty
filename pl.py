#!/usr/bin/env python3

import os
import csv
import fmtr
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

WDBC_PLOT_DATA = "./data/wdbc.train.pltd"

DIAGNOSISKEY = "diagnosis"
RADIUSMEANKEY = "radius_mean"
TEXTUREMEANKEY = "texture_mean"
PERIMETERMEANKEY = "perimeter_mean"
AREAMEANKEY = "area_mean"
SMOOTHNESSMEANKEY = "smoothness_mean"
COMPACTNESSMEANKEY = "compactness_mean"
CONCAVITYMEANKEY = "concavity_mean"
CONCAVEPOINTSMEANKEY = "concave points_mean"
SYMMETRYMEANKEY = "symmetry_mean"
FRACTALDIMENSIONMEANKEY = "fractal_dimension_mean"

HEADERS = [DIAGNOSISKEY, RADIUSMEANKEY, TEXTUREMEANKEY, PERIMETERMEANKEY, AREAMEANKEY, 
			SMOOTHNESSMEANKEY, COMPACTNESSMEANKEY, CONCAVITYMEANKEY, CONCAVEPOINTSMEANKEY, SYMMETRYMEANKEY, 
			FRACTALDIMENSIONMEANKEY]

PLOT_DATA = [HEADERS]

def get_train_data():
	return pd.read_csv(WDBC_PLOT_DATA, names= train_columns, delimiter=',', skiprows=1)


if not os.path.exists(WDBC_PLOT_DATA):
	if os.path.exists(WDBC_PLOT_DATA[:-5]):
		fmtr.ffp(WDBC_PLOT_DATA[:-5], 0)
		print("Generated formatted data successfully: {}".format(WDBC_PLOT_DATA))
	else:
		print("Missing dataset: {}".format(WDBC_PLOT_DATA[:-5]))

with open(WDBC_PLOT_DATA, 'r') as source:
	READER = csv.reader(source)
	for row in READER:
		PLOT_DATA.append(row)

# plt.scatter()
for ridx, row in enumerate(PLOT_DATA):
    sns.distplot(train_data[cn][train_data.diagnosis == "M"], bins='auto', label='Malignant')
    sns.distplot(train_data[cn][train_data.diagnosis == "B"], bins='auto', label='Benign')
	# plt.distplot(PLOT_DATA, label="")