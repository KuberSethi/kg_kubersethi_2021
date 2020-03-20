import sys

def main():
    # Check for missing arguments
    if len(sys.argv) < 3:
        arg_err = 'Error: Missing arguments for s1 and s2'
        sys.stdout.write(arg_err)
        exit()
    
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    
    valid_input, errors = check_input(s1, s2) # validate input

    if valid_input: # input is valid, so proceed
        result = determine_mapping(s1, s2)
        sys.stdout.write(str(result))        
        exit()
    else: # return errors to user
        input_err = ''.join(errors)
        sys.stdout.write(input_err)
        exit()

def check_input(s1, s2):
    """check_input : Function to handle invalid / incorrect input in an easily expandable way. """
    valid_input = True
    errors = []
    if type(s1) != str:
        valid_input = False
        errors.append('Error: s1 is not a string')      
    if type(s2) != str:
        valid_input = False
        errors.append('Error: s2 is not a string')          
    if len(s1) == 0 and len(s2) != 0:
        valid_input = False
        errors.append('Error: s1 is empty')
    if len(s1) != 0 and len(s2) == 0:
        valid_input = False
        errors.append('Error: s2 is empty')

    return valid_input, errors

def determine_mapping(s1, s2):
    """determine_mapping : Function that takes in a string s1, and a string s2, and returns a string representing whether there is a one-to-one mapping from s1 to s2."""
    if len(s1) == 0 and len(s2) == 0: # assuming that case where both are empty strings results in a valid one-to-one mapping
        return True

    occurrences = {}
    for char in s1:
        occurrences[char] = occurrences.get(char, 0) + 1 # track occurrences of each character in the first string, s1
    distinct_s1 = len(occurrences.values()) # num of distinct chars in s1

    occurrences = {} # reset occurrences 
    for char in s2:
        occurrences[char] = occurrences.get(char, 0) + 1 # track occurrences of each character in the first string, s2
    distinct_s2 = len(occurrences.values()) # num of distinct chars in s1

    return len(s1) <= len(s2) and distinct_s1 >= distinct_s2 # in order for there to exist a one-to-one mapping from s1 to s2, 
                                      # the amount of distinct characters in s1 must equal or exceed that of s2,
                                      # and the length of s1 must be less than or equal to

if __name__ == "__main__":
    main()