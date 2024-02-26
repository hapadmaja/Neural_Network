# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:24:18 2024

@author: LENOVO
"""

print("Padmaja H, regno : 2021503034")
print("Hebbian model for AND gate")
x1=[0,0,1,1]
x2=[0,1,0,1]
y_act=[0,0,0,1]
xb=[1,1,1,1]
#print("Fixing values of w1=1 and w2=1")
print("Fixing the activation function as \n \
      y_est=1 if f(x)>=2  \n \
      y_est=-1 if f(x)<2")
w1=0
w2=0
wb=0
print("Making the inputs and  outputs bipolar")
for i in range(len(x1)) :
    if(x1[i]==0):
        x1[i]=-1
        
for i in range(len(x2)) :
    if(x2[i]==0):
        x2[i]=-1   
for i in range(len(y_act)) :
    if(y_act[i]==0):
        y_act[i]=-1

#print(x1) 

#print("x1\tx2\ty_act\t d(w1) \t d(w2) \t d(wb) \t W1 \t W2 \t Wb")
print("%-5s %-5s %-5s %-7s %-7s %-7s %-7s %-7s %-7s %-7s" % ("x1", "x2", "xb","y_act", "d(w1)", "d(w2)", "d(wb)", "W1", "W2", "Wb"))
sum=0
for i in range (len(x1)):
    dw1=x1[i]*y_act[i]
    dw2=x2[i]*y_act[i]
    dwb=xb[i]*y_act[i]
    w1=w1+dw1
    w2=w2+dw2
    wb=wb+dwb
    print("%-5d %-5d %-5d %-7d %-7d %-7d %-7d %-7d %-7d %-7d" % (x1[i], x2[i], xb[i], y_act[i], dw1, dw2, dwb, w1, w2, wb))

print("%-5s %-5s %-5s %-7s %-7s %-7s" % ("x1", "x2", "xb","y_act", "f(x)", "y_est"))
for j in range (4):
    sum=w1*x1[j]+w2*x2[j]
    sum=sum+wb*xb[j]
    if(sum>=2):
        print("%-5d %-5d %-5d %-7d %-7d %-7d " % (x1[j], x2[j], xb[j], y_act[j],sum,1))
    else :
       print("%-5d %-5d %-5d %-7d %-7d %-7d " % (x1[j], x2[j], xb[j], y_act[j],sum,-1))
       
       
print("\n")
print("Padmaja H, regno : 2021503034")
print("Hebbian model for OR gate")
x1=[0,0,1,1]
x2=[0,1,0,1]
y_act=[0,1,1,1]
xb=[1,1,1,1]
#print("Fixing values of w1=1 and w2=1")
print("Fixing the activation function as \n \
      y_est=1 if f(x)>=2  \n \
      y_est=-1 if f(x)<2")
w1=0
w2=0
wb=0
print("Making the inputs and  outputs bipolar")
for i in range(len(x1)) :
    if(x1[i]==0):
        x1[i]=-1
        
for i in range(len(x2)) :
    if(x2[i]==0):
        x2[i]=-1   
for i in range(len(y_act)) :
    if(y_act[i]==0):
        y_act[i]=-1

#print(x1) 

#print("x1\tx2\ty_act\t d(w1) \t d(w2) \t d(wb) \t W1 \t W2 \t Wb")
print("%-5s %-5s %-5s %-7s %-7s %-7s %-7s %-7s %-7s %-7s" % ("x1", "x2", "xb","y_act", "d(w1)", "d(w2)", "d(wb)", "W1", "W2", "Wb"))
sum=0
for i in range (len(x1)):
    dw1=x1[i]*y_act[i]
    dw2=x2[i]*y_act[i]
    dwb=xb[i]*y_act[i]
    w1=w1+dw1
    w2=w2+dw2
    wb=wb+dwb
    print("%-5d %-5d %-5d %-7d %-7d %-7d %-7d %-7d %-7d %-7d" % (x1[i], x2[i], xb[i], y_act[i], dw1, dw2, dwb, w1, w2, wb))

print("%-5s %-5s %-5s %-7s %-7s %-7s" % ("x1", "x2", "xb","y_act", "f(x)", "y_est"))
for j in range (4):
    sum=w1*x1[j]+w2*x2[j]
    sum=sum+wb*xb[j]
    if(sum>=2):
        print("%-5d %-5d %-5d %-7d %-7d %-7d " % (x1[j], x2[j], xb[j], y_act[j],sum,1))
    else :
       print("%-5d %-5d %-5d %-7d %-7d %-7d " % (x1[j], x2[j], xb[j], y_act[j],sum,-1))



print("Padmaja H, regno : 2021503034")
print("Hebbian model for NAND gate")
x1=[0,0,1,1]
x2=[0,1,0,1]
y_act=[1,1,1,0]
xb=[1,1,1,1]
#print("Fixing values of w1=1 and w2=1")
print("Fixing the activation function as \n \
      y_est=1 if f(x)>=2  \n \
      y_est=-1 if f(x)<2")
w1=0
w2=0
wb=0
print("Making the inputs and  outputs bipolar")
for i in range(len(x1)) :
    if(x1[i]==0):
        x1[i]=-1
        
for i in range(len(x2)) :
    if(x2[i]==0):
        x2[i]=-1   
for i in range(len(y_act)) :
    if(y_act[i]==0):
        y_act[i]=-1

#print(x1) 

#print("x1\tx2\ty_act\t d(w1) \t d(w2) \t d(wb) \t W1 \t W2 \t Wb")
print("%-5s %-5s %-5s %-7s %-7s %-7s %-7s %-7s %-7s %-7s" % ("x1", "x2", "xb","y_act", "d(w1)", "d(w2)", "d(wb)", "W1", "W2", "Wb"))
sum=0
for i in range (len(x1)):
    dw1=x1[i]*y_act[i]
    dw2=x2[i]*y_act[i]
    dwb=xb[i]*y_act[i]
    w1=w1+dw1
    w2=w2+dw2
    wb=wb+dwb
    print("%-5d %-5d %-5d %-7d %-7d %-7d %-7d %-7d %-7d %-7d" % (x1[i], x2[i], xb[i], y_act[i], dw1, dw2, dwb, w1, w2, wb))

print("%-5s %-5s %-5s %-7s %-7s %-7s" % ("x1", "x2", "xb","y_act", "f(x)", "y_est"))
for j in range (4):
    sum=w1*x1[j]+w2*x2[j]
    sum=sum+wb*xb[j]
    if(sum>=2):
        print("%-5d %-5d %-5d %-7d %-7d %-7d " % (x1[j], x2[j], xb[j], y_act[j],sum,1))
    else :
       print("%-5d %-5d %-5d %-7d %-7d %-7d " % (x1[j], x2[j], xb[j], y_act[j],sum,-1))
       
