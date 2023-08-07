import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
import pandas as pd
import uncertainties.unumpy as unp
import uncertainties as unc

intensity1 = np.array([2534.515,2439.292,2715.600,2712.573,1810.684])
density1 = np.array([0.475,0.329,0.519,0.439,0.363])

intensity2 = np.array([2550.795,2230.633,3764.176,3269.805,2570.548])
density2 = np.array([0.501,0.339,0.607,0.569,0.546])

intensity4 = np.array([4834.798,4006.645,3510.678,4332.710,4639.202])
density4 = np.array([0.619,0.567,0.520,0.616,0.667])

intensity6 = np.array([5225.657,5869.742,5227.637,5012.549,5543.436])
density6 = np.array([0.543,0.608,0.553,0.506,0.583])

intensity9 = np.array([4991.575,3493.804,5654.679,3378.457,5343.859])
density9 = np.array([0.546,0.424,0.657,0.448,0.630])

intensity12 = np.array([4193.363,4898.993,5802.657,3033.192,5113.116])
density12 = np.array([0.557,0.628,0.678,0.420,0.606])


reg1 = LinearRegression().fit(np.expand_dims(intensity1,axis=1), np.expand_dims(density1,axis=1))
reg2 = LinearRegression().fit(np.expand_dims(intensity2,axis=1), np.expand_dims(density2,axis=1))
reg4 = LinearRegression().fit(np.expand_dims(intensity4,axis=1), np.expand_dims(density4,axis=1))
reg6 = LinearRegression().fit(np.expand_dims(intensity6,axis=1), np.expand_dims(density6,axis=1))
reg9 = LinearRegression().fit(np.expand_dims(intensity9,axis=1), np.expand_dims(density9,axis=1))
reg12 = LinearRegression().fit(np.expand_dims(intensity12,axis=1), np.expand_dims(density12,axis=1))


X1 = np.linspace(786,3527) # 1min
X2 = np.linspace(956,4991)
X4 = np.linspace(1277,6117)
X6 = np.linspace(1451,6501)
X9 = np.linspace(1394,6782)
X12 = np.linspace(1225,5964)
y1 = reg1.predict(np.expand_dims(X1,axis=1))
y2 = reg2.predict(np.expand_dims(X2,axis=1))
y4 = reg4.predict(np.expand_dims(X4,axis=1))
y6 = reg6.predict(np.expand_dims(X6,axis=1))
y9 = reg9.predict(np.expand_dims(X9,axis=1))
y12 = reg12.predict(np.expand_dims(X12,axis=1))
print('1min: ',reg1.coef_,reg1.intercept_)
print('2min: ',reg2.coef_,reg2.intercept_)
print('4min: ',reg4.coef_,reg4.intercept_)
print('6min: ',reg6.coef_,reg6.intercept_)
print('9min: ',reg9.coef_,reg9.intercept_)
print('12min: ',reg12.coef_,reg12.intercept_)


def f(x, a, b):
    return a * x + b

# 1min
popt1, pcov1 = curve_fit(f, intensity1, density1)

a1 = popt1[0]
b1 = popt1[1]
print('1min: \nOptimal Values')
print('a1: ' + str(a1))
print('b1: ' + str(b1))
n1 = len(density1)

# compute r^2
r21 = 1.0-(sum((density1-f(intensity1,a1,b1))**2)/((n1-1.0)*np.var(density1,ddof=1)))
print('R^2: ' + str(r21))

# calculate parameter confidence interval
a1,b1 = unc.correlated_values(popt1, pcov1)
print('Uncertainty')
print('a1: ' + str(a1))
print('b1: ' + str(b1))

# calculate regression confidence interval
px1 = np.linspace(786,3527,1000)
py1 = a1*px1+b1
nom1 = unp.nominal_values(py1)
std1 = unp.std_devs(py1)



# 2min
popt2, pcov2 = curve_fit(f, intensity2, density2)

a2 = popt2[0]
b2 = popt2[1]
print('2min: \nOptimal Values')
print('a2: ' + str(a2))
print('b2: ' + str(b2))
n2 = len(density2)

# compute r^2
r22 = 1.0-(sum((density2-f(intensity2,a2,b2))**2)/((n2-1.0)*np.var(density2,ddof=1)))
print('R^2: ' + str(r22))

# calculate parameter confidence interval
a2,b2 = unc.correlated_values(popt2, pcov2)
print('Uncertainty')
print('a2: ' + str(a2))
print('b2: ' + str(b2))

# calculate regression confidence interval
px2 = np.linspace(956,4991,1000)
py2 = a2*px2+b2
nom2 = unp.nominal_values(py2)
std2 = unp.std_devs(py2)


# 4min
popt4, pcov4 = curve_fit(f, intensity4, density4)

