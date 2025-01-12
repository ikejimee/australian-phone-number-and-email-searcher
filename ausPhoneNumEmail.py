#! python3
#phoneAndEmail.py - finds phone numbers and email addresses on the clipboard

import re
import pyperclip
from typing import List



PHONE_NUMBER_REGEX = re.compile(r'''(
                            (\+61|0)                            # Country code or leading zero 
                            (\s|\.|-)?                          # Separator (optional)
                            (4\d{2})                            # Two digits with leading 4
                            (\.|-|\s)                           # Separator (optional)
                            (\d{3})                             # Three digits
                            (\.|-|\s)                           # Separator (optional)
                            (\d{3})                             # Three digits
                              )''', re.VERBOSE)


EMAIL_REGEX = re.compile(r'''(  
                        [a-zA-Z0-9._$+-]+                       #username
                        @                                       #symbol
                        [a-zA-Z0-9.-]+                          #domain name 
                        \.[a-zA-Z]{2,}                          #dot-something        
                        )''', re.VERBOSE)

 

def matchPattern(text: str) -> List[str]:
    matches = []
    for groups in PHONE_NUMBER_REGEX.findall(text): # Ensure the groups are not empty (only allow full patterns formed)
        if groups[1:] is not None:
            phone_number = ''.join([groups[1],groups[3],groups[5], groups[7]])
            matches.append(phone_number)
    for email_match in EMAIL_REGEX.findall(text):
        matches.append(email_match)
    return matches 
        

def copyToClipboard(matches: List[str]) -> None:
    if len(matches)>0:
        pyperclip.copy('\n'.join(matches))
        print('The following has been copied to clipboard:')
        print('\n'.join(matches))
    else:
        print('There were no phone numbers or email addresses found')
  
  
def main() -> None:
    text: str = str(pyperclip.paste())
    matches: List[str] = matchPattern(text)
    copyToClipboard(matches)
    
if __name__ == "__main__":
    main() 
