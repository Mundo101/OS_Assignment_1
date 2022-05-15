import sys
#just a file reader function that stores the whole file in an array
def readFile(path):  #working
    l = []
    with open(path, 'r') as f:
        l = f.readlines()
        n_of_lines = len(l)
        for i in range(n_of_lines):
            l[i] = str(l[i]).replace('\n', '')
            l[i] = str(l[i]).split(' ')
    return l


#create process objects
def prepproc(arr):
    #new
    completion = 0
    first_turn = [0,0]
    arrvltme = 0
    pidz = 1
    values = []
    comm = 0
    for i in range(len(arr)):
        cpz = 0
        pri = 0
        wow = arr[i]
        if wow[0] == 'proc':
            cpz = wow[2]
            comm += int(cpz)
            cpz = int(cpz)
            pri = int(wow[1])
            pr = process(pri, pidz, arrvltme, cpz, comm,completion, first_turn)
            pidz += 1
            values.append(pr)
        elif wow[0] == 'idle':
            arrvltme += int(wow[1])
        else:
            break
    return values

#counts how many arrival time levels in the proc lst
def countlvls(proclst):
  lvls_with_no_of_procs = []
  ctr = 0
  for i in range(len(proclst)):
    if i < len(proclst) - 1:
      current = proclst[i].getarrivaltime()
      next = proclst[i+1].getarrivaltime()
      
      if current == next:
        ctr = ctr +1
      else:
        lvls_with_no_of_procs.append(ctr)
        ctr = ctr + 1
    else:
      lvls_with_no_of_procs.append(ctr)
  #print(lvls_with_no_of_procs)   
  return lvls_with_no_of_procs
#bubble sort edited with Fifo case
def bubbleSort(arr):
  n = len(arr)
  for i in range(n-1):
    for j in range(0, n-i-1):
      if arr[j].getpriority() > arr[j + 1].getpriority():
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
      elif arr[j].getpriority() == arr[j + 1].getpriority():
        if arr[j].getpid() > arr[j + 1].getpid():
          arr[j], arr[j + 1] = arr[j + 1], arr[j]
def insertionSort(arr):
  for i in range(1,len(arr)):
    j = i-1
    while j >=0:
      if arr[i].getarrivaltime() <= arr[j].getcommcpu():
        if arr[i].getarrivaltime() < arr[j].commcpu:
          if arr[i].getpriority() < arr[j+1].getpriority():
            arr[i],arr[j+1] = arr[j+1],arr[i]
          elif arr[i].getpriority() == arr[j+1].getpriority():
            if arr[i].getpid() < arr[j].getpid():
              arr[i],arr[j+1] = arr[j+1],arr[i]
        else:  
          if arr[i].getpriority() < arr[j].getpriority():
            arr[i],arr[j] = arr[j],arr[i]
          elif arr[i].getpriority() == arr[j].getpriority():
            if arr[i].getpid() < arr[j].getpid():
              arr[i],arr[j] = arr[j],arr[i]
      j -= 1
RQ = []
def check_for_arrival(lst, time):
  global RQ
  for i in range(len(lst)):
    if(lst[i].getarrivaltime() == time):
      RQ.append(lst[i])
def RR(proclst, quantum):
  time = 0
  check_for_arrival(proclst, time)
  print('• CPU timeline:')
  while(len(RQ)!=0):
    cpy = RQ.pop(0)
    if(cpy.first_turn[0] == 0):
        cpy.first_turn[0] = 1
        cpy.first_turn[1] = time
        proclst[cpy.getpid() - 1].first_turn[1] = time
    if(cpy.cpubursts < quantum):
      x = time
      for i in range(cpy.cpubursts):
        time += 1
        check_for_arrival(proclst, time)
        cpy.cpubursts -= 1
      proclst[cpy.getpid() - 1].completion = time
      print('Process: ' + str(cpy.pid) + ' (' + str(x) + ' -> ' + str(time)+')')
    else:
      x = time
      for i in range(quantum):
        time+=1
        check_for_arrival(proclst, time)
        cpy.cpubursts -= 1
      if(cpy.cpubursts != 0):
        RQ.append(cpy)
      else:
        proclst[cpy.getpid() - 1].completion = time
      print('Process: ' + str(cpy.pid) + ' (' + str(x) + ' -> ' + str(time)+')')
  print("")
  turnaroundsum = 0
  resptimesum = 0
  for i in range(len(proclst)):
    turnaroundsum += (proclst[i].completion - proclst[i].arrivaltime)
    resptimesum += (proclst[i].first_turn[1] - proclst[i].arrivaltime)
  print("• Avg. Turnaround time : ", turnaroundsum/len(proclst),'\n')
  print("• Avg. Response time in R queue : ", resptimesum/len(proclst),'\n')
    
