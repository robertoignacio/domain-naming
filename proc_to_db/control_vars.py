# Variables for the control flow of the program
# Currently working on the Control Panel flow

# Set the TLD to be used
# TLD: Top Level Domain, like .com, .org, .net, .dev, etc.
tld_whitelist = ['com', 'org', 'net', 'dev']
# A list of all valid top-level domains is maintained by the IANA and is updated from time to time.
# https://data.iana.org/TLD/tlds-alpha-by-domain.txt
# A list of public suffix is maintained by Mozilla and is updated from time to time.
# https://publicsuffix.org/list/public_suffix_list.dat


# ---------------------------------
# Input variables, from a tld white list
tld = str(".dev")

# ---------------------------------