a=int(input())
if a%4==0 and a%100 !=0:
  print("LEAP")
elif a%400==0:
  print("LEAP")
else:
  print("COMMON")
