
"""
    format positive integer-like N for display with
    commas between digit groupings: "xxx,yyy,zzz".
"""

def commas(N):
    digits = str(N)
    assert(digits.isdigit())
    result = ''
    while digits:
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + ',' + result) if result else last3
    return result

def money(N, numwidth = 0, currency='$'):
    """
        format number N for display with commas, 2 decimal digits,
        leading $ and sign, and optional padding: "$ -xxx,yyy.zz"
        numwidht=0 for no space padding, currency='' to omit symbol,
        and non-Ascii for other.

    """
    sign = '-' if N < 0 else ''
    N = abs(N)
    whole = commas(int(N))
    fract = ('%.2f' % N)[-2:]
    number = '%s%s.%s' % (sign, whole, fract)
    return '%s%*s' % (currency, numwidth, number)

print(money(999999999, 15))