def min_subseq(source, target):
    
    # if target string contains a char not in source string, invalid
    if not set(target).issubset(set(source)):
        return -1
    
    count = 0 # number of subsequence
    target_pointer = 0 # track target

    while target_pointer < len(target):
        source_pointer = 0

        while source_pointer < len(source):
            if target[target_pointer] == source[source_pointer]:
                # if same char, both point to the next char
                target_pointer += 1
                source_pointer += 1
            else:
                # if different, compare target char to the next source char
                source_pointer += 1
        count += 1

    return count

def main():
    
    print(min_subseq('abc', 'abcbc'))
    print(min_subseq('abc', 'acdbc'))
    print(min_subseq('xyz', 'xzyxz'))

if __name__ == "__main__":
    main()


