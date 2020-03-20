Question:
    Determine whether a one-to-one character mapping exists from one string, s1, to another string,
    s2.
    For example, given s1 = abc and s2 = bcd, print "true" into stdout since we can map each
    character in "abc" to a character in "bcd".
    Given s1 = foo and s2 = bar, print "false" since the character ‘o’ cannot map to two characters.
    But given s1 = bar and s2 = foo, print "true" since each character in "bar" can be mapped to a
    character in "foo".

Approach:
    I determined that the fastest way to determine whether the one-to-one mapping existed from s1 to s2 would be to use dictionaries
    to count the number of distinct characters. After doing this in O(N) time and O(N) space, all that had to be done was to check
    whether the 'distinctness' of s1 equaled or exceed that of s2

