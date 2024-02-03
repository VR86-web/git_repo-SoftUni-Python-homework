
class ValueTooSmallError(Exception):
    pass


amount_to_send = float(input())

if 0 <= amount_to_send < 1:
    raise ValueTooSmallError("Value is too low!")