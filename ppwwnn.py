
input_string = "9J<q=^':h*#*d:#+Jh*9)#'+#>)'Bs"
input_list = list(input_string)
#print(input_list)
i=0
output_list = []
while i < len(input_list):
    asciisymbol = ord(input_list[i])
    #print(asciisymbol)
    flag = asciisymbol + 10
    #print(chr(flag))
    output_list.append(chr(flag))
    flag_str = ''.join(map(str, output_list))
    print(flag_str)
    i= i + 1


