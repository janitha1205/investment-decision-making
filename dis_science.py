
# Present value : PV
# future value : FV
# discounted rate : k(in %)
# number of years : n
import numpy as np
def FV(PV,k,n):
    return PV*pow((1+k),n)
def PV(FV,k,n):
    return FV/pow((1+k),n)
def NOY(FV,PV,k):
    return (np.log(FV/PV)/np.log(k+1))  
def ROI(FV,PV,n):
    return (pow((FV/PV),1/n)-1)  
P=100
k= 0.1   #(10%)
n=10  #after 10 years

print(FV(P,k,n))
F=100
k= 0.1   #(10%)
n=1  #before 1 years
print(PV(F,k,n))

F=100
k= 0.1   #(10%)
n=5  #before 5 years
print(PV(F,k,n))

F=100
k= 0.1   #(10%)
n=10  #before 10 years
print(PV(F,k,n))

F=100  # future value to be
P=10   # current value
k= 0.1   #(10%)

print(NOY(F,P,k))

F=150  # future value to be
P=100   # current value
n= 10   # number of years

print(ROI(F,P,n)*100)

# NPV calculation

# NPV>0 accept
# NPV<0 reject
# NPV=0 no profit rather than experience on investment

# FVs 1 2 3 4 5 years
F=[]
F.append(70000)
F.append(120000)
F.append(140000)
F.append(140000)
F.append(40000)

# to calculate PVs 1 2 3 4 5  opertunity cost 8%(ROI)
P=[]
P.append(PV(F[0],0.08,1))
P.append(PV(F[1],0.08,2))
P.append(PV(F[2],0.08,3))
P.append(PV(F[3],0.08,4))
P.append(PV(F[4],0.08,5))
PN=P
# cash inflow of all sum up all P1 tp P5

Cash_inflow=np.sum(P[:])

print(Cash_inflow)

# as investment to initiate the project

cash_out_flow=400000

#net present value
NPV=Cash_inflow-cash_out_flow
print("Net Present value:",NPV)


# internal rate of return(IRR)

# to NPV=0 cash inflow would be

cash_inflow_IRR=cash_out_flow
k=0.08
npv=NPV
while(npv>0):
        
    P.append(PV(F[0],k,1))
    P.append(PV(F[1],k,2))
    P.append(PV(F[2],k,3))
    P.append(PV(F[3],k,4))
    P.append(PV(F[4],k,5))

# cash inflow of all sum up all P1 tp P5

    CI=np.sum(P[:])
    P=[]
    
    npv=CI-cash_out_flow
    
    k=k+0.00000001
    
print(npv)
irr=(k-0.00000001)*100
print("internal rate of return: ",irr)
# checking IRR with discont rate if irr>discount rate project is worth
if irr>k:
    print("project is accepted acording to irr")
else :
    print("project is rejected")
    
#profitability index cash outflows and cash inflows as fraction

Pro_index=Cash_inflow/cash_out_flow
print("profitability index: ",Pro_index)
if Pro_index>0:
    print("project is accepted according to pro index")
else :
    print("project is rejected")
# pay back period
ern=PN[1]
rec=cash_out_flow
i=1
payback=0
while(payback!=1):
    if ern<rec:
        ern+=PN[i]
        i=i+1
    else:
       ern=(ern-PN[i-1])
       ratm=PN[i-1]/12 
       ern+=ratm
       p_m=1
       while(ern<rec):
           ern+=ratm
           p_m+=1
           payback=1
#pay back period
print("payback period years: ",i-1)
print("months: ",p_m)
        
           
       
       
    
