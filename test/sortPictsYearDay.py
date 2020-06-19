import os
import shutil
try:
   files = [f for f in os.listdir('./') if os.path.isfile(f)]
   ctr   = {}
   for f in files:
      if f[:2] == '20':
         fileprefix=f[0:8]
         print("File Prefix:",fileprefix)
         diryear  = f[0:4]
         dirmonth = f[4:6]
         print("Directory year:" , diryear)
         if not os.path.exists(diryear):
            os.makedirs(diryear)
         dirday = f[:4] + "-" + f[4:6] + "-" + f[6:8]
         print("Directory Day:" , dirday)
         if not os.path.exists(diryear + "/" + dirday):
            os.makedirs(diryear + "/" + dirday)
         shutil.move(f,diryear + "/" + dirday + "/" + f)
         #ctr[diryear] = ctr.get(diryear,0) + 1
         #ctr[diryear[dirmonth]] = ctr.get(diryear(dirmonth),0) + 1
         #ctr[diryear[dirmonth[dirday]]] = ctr.get(diryear(dirmonth(dirday)),0) + 1
      ctr[f[0:4]] = ctr.get(f[0:4],0) + 1
      ctr[f[0:6]] = ctr.get(f[0:6],0) + 1
      ctr[f[0:8]] = ctr.get(f[0:8],0) + 1
   print("Picture Count by year month day",ctr)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