a4 = popt4[0]
b4 = popt4[1]
print('4min: \nOptimal Values')
print('a4: ' + str(a4))
print('b4: ' + str(b4))
n4 = len(density4)

# compute r^2
r24 = 1.0-(sum((density4-f(intensity4,a4,b4))**2)/((n4-1.0)*np.var(density4,ddof=1)))
print('R^2: ' + str(r24))

# calculate parameter confidence interval
a4,b4 = unc.correlated_values(popt4, pcov4)
print('Uncertainty')
print('a4: ' + str(a4))
print('b4: ' + str(b4))

# calculate regression confidence interval
px4 = np.linspace(1277,6117,1000)
py4 = a4*px4+b4
nom4 = unp.nominal_values(py4)
std4 = unp.std_devs(py4)

# 6min
popt6, pcov6 = curve_fit(f, intensity6, density6)

a6 = popt6[0]
b6 = popt6[1]
print('6min: \nOptimal Values')
print('a6: ' + str(a6))
print('b6: ' + str(b6))
n6 = len(density6)

# compute r^2
r26 = 1.0-(sum((density6-f(intensity6,a6,b6))**2)/((n6-1.0)*np.var(density6,ddof=1)))
print('R^2: ' + str(r26))

# calculate parameter confidence interval
a6,b6 = unc.correlated_values(popt6, pcov6)
print('Uncertainty')
print('a6: ' + str(a6))
print('b6: ' + str(b6))

# calculate regression confidence interval
px6 = np.linspace(1451,6501,1000)
py6 = a6*px6+b6
nom6 = unp.nominal_values(py6)
std6 = unp.std_devs(py6)

# 9min
popt9, pcov9 = curve_fit(f, intensity9, density9)

a9 = popt9[0]
b9 = popt9[1]
print('9min: \nOptimal Values')
print('a9: ' + str(a9))
print('b9: ' + str(b9))
n9 = len(density9)

# compute r^2
r29 = 1.0-(sum((density9-f(intensity9,a9,b9))**2)/((n9-1.0)*np.var(density9,ddof=1)))
print('R^2: ' + str(r29))

# calculate parameter confidence interval
a9,b9 = unc.correlated_values(popt9, pcov9)
print('Uncertainty')
print('a9: ' + str(a9))
print('b9: ' + str(b9))

# calculate regression confidence interval
px9 = np.linspace(1394,6782,1000)
py9 = a9*px9+b9
nom9 = unp.nominal_values(py9)
std9 = unp.std_devs(py9)

# 12min
popt12, pcov12 = curve_fit(f, intensity12, density12)

a12 = popt12[0]
b12 = popt12[1]
print('12min: \nOptimal Values')
print('a12: ' + str(a12))
print('b12: ' + str(b12))
n12 = len(density12)

# compute r^2
r212 = 1.0-(sum((density12-f(intensity12,a12,b12))**2)/((n12-1.0)*np.var(density12,ddof=1)))
print('R^2: ' + str(r212))

# calculate parameter confidence interval
a12,b12 = unc.correlated_values(popt12, pcov12)
print('Uncertainty')
print('a12: ' + str(a12))
print('b12: ' + str(b12))

# calculate regression confidence interval
px12 = np.linspace(1225,5964,1000)
py12 = a12*px12+b12
nom12 = unp.nominal_values(py12)
std12 = unp.std_devs(py12)


fontsize = 16

# 1min
fig, ax1 = plt.subplots()

ax1.plot(intensity1,density1,'*r', label='measurement points')
# ax1.plot(X8,y8,'--',label='regression line')
ax1.plot(px1, nom1,'--', c='black',label='regression line')
ax1.plot(px1, nom1 - 1.96 * std1, c='orange',\
         label='95% confidence region')
ax1.plot(px1, nom1 + 1.96 * std1, c='orange')

ax1.set_xlabel('fluorescence intensity [$a.u.$]',fontsize=fontsize)
ax1.set_ylabel('volume fraction of platelets \n in the aggregate',fontsize=fontsize)
# ax2.set_ylabel('average velocity (mm/s)', color='tab:blue',fontsize=fontsize)
# ax1.set_title('WSR = 800 $s^{-1}$',fontsize=fontsize)
ax1.set_ylim(0,1.1)

ticksize = 16
ax1.tick_params(axis='x', labelsize= ticksize)
ax1.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=2,fontsize=14)
plt.grid(alpha=0.3)

plt.savefig('intensity/1min.png',bbox_inches='tight')
plt.show()



# 2min
fig, ax1 = plt.subplots()

ax1.plot(intensity2,density2,'*r', label='measurement points')
ax1.plot(px2, nom2,'--', c='black',label='regression line')
ax1.plot(px2, nom2 - 1.96 * std2, c='orange',\
         label='95% confidence region')
ax1.plot(px2, nom2 + 1.96 * std2, c='orange')