#Priority Queue
def Pr(proclst):
  sortedlst = []
  lvls = countlvls(proclst)
  temparr = []
  for i in range(len(lvls)):
    if i == 0:
      temparr = proclst[0:lvls[i]+1]
    else:
      temparr = proclst[lvls[i-1]+1:lvls[i]+1]
    bubbleSort(temparr)
    for x in range(len(temparr)):
      sortedlst.append(temparr[x])
  insertionSort(sortedlst)
  # for j in range(len(sortedlst)):
  #   sortedlst[j].printmyinfo()
  first_turn = 0
  completion = 0
  turnaroundsum = 0
  resptimesum = 0
  for i in range(len(sortedlst)):
    if i == 0:
      completion += sortedlst[i].getcpubursts()
    else:
      first_turn += sortedlst[i-1].getcpubursts()
      completion += sortedlst[i].getcpubursts()
    tt1 = (completion - sortedlst[i].getarrivaltime())
    tt2 = (first_turn - sortedlst[i].getarrivaltime())
    resptimesum += tt2
    turnaroundsum += tt1
    print('process: ' + str(sortedlst[i].pid) + ' (' + str(first_turn) +' -> ' + str(completion)+')')
  print('')
  turnarounavg = turnaroundsum/(len(sortedlst))
  respavg = resptimesum/(len(sortedlst))
  print("• Avg. Turnaround time : ",turnarounavg,'\n')
  print("• Avg. Response time in R queue : ",respavg,'\n')
  

#an object for the process
class process:
    def __init__(self, priority, pid, arrivaltime, cpubursts,commcpu,completion, first_turn = [0,0]):
        self.priority = priority
        self.pid = pid
        self.arrivaltime = arrivaltime
        self.cpubursts = cpubursts
        self.commcpu = commcpu
        self.completion = 0
        self.first_turn = [0,0]

    #prints info

    def printmyinfo(self):
        print("My PID: ", self.pid)
        print("My Priority: ", self.priority)
        print("My arrival time: ", self.arrivaltime)
        print("My cpu burst: ", self.cpubursts)
        print("My commulative cpu:",self.commcpu)

    #getters
    def getpriority(self):
        return self.priority
    
    def getfirst_turn(self):
        return self.first_turn[1]
      
    def getcompletion(self):
        return self.completion
      
    def getpid(self):
        return self.pid

    def getarrivaltime(self):
        return self.arrivaltime

    def getcpubursts(self):
        return self.cpubursts

    def getcommcpu(self):
        return self.commcpu
    #setters
    def setpriority(self, pr):
        self.priority = pr

    def setfirst_turn(self, first_turn):
        #flag
        self.first_turn[0] = first_turn[0]
        #value
        self.first_turn[1] = first_turn[1]
        
      
    def setcompletion(self, completion):
        self.completion = completion
    
    def setpid(self, p):
        self.pid = p

    def setarrivaltime(self, arr):
        self.arrivaltime = arr

    def setcpubursts(self, bb):
        self.cpubursts = bb


#main.py inputfile algorithm quantum
if __name__ == "__main__":
  x = readFile(sys.argv[1])
  print('\n• Input File Name: ', sys.argv[1],'\n')
  pres = prepproc(x)
  if(sys.argv[2] == 'Pr'):
    print('• CPU Scheduling Alg: ', 'Pr\n')
    Pr(pres)
  elif(sys.argv[2] == 'RR'):
    print('• CPU Scheduling Alg: ', 'RR'+'('+(sys.argv[3])+')\n')
    RR(pres, int(sys.argv[3]))
  else:
    print('Invalid input try again')
