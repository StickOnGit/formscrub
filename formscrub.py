#! /usr/bin/env python

"""formscrub deletes the mp_uuid key-value pairs from imported .itpl files.
The resulting .itpl file will always be treated as a new form with new form sections.
This file can be imported over and over; it will always be treated as a new form."""
print
##u mad bro?
def end():
	print
	sys.exit(0)
##end u mad bro

try:
	import sys
	import plistlib as PLIB
except ImportError as reason:
	print """\tCouldn't run formscrub because: {reason}.
\tIf you're missing a module, you may need to download 'pip' or a similar Python package installer and then run 'pip install (missing module)'.
	
\tGoogle is your friend - use it! Use it now!!""".format(reason=reason)
	end()

def scrub(someobject, badvalue='mp_uuid'):
	"""Walks the structure of the plistlib-created dict and finds all the mpuuids and viciously eliminates them.
	
	Can optionally be passed a different key to search for."""
	if isinstance(someobject, dict):
		for k in someobject.keys():
			if k == badvalue:
				del someobject[k]
				_COUNT[0] += 1
			else:
				scrub(someobject[k], badvalue)
	elif isinstance(someobject, list):
		for i in reversed(range(len(someobject))):
			if someobject[i] == badvalue:
				del someobject[i]
				_COUNT[0] += 1
			else:
				scrub(someobject[i], badvalue)
	else:
		pass
	
	return "\tRemoved {count} instances of {badvalue} from {file}.".format(count=_COUNT[0], badvalue=badvalue, file=file)

if __name__ == '__main__':
	_COUNT = [0]
	try:
		file = sys.argv[1]
	except IndexError:
		print "\tformscrub needs the filename. Try 'formscrub myfile.itpl'."
		end()

	try:
		loadedplist = PLIB.readPlist(file)
	except:
		print "\tWasn't able to read '{file}'. Check the file and try again.".format(file=file)
		end()
		
	print "\t{file} is loaded. Scrubbing...".format(file=file)
	result = scrub(loadedplist)
	print result
	try:
		PLIB.writePlist(loadedplist, file)
		print "\tSuccessfully saved '{file}'.".format(file=file)
	except:
		print "\tCouldn't seem to save {file} after scrubbing it.".format(file=file)
		end()
	end()
