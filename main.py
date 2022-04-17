import sys
lst = []
def ModLines():
  with open(sys.argv[2], "r") as f:
    for line in f:
        s1 = line.strip()
        s2 = s1.split()
        lst.append(s2)
  return lst    
class PR:
  procc, totb, totid = 0, 0, 0
  temp1, temp2, temp3, temp4 = 0, 0, 0, 0
  pritemp1 = []
  pritemp2 = []
  pritemp3 = []
  proctemp = []
  nlst = []
  lst = ModLines()
  def cpuUt(self):
        j, i, k = 3, 0, 0
        for l in self.lst:
            if (self.lst[i][0] == 'proc'):
                self.procc += + 1
                self.nlst.append(self.lst[i])
            j = 3
            for z in range(len(l)):
                if (j >= int(len(l))):
                    if (self.lst[i][0] == 'idle'):
                        self.totid += int(self.lst[i][1])
                    break
                if (self.lst[i][0] == 'proc'):
                    self.totb += int(self.lst[k][j])
                    j += 1
            i += 1
            k += 1
        return (self.totb / (self.totb + self.totid))
    
  def avg_Ttime(self):
        return(self.totb/self.procc)

  def cpu_tl(self):
        i=-1
        j=1
        for line in self.lst:
            i=i+1
            if (self.lst[i][0] == 'Done'):
                break
            if (self.lst[i][0] == 'idle'):
                continue
            if (int(self.lst[i][j]) == 1):
                if (self.lst[i][0] == 'proc'):
                    self.pritemp1.append(line)
            elif (int(self.lst[i][j]) == 2):
                if (self.lst[i][0] == 'proc'):
                    self.pritemp2.append(line)
            elif (int(self.lst[i][j]) == 3):
                if (self.lst[i][0] == 'proc'):
                    self.pritemp3.append(line)
            elif (int(self.lst[i][j]) > 3):
                if (self.lst[i][0] == 'proc'):
                    self.proctemp.append(line)
                    self.proctemp.sort()
        if(len(self.pritemp1)):
            self.nlst.append(self.pritemp1)
        if(len(self.pritemp2)):
            self.nlst.append(self.pritemp2)
        if(len(self.pritemp3)):
            self.nlst.append(self.pritemp3)
        if(len(self.proctemp)):
            self.nlst.append(self.proctemp)
        return self.nlst
  def time_counter(self):
        i = 0
        self.nlst.sort()
        for line in self.nlst:
            for z in range(3, len(line)):
                if (i == 0):
                    self.temp1 = self.temp1 + int(self.nlst[i][z])
                elif (i == 1):
                    self.temp2 = self.temp2 + int(self.nlst[i][z])
                elif (i == 2):
                    self.temp3 = self.temp3 + int(self.nlst[i][z])
                elif (i == 3):
                    self.temp4 = self.temp4 + int(self.nlst[i][z])
            i = i + 1
        self.temp2 = self.temp2 + self.temp1
        self.temp3 = self.temp3 + self.temp2
        self.temp4 = self.temp4 + self.temp3
  def RQ(self):
        i = 1
        tmp = []
        tmp = self.nlst
        for line in tmp:
            if (i == 1):
                print("Waiting time = 0 , priority = ", i)
                print("Priority#", i, ":\t", line)
            elif (i == 2):
                print("Waiting time =", self.temp1, ", priority = ", i)
                print("Priority#", i, ":\t", line)
            elif (i == 3):
                print("Waiting time =", self.temp2, ", priority = ", i)
                print("Priority#", i, ":\t", line)
            elif (i == 4):
                print("Waiting time =", self.temp3, ", priority = ", i)
                print("Priority#", i, ":\t", line)
            i = i + 1
if(sys.argv[1]=='PR'):
    pr = PR()
    print("Inputfile: ", sys.argv[2])
    print("Priority Scheduling")
    print("CPU utalization: ",pr.cpuUt())
    print("Turn arond time average = " ,pr.avg_Ttime())
    pr.time_counter()
    pr.RQ()
    print("CPU Timeline:")
    TimelineTest = pr.nlst
    for line in TimelineTest:
      print(line)