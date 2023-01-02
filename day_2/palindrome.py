def isPalindrome(x):
    """
        :type x: int
        :rtype: bool
        """
    return str(x) == str(x)[::-1]


if __name__ == "__main__":
    result = isPalindrome(121)
    print(result)

# True
#JEK __python__