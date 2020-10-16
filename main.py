# Copyright (c) 2020 @devanteayris
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# DISCLAMER This tool was developed for educational goals. 
# The author is not responsible for using to others goals.

from key import *
from helpers import haveibeenpwned_paste, haveibeenpwned_search, dehashed_domain_search

# HAVEIBEENPWNED API CHECK (EMAIL CHECKS)
haveibeenpwned_search(HAVEIBEENPWNED_KEY)
print("\nPastebin Search Upcoming.....")
haveibeenpwned_paste(HAVEIBEENPWNED_KEY)

# DEHASHED API CHECK (FULL DOMAIN SEARCH)
query = input("Enter a Domain for Search: ")
dehashed_domain_search(DEHASHED_KEY, query)






