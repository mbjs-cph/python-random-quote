import random
def simple():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 15
  rnd1 = random.randint(0, last)
  rnd2 = random.randint(0, last)
  #print(quotes[rnd1])
  #print(quotes[rnd2])
  print(quotes[rnd1], end = '')
  print(quotes[rnd2])
 
  
  
  

if __name__== "__main__":
  simple()


