from machine import Pin
from microbit import *

def set_pixel(x,y,r,g,b):
    v=(r,g,b)
    display.Led.LoadPos(20-x*5+y,v)
    display.Led.Show()

def get_pixel(x,y):
    return display.Led.__getitem__(20-x*5+y)

display.set_pixel = set_pixel
display.get_pixel = get_pixel

MYCO='mycobit'
DFLT='default'

pin0.write_analog(0)
pin1.write_digital(0)
pin2.write_digital(0)
pin8.write_digital(0)
pin12.write_digital(0)

p16 = Pin(5, Pin.IN, Pin.PULL_UP)
p15 = Pin(23, Pin.IN, Pin.PULL_UP)
p14 = Pin(19, Pin.IN, Pin.PULL_UP)
p13 = Pin(18, Pin.IN, Pin.PULL_UP)
    
display.clear()

p=bytearray(256)

def save():
    with open(MYCO, 'wb') as mb:
        mb.write(p)

def load(fn):
    try:
        with open(fn, 'rb') as mb:
            mb.readinto(p)
    except OSError:
        pass

def get_nib(pb,nib):
    if nib:
        return p[pb]&0x0F
    else:
        return (p[pb]>>4)&0x0F

def set_nib(pb,nib,v):
    if nib:
        p[pb]=(p[pb]&0xF0)|v
    else:
        p[pb]=(v<<4)|(p[pb]&0x0F)

def prg():
    PC=0
    nib=0
    moved=1
    load(MYCO)
    for i in range(2):
        for j in range(2):
            for k in range(4):
                if get_nib(i,j)&(1<<k):
                    display.set_pixel(4-k,i*2+j,7*bool(get_nib(i,j)&(1<<k)),0,0)

    for i in range(4):
        display.set_pixel(4-i,nib%4,4,4,4)

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
                            display.set_pixel(4-k,i*2+j,7*bool(get_nib(PC+i,j)&(1<<k)),0,0)

            for i in range(4):
                display.set_pixel(0,i,0,1*bool(PC&(1<<i)),0)
            for i in range(4,8):
                display.set_pixel(4-(i-4),4,0,0,1*bool(PC&(1<<i)))

            for i in range(4):
                display.set_pixel(4-i,nib%4,4,4,4)
            sleep(100)

        for i in range(4):
            display.set_pixel(4-i,nib%4,7*bool(get_nib(PC,nib%2)&(1<<i)),0,0)
        sleep(100)

def run():
    A=0
    B=0
    C=0
    D=0
    Din=0
    PC=0
    PAGE=0
    RET=0
    SKIP=0
    INST=0
    DATA=0
    Row=0
    Red=9
    Green=0
    Blue=0

    wait=[1,2,5]
    Dout=[pin12, pin8, pin2, pin1]
    button=[button_a, button_b]

    if p[0]==0xFF and p[1]==0xFF:
        load(DFLT)
        save()
    else:
        load(MYCO)

    while True:
        INST=get_nib(PC,0)
        DATA=get_nib(PC,1)

        Din=bool(p16.value())|(bool(p15.value())<<1)|(bool(p14.value())<<2)|(bool(p13.value())<<3)

        if INST==0x00 or INST==0x0F:
            if DATA:
                set_nib(C*16+B,1-(INST&0x01),A)
            else:
                A=get_nib(C*16+B,1-(INST&0x01))

        elif INST==0x01:
            for i in range(4):
                display.set_pixel(4-i,Row,Red*bool(DATA&(1<<i)),Green*bool(DATA&(1<<i)),Blue*bool(DATA&(1<<i)))

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
                    display.set_pixel(4-i,Row,Red*bool(A&(1<<i)),Green*bool(A&(1<<i)),Blue*bool(A&(1<<i)))
            elif DATA>=0x05 and DATA<=0x08:
                display.set_pixel(9-DATA,Row,Red*(A&0x01),Green*(A&0x01),Blue*(A&0x01))
            elif DATA==0x09:
                pin0.write_analog((136+(A*3))%255)
            elif DATA==0x0A:
                for i in range(4):
                    Dout[i].write_digital((A>>i)&0x01)
            elif DATA>=0x0B and DATA<=0x0E:
                Dout[DATA-0X0B].write_digital(A&0x01)

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
                A=Din
            elif DATA>=0x05 and DATA<=8:
                A=(Din>>(DATA-5))&0x01
            elif DATA==0x09:
                A=int(pin1.read_analog()/256)
            elif DATA==0x0A:
                A=int(pin2.read_analog()/256)
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
                A=A/B
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
            elif DATA==0X0C:
                A=A>>1
            elif DATA==0x0D:
                A=(A<<1)|((A&0x08)>>3)
            elif DATA==0X0E:
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
                SKIP=(Din>>DATA%4)&0x01==1*(DATA<0x08)
            elif DATA>=0x0C and DATA<=0x0D:
                SKIP=button[DATA-0x0C].is_pressed()
            elif DATA>=0x0E:
                SKIP=not button[DATA-0x0E].is_pressed()
            if SKIP:
                PC=PC+1

        elif INST==0x0D:
            RET=PC+1
            PC=PAGE+DATA
            continue

        elif INST==0x0E:
            if DATA==0x00:
                PC=RET
                continue
            elif DATA==0x01:
                Red=A
            elif DATA==0x02:
                Green=A
            elif DATA==0x03:
                Blue=A
            elif DATA==0x04:
                A=Red
            elif DATA==0x05:
                A=Green
            elif DATA==0x06:
                A=Blue
            elif DATA==0x07:
                Red, Green, Blue = display.get_pixel(4-(A%4),Row)

        PC=(PC+1)%256
        A=A%16

if button_b.is_pressed():
    prg()
run()
