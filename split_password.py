import argparse
import binascii
import secrets


def xor_strings(s, t):
    #return binascii.hexlify(''.join(chr(ord(a)^ord(b)) for a, b in zip(s, t)))
    return ''.join(chr(ord(a)^ord(b)) for a, b in zip(s, t))

parser = argparse.ArgumentParser(description="Split password into secret shares")
parser.add_argument("password", type=str, help="Input password")
parser.add_argument("n", type=int, help="Num of shares to split password into")

args = parser.parse_args()

password = args.password
n_shares = args.n

password_len = len(password)

# Create shares
shares = []
last_share = password
for i in range(n_shares-1):
    # token_urlsafe for pretty print
    secret = secrets.token_urlsafe(password_len-1)
    shares.append(secret)
    last_share = xor_strings(last_share, secret) 

shares.append(last_share)


# Recover password from shares
recovered_password = shares[0]
for i in range(1, len(shares)):
    recovered_password = xor_strings(recovered_password, shares[i])


print(f"Password: {password}")
print(f"Shares: {shares}")
print(f"Recovered password: {recovered_password}")

