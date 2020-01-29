class Queue:
    def __init__(self):
        self.q = []
    def enqueue(self,ele):
        self.q.append(ele)
    def dequeue(self):
        return self.q.pop(0)
    def isEmpty(self):
        return len(self.q) == 0 

class FCFS:
    def __init__(self,process,at,bt):
        self.process = process
        self.at = at
        self.bt = bt
        self.tat = list()
        self.wt = list()
        self.q = Queue()
        self.t = 0
    def calc(self):
        p = self.process
        for i in range(len(self.process)):
            if self.at[i] == 0:
                self.q.enqueue(self.process[i])
        while (not self.q.isEmpty()) or (not len(p)==0):
            if not self.q.isEmpty():
                x = self.q.dequeue()
            else:
                x = p.pop(0)
            self.t += self.bt[x-1]
            self.tat.append(x-self.at[x-1])
            self.wt.append(x-self.at[x-1]-self.bt[x-1])
            for i in range(len(self.process)):
                if self.at[i] < self.t:
                    self.q.enqueue(self.process[i])
            p.pop(x-1)
    def display(self):
        for i in range(len(self.process)):
            print("PROCESS\tAT\tBT\tTAT\tWT")
            print(f"{self.process[i]}\t{self.at[i]}\t{self.bt[i]}\t{self.tat[i]}\t{self.wt[i]}")
p1 = []
a = []
b = []
def accept():
    n = int(input("Enter number of process:"))
    for i in range(n):
        p1.append(i+1)
        a.append(int(input(f"Enter arrival time of {i+1}:")))   
        b.append(int(input(f"Enter burst time of {i+1}:")))              
accept()
f = FCFS(p1,a,b)
f.calc()
f.display()
