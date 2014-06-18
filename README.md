igem-wiki
=========

Wiki pages for the Aalto-Helsinki iGEM-2014 team.

* Installing the python upload tool
1. download the lib at
https://code.google.com/p/httplib2/downloads/list
extract and run `python setup.py install`. If you are on mac, you need to install python3 and `python3` instead of `python` in the rest of the instructions.

2. now it works

3. Usage:
It is used to update the wikipages without having to log in and click edit.
It automatically transfers contents of a file to a page.
`python upload.py <wikipage> <filename>`
wikipage:	the subpage in the wiki.
			eg. in igem.org/wiki/index.php?title=Team:teamname/members
			the wikipage is members
			
file:		filename in current directory

There is also an automatic option `python upload.py -auto`
which reads the source defined pages to wiki.
eg.
AUTO_PAGES = ["members", "main", "INDEX"]
will upload members.html to wikipage "members" and so on.
`INDEX` is a special entry. It updates the wiki main page (...index.php?title=Team:teamname) its contents are taken from INDEX.html

You can also specify a header and footer to be included in every page.
These can be stored in HEADER.html and FOOTER.html and are then automatically included when autoupdating. Please note that the names hav to be capitalized. This prevents collisions.
