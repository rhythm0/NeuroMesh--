def check_parentheses(input_string):
    # 2 list for comparison using pointer
    list1 = list(input_string)
    list2 = list(input_string)
    label_list = [' '] * len(input_string) # empty label list of the same length as input
    
    i = 0
    while i < len(list1):
        if list1[i] == '(':
            matched = False
            # Search for right parenthesis in list2
            for j in range(i + 1, len(list2)):
                if list2[j] == ')':
                    list2[j] = ' '  # Mark the matched right parenthesis as empty space
                    matched = True
                    break
            if not matched:
                # Mark unmatched left parenthesis with 'x'
                label_list[i] = 'x'
        elif list1[i] == ')':
            matched = False
            # Search for left parenthesis in list2
            for j in range(i):
                if list2[j] == '(':
                    list2[j] = ' '  # # Mark the matched left parenthesis as empty space
                    matched = True
                    break
            if not matched:
                label_list[i] = '?' # Mark unmatched right parenthesis with '?'
        i += 1
    
    return input_string, ''.join(label_list)

def main():
    input_strings = [
        "bge)))))))))",
        "((IIII))))))",
        "()()()()(uuu",
        "))))UUUU((()"
    ]
    
    for input_string in input_strings:
        original, labels = check_parentheses(input_string)
        print(original)
        print(labels)

if __name__ == "__main__":
    main()
