igem-wiki
=========

These are the wiki pages for the Aalto-Helsinki iGEM-2014 team. The actual wiki can be found here: http://2014.igem.org/Team:Aalto-Helsinki.



iGEM Wiki Quickifier
====================

With this upload tool (upload.py) we could upload content to a our team wiki without using the cumbersome wiki interface.

Installation:

1. Download the lib at
https://code.google.com/p/httplib2/downloads/list
extract and run `python setup.py install`. If you are on mac, you need to install python3 and use `python3` instead of `python` in the rest of the instructions.

2. Now everything should be ready for use.

3. Usage:
With this tool you can update the wikipages without having to log in and click edit.
It automatically transfers contents of a file to a page.
`python upload.py <wikipage> <filename>`
(wikipage:	the subpage in the wiki.
			eg. in igem.org/wiki/index.php?title=Team:teamname/members
			the wikipage is members;
filename:	the name of the file you want to upload in current directory)

There is also an automatic option `python upload.py -auto`
which reads the source defined pages to wiki.
eg.
AUTO_PAGES = ["members", "main", "INDEX"]
will upload members.html to wikipage "members" and so on.
`INDEX` is a special entry. It updates the wiki main page (...index.php?title=Team:teamname) its contents are taken from INDEX.html

You can also specify a header and footer to be included in every page.
These can be stored in HEADER.html and FOOTER.html and are then automatically included when autoupdating. Please note that the names hav to be capitalized. This prevents collisions.
