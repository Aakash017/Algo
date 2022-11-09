# s = "babad"
s = "ce"


def longestPalindrome(s: str) -> str:
    if len(s) == 1:
        return s
    elif s == s[::-1]:
        return s
    else:
        stack = []
        max_count = 0
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                _s = s[i:j]
                if _s == _s[::-1]:
                    count = j - i
                    if max_count < count:
                        max_count = count
                        if stack:
                            stack.pop()
                        stack.append(_s)
        print(stack)
        return stack[-1]


def optimisedlongestPalindrome(s: str) -> str:
    if len(s) == 1:
        return s
    elif len(s)==2:
        return s[0]
    elif s == s[::-1]:
        return s
    else:
        stack = []
        for i in range(1, len(s) - 1):
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s):
                _s = s[l:r]
                if _s == _s[::-1]:
                    # result=s[l:r]
                    # # if count > max_count:
                    # #     max_count = count
                    # if stack:
                    #     stack.pop()
                    stack.append(_s)
                    l -= 1
                    r += 1
                r += 1
        return max(stack)


# print(longestPalindrome(s))
print(optimisedlongestPalindrome("bb"))


def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    res = ""
    for i in range(len(s)):
        p1 = isPalindrome(s, i, i)
        p2 = isPalindrome(s, i, i + 1)
        if len(p1) > len(res):
            res = p1
        if len(p2) > len(res):
            res = p2
    return res


def isPalindrome(s: str, l: int, r: int) -> str:
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r]

print(longestPalindrome("abb"))




s="""
busislnescsicxpvvysuqgcudefrfjbwwjcchtgqyajdfwvkypfwshnihjdztgmyuuljxgvhdiwphrweyfkbnjgerkmifbirubhseuhrugwrabnjafnbdfjn
ufdstjbkuwtnpflffaqmjbhssjlnqftgjiglvvequhapasarlkcvbmkwnkuvwktbgfoaxteprobdwswcdyddyvrehvmxrrjiiidatidlpihkbmmruysmhhsncmfdanafdrfpdtfgkglcqpwrrtvacuicohspkounojuziittugpqjyhhkwfnflozbispehrtrnizowrlzcuollagxwtznjwzcumvedjwokueuqktvvouwnsmpxqvvpuwprezrbobrpnwaccwljchdguubjulyilzvmandjjleitweybqkjttschrjjlebnmponvlktzzcdtuybugggcqffkcffpamauvxfbonjrobgpvlyzveiwemmtdvbjciaytvesnocnjrwodtcokgcuoiicxapmrzpkfphjniuvzjrhbnqndfshoduejyktebgdabidxlkstepuwvtrtgbxaeheylicvhrxddijshcvdadxzsccmainyfpfdhqdanfccqkzlmhsfilvoybqojlvbcixjzqpbngdvesuokbxhkomsiqfyukvspqthlzxdnlwthrgaxhtpjzhrugqbfokrdcyurivmzgtynoqfjbafboselxnfupnpqlryvlcxeksirvufepfwczosrrjpudbwqxwldgjyfjhzlzcojxyqjyxxiqvfhjdwtgoqbyeocffnyxhyyiqspnvrpxmrtcnviukrjvpavervvztoxajriuvxqveqsrttjqepvvahywuzwtmgyrzduxfqspeipimyoxmkadrvrdyefekjxcmsmzmtbugyckcbjsrymszftjyllfmoeoylzeahnrxlxpnlvlvzltwnmldi"""