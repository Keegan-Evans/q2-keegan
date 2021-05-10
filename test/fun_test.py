import sys

def sprinkle(input_file,
             case_mode,
             out_file,
             sort_ascending=False,
             sort_descending=False):
    contents = []
    with open(input_file, 'r') as fh:
        for line in fh:
            if line.rstrip():
                contents.append(line)
    # Sort if appropriate 
    sort_var = None
    if sort_ascending:
        sort_var=False
    if sort_descending:
        sort_var=True
    if sort_var is not None:
        contents.sort(key=lambda x: x[0].lower(), reverse=sort_var)

    print(contents)

    # Apply the desired case transformation
    case_transformer = {
            'all_upper': str.upper,
            'all_lower': str.lower,
            'invert': str.swapcase,
            }[case_mode]

    for i, line in enumerate(contents, 0):
        contents[i] = case_transformer(line)

    # write out to file
    with open(out_file, 'w') as fw:
        for line in contents:
            fw.write(line)

    # sorted_lines = contents.sort()

    # for i in contents:
    #     print(i.rstrip().split(" "))

if __name__ == '__main__':
    sprinkle(input_file='./test/test2.txt',
             case_mode='invert',
             out_file='./test/outtest_invert.txt')

    sprinkle(input_file='./test/test2.txt',
             case_mode='all_lower',
             out_file='./test/outtest_lower.txt')

    sprinkle(input_file='./test/test2.txt',
             case_mode='all_upper',
             out_file='./test/outtest_upper.txt')
    
    sprinkle(input_file='./test/test2.txt',
             case_mode='all_lower',
             sort_ascending=True,
             out_file='./test/outtest_ascending.txt')

    sprinkle(input_file='./test/test2.txt',
             case_mode='all_lower',
             sort_descending=True,
             out_file='./test/outtest_descending.txt')
