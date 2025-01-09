import numpy as np
# a= np.arange(12).reshape((3,4))
# print(a, "\n")
# print(10+a,"\n")
# print(2*a, "\n")
# print(2**a, "\n")
# print(a==7 , "\n")


# a=np.arange(0,16).reshape((4,4))
# a=a*2
# print(a, "\n")


# b=np.arange(1,21).reshape((4,5))
# b=b*2
# print(b, "\n")
# print(b[1], "\n")
# print(b[:,2], "\n")
# print(b[3:1], "\n")
# print(b[2,:], "\n")
# print(b[:], "\n")


names=np.array(["hem", "cyrus", "kant", "divye", "nayak", "gagan"])
results= np.array([17,14,20,18,13,15])
results[names== "kant"]