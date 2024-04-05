def rep_char(st, num) :
    print(st * num)


def draw_line_string(msg1) :
    msg1 = 'Hello ' + msg1 + ','
    msg1_length = len(msg1)
    msg1_num = msg1_length + 2
    msg2 = 'Welcom to Seoul.'
    msg2_length = len(msg2)
    msg2_num = msg2_length + 2

    if(msg1_length > msg2_length) :
        rep_char('-', msg1_num)
        print(f' {msg1}')
        print(f' {msg2}')
        rep_char('-', msg1_num)
    
    else :
        rep_char('-', msg2_num)
        print(f' {msg1}')
        print(f' {msg2}')
        rep_char('-', msg2_num)

msg1 = input('Input his/her name: ')
draw_line_string(msg1)
    
