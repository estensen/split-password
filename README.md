# split-password

Prototype of a split-password scheme for password recovery in a semi-trusted environment.
A password is split into shares using a trivial secret sharing scheme. You can only recover the password by combining all the shares.

## Example
```sh
$ python split_password.py supersecret 3
Password: supersecret
Shares: ['WgxepHzwwN9xEA', '0T7UMP0hr-pPwg', '\x14F?UOk/|w\x06=']
Recovered password: supersecret
```

