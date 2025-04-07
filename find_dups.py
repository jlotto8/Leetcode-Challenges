def hasDuplicate(nums) -> bool:

    seen = set()
    for n in nums:
        if n not in seen:
            seen.add(n)
        else:
            return True
    return False
    # return n in seen 

print(hasDuplicate([1, 2, 3, 3, 4]))