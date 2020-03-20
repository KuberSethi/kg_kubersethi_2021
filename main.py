import sys

def main():
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    result = determine_mapping(s1, s2)
    sys.stdout.write(str(result))

def determine_mapping(s1, s2):
    occurrences = {}
    for char in s1:
        occurrences[char] = occurrences.get(char, 0) + 1 # track occurrences of each character in the first string, s1
    print(occurrences.items())

    distinct_s1 = len(occurrences.values()) # num of distinct chars in s1
    occurrences = {} # reset occurrences 
    for char in s2:
        occurrences[char] = occurrences.get(char, 0) + 1 # track occurrences of each character in the first string, s2
    print(occurrences.items())

    distinct_s2 = len(occurrences.values()) # num of distinct chars in s1
    print(distinct_s1, distinct_s2)

    return distinct_s1 >= distinct_s2 # in order for there to exist a one-to-one mapping from s1 to s2, 
                                      # the amount of distinct characters in s1 must equal or exceed that of s2

if __name__ == "__main__":
    main()