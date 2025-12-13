class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            raise ValueError
        self.capacity=capacity
        self.size=0

    def __str__(self):
        n=self.size
        return f"{n*'🍪'}"

    def deposit(self, n):
        self.size=self.size+n
        if self.size>self.capacity:
            raise ValueError
        return self.size
    
    def withdraw(self, n):
        self.size=self.size-n
        if self.size<0:
            raise ValueError
        return self.size

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self,capacity):
        if capacity<0:
            raise ValueError
        self._capacity=capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size=0):
        self._size=size

#def main():
 # capacity=13
  #jar=Jar(capacity)
  #Jar.deposit(jar,5)
  #Jar.withdraw(jar,3)
  #print(jar)


#if __name__=="__main__":
 #   main()
