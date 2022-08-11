x=range(100)
for a in x:
     if a%5==0 and a%6==0 and a%7==0 and a%9==0:
      print(f"{a} is divisible by all")
     elif a%5==0:
      print(f"{a} is divisible by 5")
     elif a%6==0:
      print(f"{a} is divisible by 6")
     elif a%7==0:
      print(f"{a} is divisible by 7")
     elif a%9==0:
      print(f"{a} is divisible by 9")
     else:
      print(f"{a} is not divisible by any")