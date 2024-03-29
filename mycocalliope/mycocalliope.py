
from calliope_mini import *
import gc
gc.collect()
MYCO = 'mycobit'
DFLT = 'default'
READ = 'rb'
WRITE = 'wb'
p = bytearray(256)

def save():
	with open(MYCO, WRITE) as mb:
		mb.write(p)

def load(f):
	try:
		with open(f, READ) as mb:
			mb.readinto(p)
	except OSError:
		pass

def get_nib(b,n):
	if n:
		return p[b]&0x0F
	else:
		return (p[b]>>4)&0x0F

def set_nib(b,n,v):
	if n:
		p[b]=(p[b]&0xF0)|v
	else:
		p[b]=(v<<4)|(p[b]&0x0F)

def prg():
	PC=0
	nib=0
	moved=1
	load(MYCO)
	for i in range(2):
		for j in range(2):
			for k in range(4):
				if get_nib(i,j)&(1<<k):
					display.set_pixel(4-k,i*2+j,7*bool(get_nib(i,j)&(1<<k)))

	for i in range(4):
		display.set_pixel(4-i,nib%4,9)

	while button_b.is_pressed():
		pass

	while True:
		if button_a.is_pressed() and button_b.is_pressed():
			save()
			display.clear()
			while button_a.is_pressed() and button_b.is_pressed():
				pass
			break

		if button_a.is_pressed():
			if moved:
				moved=0
				set_nib(PC,nib%2,0x0F)
			set_nib(PC,nib%2,(get_nib(PC,nib%2)+1)%16)
			sleep(100)

		if button_b.is_pressed():
			moved=1
			nib=(nib+1)%512
			PC=nib>>1
			if nib%4==0:
				for i in range(2):
					for j in range(2):
						for k in range(4):
							display.set_pixel(4-k,i*2+j,7*bool(get_nib(PC+i,j)&(1<<k)))

			for i in range(4):
				display.set_pixel(0,i,5*bool(PC&(1<<i)))

			for i in range(4,8):
				display.set_pixel(4-(i-4),4,5*bool(PC&(1<<i)))

			for i in range(4):
				display.set_pixel(4-i,nib%4,9)
			sleep(100)

		for i in range(4):
			display.set_pixel(4-i,nib%4,7*bool(get_nib(PC,nib%2)&(1<<i)))
		sleep(100)

def run():
	A=B=C=D=PC=PAGE=RET=SKIP=INST=DATA=Row=0

	wait=[1,2,5]

	if p[0]==0xFF and p[1]==0xFF:
		load(DFLT)
		save()
	else:
		load(MYCO)

	while True:
		INST=get_nib(PC,0)
		DATA=get_nib(PC,1)

		#if INST==0x00 or INST==0x0F:
		#	if DATA:
		#		set_nib(C*16+B,1-(INST&0x01),A)
		#	else:
		#		A=get_nib(C*16+B,1-(INST&0x01))

		if INST==0x01:
			for i in range(4):
				display.set_pixel(4-i,Row,9*bool(DATA&(1<<i)))

		elif INST==0x02:
			if DATA==0x0E:
				slp=30000

			elif DATA==0x0F:
				slp=60000

			else:
				slp=(10**(DATA//3))*wait[DATA%3]

			sleep(slp)

		elif INST==0x03:
			PC=PC-DATA
			continue

		elif INST==0x04:
			A=DATA

		elif INST==0x05:
			if DATA==0x00:
				Row=A%4

			elif DATA==0x01:
				B=A

			elif DATA==0x02:
				C=A

			elif DATA==0x03:
				D=A

			elif DATA==0x04:
				for i in range(4):
					display.set_pixel(4-i,Row,9*bool(A&(1<<i)))

			elif DATA>=0x05 and DATA<=0x08:
				display.set_pixel(9-DATA,Row,9*(A&0x01))

			elif DATA==0x09:
				pin0.write_analog(A*68)

			elif DATA==0x0A:
				pin22.write_digital(A&0x01)

		elif INST==0x06:
			if DATA==0x00:
				A=Row

			elif DATA==0x01:
				A=B

			elif DATA==0x02:
				A=C

			elif DATA==0x03:
				A=D

			elif DATA==0x04:
				A=pin2.read_digital()

			elif DATA==0x09:
				A=int(pin1.read_analog()/64)

			elif DATA==0x0F:
				save()

		elif INST==0x07:
			if DATA==0x01:
				A=A+1

			elif DATA==0x02:
				A=A-1

			elif DATA==0x03:
				A=A+B

			elif DATA==0x04:
				A=A-B

			elif DATA==0x05:
				A=A*B

			elif DATA==0x06:
				if B:
					A=A//B

			elif DATA==0x07:
				A=A&B

			elif DATA==0x08:
				A=A|B

			elif DATA==0x09:
				A=A^B

			elif DATA==0x0A:
				A=A^0x0F

			elif DATA==0x0B:
				A=A<<1

			elif DATA==0x0C:
				A=A>>1

			elif DATA==0x0D:
				A=(A<<1)|((A&0x08)>>3)

			elif DATA==0x0E:
				A=(A>>1)|((A&0x01)<<3)

		elif INST==0x08:
			PAGE=DATA*16

		elif INST==0x09:
			PC=PAGE+DATA
			continue

		elif INST==0x0A:
			if C>0:
				C=C-1
				PC=PAGE+DATA
				continue

		elif INST==0x0B:
			 if D>0:
				D=D-1
				PC=PAGE+DATA
				continue

		elif INST==0x0C:
			SKIP=A==0
			if DATA==0x01:
				SKIP=A>B

			elif DATA==0x02:
				SKIP=A<B

			elif DATA==0x03:
				SKIP=A==B

			elif DATA>=0x04 and DATA<=0x0B:
				SKIP=(pin2.read_digital()&0x01==1*(DATA<0x08))

			elif DATA==0x0C:
				SKIP=button_a.is_pressed()

			elif DATA==0x0D:
				SKIP=button_b.is_pressed()

			#elif DATA==0x0E:
			#	SKIP=not button_a.is_pressed()

			#elif DATA==0x0F:
			#	SKIP=not button_b.is_pressed()

			if SKIP:
				PC=PC+1

		elif INST==0x0D:
			RET=PC+1
			PC=PAGE+DATA
			continue

		elif INST==0x0E:
			PC=RET
			continue

		PC=(PC+1)%256
		A=A&0xF

if button_b.is_pressed():
	prg()
run()