ax1.set_xlabel('fluorescence intensity [$a.u.$]',fontsize=fontsize)
ax1.set_ylabel('volume fraction of platelets \n in the aggregate',fontsize=fontsize)
# ax2.set_ylabel('average velocity (mm/s)', color='tab:blue',fontsize=fontsize)
# ax2.set_title('WSR = 2 $s^{-1}$',fontsize=fontsize)
ax1.set_ylim(0,1.1)

ax1.tick_params(axis='x', labelsize= ticksize)
ax1.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=2,fontsize=14)
plt.grid(alpha=0.3)

plt.savefig('intensity/2min.png',bbox_inches='tight')
plt.show()


# 4min
fig, ax1 = plt.subplots()

ax1.plot(intensity4,density4,'*r', label='measurement points')
ax1.plot(px4, nom4,'--', c='black',label='regression line')
ax1.plot(px4, nom4 - 1.96 * std4, c='orange',\
         label='95% confidence region')
ax1.plot(px4, nom4 + 1.96 * std4, c='orange')

ax1.set_xlabel('fluorescence intensity [$a.u.$]',fontsize=fontsize)
ax1.set_ylabel('volume fraction of platelets \n in the aggregate',fontsize=fontsize)
# ax1.set_ylabel('average velocity (mm/s)', color='tab:blue',fontsize=fontsize)
# ax1.set_title('WSR = 4 $s^{-1}$',fontsize=fontsize)
ax1.set_ylim(0,1.1)

ax1.tick_params(axis='x', labelsize= ticksize)
ax1.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=2,fontsize=14)
plt.grid(alpha=0.3)

plt.savefig('intensity/4min.png',bbox_inches='tight')
plt.show()


# 6min
fig, ax1 = plt.subplots()

ax1.plot(intensity6,density6,'*r', label='measurement points')
ax1.plot(px6, nom6,'--', c='black',label='regression line')
ax1.plot(px6, nom6 - 1.96 * std6, c='orange',\
         label='95% confidence region')
ax1.plot(px6, nom6 + 1.96 * std6, c='orange')

ax1.set_xlabel('fluorescence intensity [$a.u.$]',fontsize=fontsize)
ax1.set_ylabel('volume fraction of platelets \n in the aggregate',fontsize=fontsize)
# ax1.set_ylabel('average velocity (mm/s)', color='tab:blue',fontsize=fontsize)
# ax1.set_title('WSR = 6 $s^{-1}$',fontsize=fontsize)
ax1.set_ylim(0,1.1)

ax1.tick_params(axis='x', labelsize= ticksize)
ax1.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=2,fontsize=14)
plt.grid(alpha=0.3)

plt.savefig('intensity/6min.png',bbox_inches='tight')
plt.show()


# 9min
fig, ax1 = plt.subplots()

ax1.plot(intensity9,density9,'*r', label='measurement points')
ax1.plot(px9, nom9,'--', c='black',label='regression line')
ax1.plot(px9, nom9 - 1.96 * std9, c='orange',\
         label='95% confidence region')
ax1.plot(px9, nom9 + 1.96 * std9, c='orange')

ax1.set_xlabel('fluorescence intensity [$a.u.$]',fontsize=fontsize)
ax1.set_ylabel('volume fraction of platelets \n in the aggregate',fontsize=fontsize)
# ax2.set_ylabel('average velocity (mm/s)', color='tab:blue',fontsize=fontsize)
# ax2.set_title('WSR = 9 $s^{-1}$',fontsize=fontsize)
ax1.set_ylim(0,1.1)

ax1.tick_params(axis='x', labelsize= ticksize)
ax1.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=2,fontsize=14)
plt.grid(alpha=0.3)

plt.savefig('intensity/9min.png',bbox_inches='tight')
plt.show()


# 12min
fig, ax1 = plt.subplots()

ax1.plot(intensity12,density12,'*r', label='measurement points')
ax1.plot(px12, nom12,'--', c='black',label='regression line')
ax1.plot(px12, nom12 - 1.96 * std12, c='orange',\
         label='95% confidence region')
ax1.plot(px12, nom12 + 1.96 * std12, c='orange')

ax1.set_xlabel('fluorescence intensity [$a.u.$]',fontsize=fontsize)
ax1.set_ylabel('volume fraction of platelets \n in the aggregate',fontsize=fontsize)
# ax2.set_ylabel('average velocity (mm/s)', color='tab:blue',fontsize=fontsize)
# ax2.set_title('WSR = 12 $s^{-1}$',fontsize=fontsize)
ax1.set_ylim(0,1.1)

ax1.tick_params(axis='x', labelsize= ticksize)
ax1.tick_params(axis='y', labelsize= ticksize)

plt.legend(loc=2,fontsize=14)
plt.grid(alpha=0.3)

plt.savefig('intensity/12min.png',bbox_inches='tight')
plt.show()