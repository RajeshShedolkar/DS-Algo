input_str = "fshlsq12%^f098hikd76"

def extract_num(str):
    output = []
    curr_num = ''
    for char in str:
        if char.isdigit():
            curr_num+=char
        else:
            if curr_num:
                output.append(curr_num)
                curr_num = ''
    if curr_num:
        output.append(curr_num)
    print(output)

extract_num(input_str)
