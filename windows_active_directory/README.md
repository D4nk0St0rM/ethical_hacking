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

#### Summary

- Domain Controller
    - Domains [group and manage objects]
        - Parent + Children = Tree
            - Multiple Trees = Forest
    - Org Units
        -  objects
    - Trusts
        - one domain to another
        - Inherited trusts


##### AD components

- Domain Controller
    - AD DS directory store [the phone book]
    - Authentication
    - Updates other DCs in forest
    - Admin access
-  AD DS Schema
    - The definitions that can be created in AD [rule book]
- Domains [boundries]
    - Applying policies to groups of objects
-  Trees
    - shares namespace with main domain
    - Groups of domains
        - domain.com + europe.domain.com + dev.domains.com
    - child domains
    - trust sharing
- Forest
    - Groups of trees
    - common schema, configuration, catalog [search]
    - trust between domains
    - shared Admin groups
- Org Units [OU]
    - groups of computers, users, et cetera
    - hierarchy
    - manage objects
    - delegate permissions
    - policies
- Trusts
    - Directional
        - Flows from one domain to another
    - Transitive
        - Trusts everything other domains trust
- objects
    - inside OUs
    - user, contacts, groups, computers, printers, sharing




