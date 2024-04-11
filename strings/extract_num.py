def extrct_numbers(s):
    output = []
    prev_flag = 0
    curr_num = ""
    for curr_char in s:
        if ord(curr_char) >= ord('0') and ord(curr_char) <=ord('9'):
            if prev_flag == 0:
                curr_num = curr_char
                prev_flag=1
            else:
                curr_num += curr_char
        else:
            if curr_num:
                output.append(curr_num)
            prev_flag = 0
            curr_num = ""
    if curr_num:
        output.append(curr_num)
    return output

if __name__=="__main__":
    s = "aaabb2345rr23$%io6iui066m"
    # s = "123abc12dhjsd0"
    print(extrct_numbers(s))
