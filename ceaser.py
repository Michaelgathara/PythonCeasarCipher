inventory = ["a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "e", "s", "t", "u", "v", "w", "x", "y", "z"]
def letterEncode():
  ldecodedMessage = []
  lshiftedMessage = []
  dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
  lshift = int(input("Shift for encoding?: "))
  lamountofWords = int(input("How many words: "))
  for u in range(lamountofWords):
    letterText = input("Word: ")
    ltrText = letterText.lower()
    for c in range(len(ltrText)):
      ind = ltrText[c]
      for k,v in dict.items():
        if k == ind:
          if lshift + (int(v)-1) >= 26:
              lshift = (lshift+(int(v)-1)) - 26
          ldecodedMessage.append(inventory[int(v)+1]) 
          lshiftedMessage.append(inventory[(int(v))+(lshift-1)])
    lshiftedMessage.append(" ")
  for i in range(len(lshiftedMessage)):
    print(lshiftedMessage[i], end="")
  print(" ")

letterEncode()