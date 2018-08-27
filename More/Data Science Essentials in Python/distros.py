import scipy.stats, numpy as np
import matplotlib.pyplot as plt, matplotlib

np.random.seed(0)

matplotlib.style.use("ggplot")

plt.subplot(2,2,1)
plt.title('Continuous uniform')
plt.xlim(xmin=-1,xmax=1)
plt.ylim(ymin=-0.1,ymax=1.2)
plt.plot([-1,-0.5,-0.5,0.5,0.5,1],[0,0,1,1,0,0],'-')

plt.subplot(2,2,2)
plt.title('Normal')
plt.xlim(xmin=-1,xmax=1)
plt.ylim(ymin=-0.1,ymax=2.2)
plt.plot(np.array(range(-50,51,1))/50,[scipy.stats.norm(0,.2).pdf(x/100) for x in range(-50,51,1)],'-')

plt.subplot(2,2,3)
plt.title('Binomial, n=11, p=0.9')
rd = np.random.binomial(11,0.9,size=1000)
plt.hist(rd,bins=np.arange(min(rd),max(rd)+2)-0.5,normed=True,rwidth=0.5)

plt.subplot(2,2,4)
plt.title('Binomial, n=4, p=0.5')
rd=np.random.binomial(4,0.5,size=1000)
plt.hist(rd,bins=np.arange(min(rd),max(rd)+2)-0.5,normed=True,rwidth=0.5)

plt.tight_layout() 
plt.savefig("../images/distros.pdf")
