"""Kata: Tribonacci Sequence
kyu 6
#1 Best Practices Solution by Azuaron, Abhi_Scorp

def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res
"""
def tribonacci(signature, n):
    """This code takes an array of three numbers as the signature, and a number as n.
    It returns an list containing the entire tribonacci(like fibonacci, but adding the last 3 instead of 2)
    from the signature as a starting point, up until step n."""
    if n == 0:
        return []
    if n <= 3:
        return signature[:n]
    signature.append(sum(signature[-3:]))
    tribonacci(signature, n - 1)
    return signature
