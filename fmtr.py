#!/usr/bin/env python3
import csv
diagnosisKey = "diagnosis"
radiusMeanKey = "radius_mean"
textureMeanKey = "texture_mean"
perimeterMeanKey = "perimeter_mean"
areaMeanKey = "area_mean"
smoothnessMeanKey = "smoothness_mean"
compactnessMeanKey = "compactness_mean"
concavityMeanKey = "concavity_mean"
concavePointsMeanKey = "concave points_mean"
symmetryMeanKey = "symmetry_mean"
fractalDimensionMean = "fractal_dimension_mean"
radiusSeKey = "radius_se"
textureSeKey = "texture_se"
perimeterSeKey = "perimeter_se"
areaSeKey = "area_se"
smoothnessSeKey = "smoothness_se"
compactnessSeKey = "compactness_se"
concavitySeKey = "concavity_se"
concavePointsSeKey = "concave points_se"
symmetrySeKey = "symmetry_se"
fractalDimensionSeKey = "fractal_dimension_se"
radiusWorstKey = "radius_worst"
textureWorstKey = "texture_worst"
perimeterWorstKey = "perimeter_worst"
areaWorstKey = "area_worst"
smoothnessWorstKey = "smoothness_worst"
compactnessWorstKey = "compactness_worst"
concavityWorstKey = "concavity_worst"
concavePointsWorstKey = "concave points_worst"
symmetryWorstKey = "symmetry_worst"
fractalDimensionWorstKey = "fractal_dimension_worst"

headers = [diagnosisKey, radiusMeanKey, textureMeanKey, perimeterMeanKey, areaMeanKey, 
smoothnessMeanKey, compactnessMeanKey, concavityMeanKey, concavePointsMeanKey, symmetryMeanKey, 
fractalDimensionMean, radiusSeKey, textureSeKey, perimeterSeKey, areaSeKey, smoothnessSeKey, 
compactnessSeKey, concavitySeKey, concavePointsSeKey, symmetrySeKey, fractalDimensionSeKey, 
radiusWorstKey, textureWorstKey, perimeterWorstKey, areaWorstKey, smoothnessWorstKey, 
compactnessWorstKey, concavityWorstKey, concavePointsWorstKey, symmetryWorstKey, 
fractalDimensionWorstKey]

header = [0, 0, "Malignant", "Benign"]

def fmt(filename, col, features):
	with open(filename, 'r') as source:
		rdr = csv.reader(source)
		header[0] = sum(1 for row in rdr)
		header[1] = features
		source.seek(0)
		with open(filename + '.fmtd', 'w') as result:
			wtr = csv.writer(result)
			wtr.writerow(header)
			for row in rdr:
				del row[col]
				row[0] = 0 if row[0] == "B" else 1
				wtr.writerow(row)

def ffp(filename, col):
	with open(filename, 'r') as source:
		rdr = csv.reader(source)
		with open(filename + '.pltd', 'w') as result:
			wtr = csv.writer(result)
			for row in rdr:
				del row[col]
				wtr.writerow(row)