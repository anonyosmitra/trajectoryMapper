import matplotlib.pyplot as plt
import numpy as np
def euler(dt=0.05,gx=0,gy=-10,vx=10,vy=10,kx=1,ky=1):
	xs=[0]
	ys=[0]
	ts=[0]
	t=0
	sx=0
	sy=0
	dsx=vx*dt
	dsy=vy*dt
	dvx=(gx+kx)*dt
	dvy=(gy+ky)*dt
	started=False
	while(not started or sy>=0):
		if not started:
			started=True
		sx+=dsx
		sy+=dsy
		t+=dt
		xs.append(sx)
		ys.append(sy)
		ts.append(t)
		vx+=dvx
		vy+=dvy
		dsx=vx*dt
		dsy=vy*dt
		dvx=(gx+kx)*dt
		dvx=(gy+ky)*dt
	plt.plot(np.array(ts), np.array(ys))

def impEuler(dt=0.05,gx=0,gy=-10,vx=10,vy=10,kx=0,ky=0):
	ys=[0]
	ts=[0]
	t=0
	sx=0
	sy=0
	dtx=vx+(gx*dt/2)
	dty=vy+(gy*dt/2)
	dsx=dtx*dt
	dsy=dty*dt
	dvx=(gx+kx)*dt
	dvy=(gy+ky)*dt
	vx+=dvx
	vy+=dvy
	started=False
	while(not started or sy>=0):
		if not started:
			started=True
		sx+=dsx
		sy+=dsy
		t+=dt
		ys.append(sy)
		ts.append(t)
		dtx=vx+(gx*dt/2)
		dty=vy+(gy*dt/2)
		dsx=dtx*dt
		dsy=dty*dt
		dvx=(gx+kx)*dt
		dvy=(gy+ky)*dt
		vx+=dvx
		vy+=dvy
	plt.plot(np.array(ts), np.array(ys))
euler()
impEuler()
plt.show()