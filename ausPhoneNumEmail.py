#! python3
#phoneAndEmail.py - finds phone numbers and email addresses on the clipboard

import re
import pyperclip
from typing import List

#allow +614 and just 04 as well

PHONE_NUMBER_REGEX = re.compile(r'''(
                            (\s*\d{3}|\(\d{3}\))                #area code (optional)
                            (\s|\.|-)?                          #separator (optional)
                            (\d{3})                             #first three digits
                            (\.|-|\s)                           #second separator
                            (\d{4})                             #last four digits

                              )''', re.VERBOSE)

#TO DO:create email regex

EMAIL_REGEX = re.compile(r'''(  
                        [a-zA-Z0-9._$+-]+                       #username
                        @                                       #symbol
                        [a-zA-Z0-9.-]+                          #domain name 
                        (\.[a-zA-Z]{2,4})                       #dot-something        
                      
                        )''', re.VERBOSE)
#TO DO: find matches in clipboard text

def matchPattern(text: str) -> List[str]:
    matches = []
    for groups in PHONE_NUMBER_REGEX.findall(text):
        phoneNum = '-'.join([groups[1],groups[3],groups[5]])
        matches.append(phoneNum)
    for groups in EMAIL_REGEX.findall(text):
        matches.append(groups[0])
    return matches
        
    #TO DO: copy results to clipboard

def copyToClipboard(matches: List[str]) -> None:
    if len(matches)>0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found')
  
  
def main() -> None:
    text: str = str(pyperclip.paste())
    matches: List[str] = matchPattern(text)
    copyToClipboard(matches)
    
if __name__ == "__main__":
    main() 
