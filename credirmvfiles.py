import os
import shutil
try:
   files = [f for f in os.listdir('.') if os.path.isfile(f)]
   for f in files:
      fileprefix=f[1:10]
      print("File Prefix:",fileprefix)
      dirname = f[1:2] + "-" + f[4:6] + "-" + f[7:9]
      print("Directory Name:" , dirname)
      os.makedirs(dirname)
      shutil.move(f,dirname+"/"+f)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
