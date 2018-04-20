import os
import fchat

acct_1 = fchat.account(os.environ['FLIST_USER'], os.environ['FLIST_PASS'])
print(acct_1.ticket)

acct_1.get_ticket()
print(acct_1.ticket)
