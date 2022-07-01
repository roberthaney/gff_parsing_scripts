import sys

features = {}

complete = True
# open and read gff file 
with open(sys.argv[1]) as fhand:
	for line in fhand:
		# skip comment lines
		if line.startswith("#"):
			continue
		# split columns 
		temp = line.split()
		# check that line contains at least 9 columns, as specified in gff definition
		if len(temp) < 9:
			print "\nCheck file format: gff file should have at least nine columns\n"
			complete = False
			break
		# add to dict or increment
		if temp[2] not in features:
			features[temp[2]] = 1
		else:
			features[temp[2]] += 1

if complete:
	print 		
	print "Features present in file", sys.argv[1], "and number of entries:"
	for feature in sorted(features):
		print feature + ": " + "\t" + str(features[feature])
