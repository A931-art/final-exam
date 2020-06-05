import numpy as np
import matplotlib.pyplot as plt

def DFT(function_array):
    N = len(function_array)
    Fourier_array = []
    for m in range(N):
        f = 0
        for n in range(N):
            f += function_array[n] * np.exp(- 2j *np.pi * m * n / N)
        Fourier_array.append(f / (np.sqrt(N)))
    return Fourier_array

x_min = -1.0
x_max = 1.0
sampling_rate_1 = 256
delta = (x_max-x_min)/(sampling_rate_1-1)
function_array = np.zeros(sampling_rate_1)
x_arr = np.zeros(sampling_rate_1)
for i in range(sampling_rate_1):
        function_array[i] = 1
        x_arr[i] = x_min+i*delta
nft =  DFT(function_array)
karr =2*np.pi* np.fft.fftfreq(sampling_rate_1, d=delta)
fact = np.exp(-1j * karr * x_min)
aft = delta * np.sqrt(sampling_rate_1/(2.0*np.pi)) * fact * nft

fig1=plt.subplots()
plt.plot(x_arr,function_array,'r',label='The constant function')
plt.xlabel('x',fontsize=16)
plt.ylabel('f(x)',fontsize=16)
plt.grid(True)

fig2=plt.subplots()
plt.plot(karr,aft,'g', label='The fourier transform of the constant function for sampling rate 1')
plt.xlabel('k',fontsize=16)
plt.ylabel('g(k)',fontsize=16)
plt.grid(True)

sampling_rate_2 = 512
delta = (x_max-x_min)/(sampling_rate_2-1)
function_array = np.zeros(sampling_rate_2)
x_arr = np.zeros(sampling_rate_2)
for i in range(sampling_rate_2):
        function_array[i] = 1
        x_arr[i] = x_min+i*delta
nft =  DFT(function_array)
karr =2*np.pi* np.fft.fftfreq(sampling_rate_2, d=delta)
fact = np.exp(-1j * karr * x_min)
aft = delta * np.sqrt(sampling_rate_2/(2.0*np.pi)) * fact * nft

fig3=plt.subplots()
plt.plot(karr,aft,'y', label='The fourier transform of the constant function for sampling rate 2')
plt.xlabel('k',fontsize=16)
plt.ylabel('g(k)',fontsize=16)
plt.grid(True)

sampling_rate_3 = 1024
delta = (x_max-x_min)/(sampling_rate_3-1)
function_array = np.zeros(sampling_rate_3)
x_arr = np.zeros(sampling_rate_3)
for i in range(sampling_rate_3):
        function_array[i] = 1
        x_arr[i] = x_min+i*delta
nft =  DFT(function_array)
karr =2*np.pi* np.fft.fftfreq(sampling_rate_3, d=delta)
fact = np.exp(-1j * karr * x_min)
aft = delta * np.sqrt(sampling_rate_3/(2.0*np.pi)) * fact * nft

fig4=plt.subplots()
plt.plot(karr,aft,'b', label='The fourier transform of the constant function for sampling rate 3')
plt.xlabel('k',fontsize=16)
plt.ylabel('g(k)',fontsize=16)
plt.grid(True)
plt.show()
