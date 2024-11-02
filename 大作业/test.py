from pylab import *
figure(figsize=(8,6), dpi=80)
subplot(1,1,1)
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)
plot(X, C, color = "blue", linewidth = 2.5, linestyle = "--", label = "cosine")
plot(X, S, color = "red", linewidth = 2.5, linestyle = "--", label = "sine")
legend(loc = "upper left")
xlim(-4,4)
ylim(-1.2, 1.2)


ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])
show()