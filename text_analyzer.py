def vocalWord(text):
      length = 0
      textSplit = text.split()
      textJoin = "".join(textSplit)
      
      a = []
      i = []
      u = []
      e = []
      o = []
      
      while length < len(textJoin):
            if textJoin[length] == "a" or textJoin[length] == "A":
                  a.append(textJoin[length])
            elif textJoin[length] == "i" or textJoin[length] == "I":
                  i.append(textJoin[length])
            elif textJoin[length] == "u" or textJoin[length] == "U":
                  u.append(textJoin[length])
            elif textJoin[length] == "e" or textJoin[length] == "E":
                  e.append(textJoin [length])
            elif textJoin[length] == "o" or textJoin[length] == "O":
                  o.append(textJoin[length])
            else:
                  pass
            length += 1
      sumA = len(a)
      sumI = len(i)
      sumU = len(u)
      sumE = len(e)
      sumO = len(o)
      totalVocal = sumA + sumI + sumU + sumE + sumO
      
      vocalRil = {"a": sumA, "i": sumI, "u": sumU, "e": sumE, "o": sumO, "total": totalVocal}
      
      return vocalRil

def analyze(text):
      splitted = text.split()
      joined = "".join(splitted)
      
      for tWord in range(len(splitted)):
            x = tWord +1
            
      print("\n"),
      print(f"1.Total character : {len(text)}")
      print(f"2.Total character without space : {len(joined)}")
      print(f"3.Total Word : {x}")
      print(f"4.Total Vocal : {vocalWord(text)["total"]}")
      print(f"  Total a/A : {vocalWord(text)["a"]}")
      print(f"  Total i/I : {vocalWord(text)["i"]}")
      print(f"  Total u/U : {vocalWord(text)["u"]}")
      print(f"  Total e/E : {vocalWord(text)["e"]}")
      print(f"  Total o/O : {vocalWord(text)["o"]}")
      print("\n")

def main():
      while True:
            print("Welcome to Text Analyzer")
            print("\n")
            i = input("Input any word or text to analyze or 0 to exit : ")
            if i == "0":
                  break
            elif i:
                 analyze(i)
            else:
                  print("Please input something")
                  print("\n")
                  
main()