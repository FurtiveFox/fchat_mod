import os
import fchat

acct_1 = fchat.account(os.environ['FLIST_USER'], os.environ['FLIST_PASS'])

print(acct_1.ticket)
print(acct_1.defaultcharacter)
