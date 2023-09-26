import re

txt ='''
Note 1 - Overview

Tesla,
Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the
State of Delaware on July 1, 2003. We design, develop, manufacture and sell
high-performance fully electric vehicles and design, manufacture, install and
sell solar energy generation and energy storage products. Our Chief Executive
Officer, as the chief operating decision maker (“CODM”), organizes our company,
manages resource allocations and measures performance among two operating and
reportable segments: (i)
automotive and (ii) energy generation and storage. We have also previously been
affected by temporary manufacturing closures, employment and compensation
adjustments and impediments to administrative activities supporting our product
deliveries and deployments.


Note 2 - Summary of Significant Accounting Policies

Unaudited
Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated
statements of operations, the consolidated statements of comprehensive income,
the consolidated statements of redeemable noncontrolling interests and equity
for the three and nine months ended September 30, 2021 and 2020 and the
consolidated statements of cash flows for the nine months ended September 30,
2021 and 2020, as well as other information disclosed in the accompanying
notes, are unaudited. The consolidated balance sheet as of December 31, 2020
was derived from the audited consolidated financial statements as of that date.
'''

x = re.findall('Note.*\n', txt)
for match in x:
    print(match)

