
        
print("\n\nPadmaja H, regno : 2021503034")
print("Mc collugh pits OR gate")
x1=[0,0,1,1]
x2=[0,1,0,1]
y_act=[0,1,1,1]
print("Fixing values of w1=1 and w2=1")
print("Fixing the activation function as \n \
      y_est=1 if f(x)>=1  \n \
      y_est=0 if f(x)<1")
w1=1
w2=1
print("x1\tx2\ty_act\t f(x)\t y_est")
for i in range (4):
    sum=w1*x1[i]+w2*x2[i]
    if(sum>=1):
        print(x1[i],"\t",x2[i],"\t",y_act[i],"\t\t",sum,"\t\t",1)
    else :
        print(x1[i],"\t",x2[i],"\t",y_act[i],"\t\t",sum,"\t\t",0)
    
'''
print("\nPadmaja H, regno : 2021503034")
print("Mc collugh pits OR gate")
x1=[0,0,1,1]
x2=[0,1,0,1]
y_act=[0,1,1,1]
print("Fixing values of w1=1 and w2=1")
print("Fixing the activation function as \n \
      y_est=1 if f(x)>=1  \n \
      y_est=0 if f(x)<1")
w1=1
w2=1
print("x1\tx2\ty_act\t f(x)\t y_est")
for i in range (4):
    sum=w1*x1[i]+w2*x2[i]
    print(x1[i],"\t",x2[i],"\t",y_act[i], end="")
    if(sum>=1):
       print("\t\t",sum,"\t\t",1)
    else :
        print("\t\t",sum,"\t\t",0)
  '''
