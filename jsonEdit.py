import json

infile = open('tweet_tone_analyzer.json', 'r')
data = json.load(infile)
# print data
for datum in data:
	print datum
	#if 'score' not in datum['tones']:
	#	del datum




infile.close()


# outfile = open('tweet_tone_analyzer.json', 'w')
# json.dump(data, outfile, indent=4)
# outfile.close()

