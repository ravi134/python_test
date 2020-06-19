import os
import shutil
try:
   files = [f for f in os.listdir('./') if os.path.isfile(f)]
   for f in files:
      if f[:2] == '20':
         fileprefix=f[0:8]
         print("File Prefix:",fileprefix)
         dirname = f[:4] + "-" + f[4:6] + "-" + f[6:8]
         print("Directory Name:" , dirname)
         os.makedirs(dirname)
         shutil.move(f,dirname+"/"+f)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
