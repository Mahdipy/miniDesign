
def returnReg(char, num):
    num = int(num)
    if char == 't' and num == 8:
        return 24

    if char == 't' and num == 9:
        return 25

    if char == 't':
        return num + 8

    if char == 'a':
        return num + 4

    if char == 's':
        return num + 16


def extent5(x):
    l = 5 - len(x)
    return  (l *'0')+x


def extent16(x):
    l = 16 - len(x)
    return (l * '0')+x

def extent26(x):
    l = 26 - len(x)
    return  (l * '0') +x


binarycode = []
a = input('enter  assembly code\n')
while(a != '') :


    operand = a.split(' ')[0]
    AsemCode = a.split(' ')[1]
    AsemCode = AsemCode.split(',')

    if operand == 'j':
        opcode = '000010'
        y = int(int(AsemCode[0])/4)
        y = extent26(bin(y)[2:])
        binarycode.append(y+opcode)

    if operand == 'add' or operand == 'sub' or operand == 'or' or operand == 'and' or operand == 'slt' :
        st = ''
        func = ''
        reg0 = AsemCode[0]
        x = returnReg(reg0[1],reg0[2])
        x = extent5(bin(x)[2:])

        reg1 = AsemCode[1]
        y = returnReg(reg1[1] , reg1[2])
        y = extent5(bin(y)[2:])

        reg2 = AsemCode[2]
        z = returnReg(reg2[1] , reg2[2])
        z = extent5(bin(z)[2:])
        opcode = '000000'
        shamt  = '00000'

        if (operand == 'add') :
            func = '100000'

        if (operand == 'sub') :
            func = '100010'

        if (operand == 'or'):
            func = '100101'

        if (operand == 'and') :
            func = '100100'

        if (operand == 'slt') :
            func = '101010'

        st = func + shamt + x + z + y + opcode
        binarycode.append(st)

    elif operand == 'addi' or operand == 'slti' or operand == 'andi' or operand == 'ori' or operand == 'bne' or operand == 'beq':
        opcode =''
        reg0 = AsemCode[0]
        reg1 = AsemCode[1]
        reg2 = AsemCode[2]

        x = returnReg(reg0[1], reg0[2])
        x = extent5(bin(x)[2:])

        y = returnReg(reg1[1], reg1[2])
        y = extent5(bin(y)[2:])

        z = int(reg2)
        z = extent16(str(bin(z)[2:]))

        if operand == 'addi' :
            opcode = '001000'

        if operand == 'slti' :
            opcode = '001010'

        if operand == 'andi' :
            opcode = '001100'

        if operand == 'ori' :
            opcode =  '001101'

        if operand == 'beq':
            opcode = '000100'

        if operand == 'bne':
            opcode = '00101'

        st = z + x + y + opcode
        binarycode.append(st)

    elif operand == 'lw' or operand == 'sw' :
        opcode = ''
        reg0 = AsemCode[0]
        reg1 = AsemCode[1]

        x = returnReg(reg0[1],reg0[2])
        x = extent5(bin(x)[2:])

        y = returnReg(reg1.split('(')[1][1],reg1.split('(')[1][2])
        y = extent5(bin(y)[2:])

        z = int(reg1.split('(')[0])
        z = extent16(bin(z)[2:])

        if operand == 'lw' :
            opcode = '100011'

        if operand == 'sw' :
            opcode = '101011'

        st = z + x + y + opcode
        binarycode.append(st)
    a = input()
print(binarycode)

