fhand = open("Lhes_BW_rnd3.all.maker.gff")

features = {}

for line in fhand:
	if line.startswith("#"):
		continue
	temp = line.split()
	if temp[2] not in features:
		features[temp[2]] = 1
	else:
		features[temp[2]] += 1


		
print "Features present in file:"
for feature in features:
	print feature + ": " + str(features[feature])