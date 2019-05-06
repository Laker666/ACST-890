import sys
m=int(sys.argv[1])
d=int(sys.argv[2])

if (m == 3) & (d >= 20):
     print("TRUE")
elif (m==6) and (d<=20):
     print("TRUE")
elif (m>3) and (m<6):
     print("TRUE")
else: 
     print ("FALSE") 
