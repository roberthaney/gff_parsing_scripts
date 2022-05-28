import sys

features = {}

# open and read gff file 
with open(sys.argv[1]) as fhand:
	for line in fhand:
		if line.startswith("#"):
			continue
		temp = line.split()
		if temp[2] not in features:
			features[temp[2]] = 1
		else:
			features[temp[2]] += 1


print 		
print "Features present in file", sys.argv[1], "and number of entries:"
for feature in features:
	print feature + ": " + str(features[feature])