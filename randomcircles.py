import stdrandom,stddraw,sys,random

#----------------
# creat random circle
#----------------


"""
   python randomcircles.py 100

"""
n=int(sys.argv[1])
while True:
    for i in range(n):
        r=stdrandom.bernoulli()
        xr=random.random()
        yr=random.random()
        if r==True:
           stddraw.setPenColor(stddraw.BLUE)
        else:
           stddraw.setPenColor(stddraw.BLACK)
        stddraw.filledCircle(xr,yr,0.02)
    stddraw.show()




