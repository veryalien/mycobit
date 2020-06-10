from microbit import *
import gc
gc.collect()

MYCO='mycobit'
DFLT='default'

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
    #moved=1
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
            sleep(200)
            display.clear()
            while button_a.is_pressed() and button_b.is_pressed():
                pass
            sleep(200)
            break

        if button_a.is_pressed():
            #if moved:
            #    moved=0
            #    set_nib(PC,nib%2,0x0F)
            set_nib(PC,nib%2,(get_nib(PC,nib%2)+1)%16)
            sleep(100)

        if button_b.is_pressed():
            #moved=1
            nib=nib+1
            PC=nib>>1
            if PC==256:
                nib=0
                PC=0
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

    wait=[1,2,5]
    Dout=[pin12, pin8, pin2, pin1]
    button=[button_a, button_b]

    pin16.set_pull(pin16.PULL_UP)
    pin15.set_pull(pin15.PULL_UP)
    pin14.set_pull(pin14.PULL_UP)
    pin13.set_pull(pin13.PULL_UP)

    if p[0]==0xFF and p[1]==0xFF:
        load(DFLT)
        save()
    else:
        load(MYCO)

    while True:
        INST=get_nib(PC,0)
        DATA=get_nib(PC,1)

        Din=pin16.read_digital()|(pin15.read_digital()<<1)|(pin14.read_digital()<<2)|(pin13.read_digital()<<3)

        if INST==0x00 or INST==0x0F:
            if DATA:
                set_nib(C*16+B,1-(INST&0x01),A)
            else:
                A=get_nib(C*16+B,1-(INST&0x01))

        elif INST==0x01:
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
                pin0.write_analog((A*64)%1023)
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
                A=int(pin1.read_analog()/64)
            elif DATA==0x0A:
                A=int(pin2.read_analog()/64)
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
            PC=RET
            continue

        PC=(PC+1)%256
        A=A%16

if button_b.is_pressed():
    prg()
run()
