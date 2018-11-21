import os
import fchat

import testgui as g

loginwindow = g.loginwindow()
loginwindow.mainloop()

acct_1 = fchat.account(os.environ['FLIST_USER'], os.environ['FLIST_PASS'])
acct_1.init_auth()

if acct_1.acct_dict['error']:
    print(acct_1.acct_dict['error'])

else:
    print(acct_1.acct_dict.keys())
    print(acct_1.acct_dict['default_character'])
    print(acct_1.acct_dict['characters'])
