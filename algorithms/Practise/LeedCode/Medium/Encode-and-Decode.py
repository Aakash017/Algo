class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        return ":;".join(_str)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        return str.split(":;")


s = Solution()
_str = ["lint", "code", "love", "you"]
print("actual string", _str)
encoded_str = s.encode(_str)
print("encoded str = ", encoded_str)
decoded_str = s.decode(encoded_str)
print("decode str", decoded_str)
