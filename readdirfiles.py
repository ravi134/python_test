import glob

txtfiles = []
for file in glob.glob("*"):
   txtfiles.append(file)
   print(file)

