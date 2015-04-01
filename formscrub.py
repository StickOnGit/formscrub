#! /usr/bin/env python

"""Deletes every uuid found in .itpl files.

Once the file is 'scrubbed' it can be imported and 
the software automatically assigns new uuids where necessary.

The file it produces should NOT be used outside the office.
"""

import sys
import plistlib as PLIB

def plog(msg):
    print "\t{}".format(msg)

def end(*out_msg):
    if out_msg:
        print
        for msg in out_msg:
            plog(msg)
    print
    sys.exit(0)

def scrub(template, bad='mp_uuid'):
    """Looks through the itpl for uuids and deletes them.
    
    Returns the number of deleted ids.
    """
    def clear(seq):
        """Deletes bad value in sequence if present.
        
        Returns 1 if deleted, 0 if not found.
        """
        if bad in seq:
            del seq[bad]
            return 1
        return 0
    
    count = clear(template)
    for section in template.get('iformSectionTiesArray', []):
        if 'iform_section' in section:
            sub_sec = section['iform_section']
            count += clear(sub_sec)
            for element in sub_sec.get('iformFieldsArray', []):
                count += clear(element)
    return count

if __name__ == '__main__':
    if not sys.argv[1:]:
        end("Please provide the file name.")
    temp = sys.argv[1]

    try:
        itpl = PLIB.readPlist(temp)
    except:
        end("Couldn't load the file. Exiting.")
        
    result = scrub(itpl)
    first_msg = "{} ids scrubbed.".format(result)
    second_msg = "Successfully saved {}.".format(temp)
    try:
        PLIB.writePlist(itpl, temp)
    except:
        second_msg = "Couldn't save after scrubbing."
    
    end(first_msg, second_msg)
