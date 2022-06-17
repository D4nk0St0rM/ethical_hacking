### Active Directory
'it is just a phone book for windows'

- 95% of fortune 1000 companies use AD for identity management
- Directory services to manage windows domains
- Information relating to objects
    - printers
    - computers
    - users
    - groups
- Authenticates using Kerberos Tickets
    - Linux, firewalls [non-windows] authenticates using RADIUS or LDAP
- Can be exploited without patchable vulnerabilities
    - features
    - trusts
    - components


#### AD components

- Domain Controller
    - AD DS directory store [the phone book]
    - Authentication
    - Updates other DCs in forest
    - Admin access
-  