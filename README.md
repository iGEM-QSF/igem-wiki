igem-wiki
=========

Wiki pages for the Aalto-Helsinki iGEM-2014 team.

* Installing the python upload tool
1. download the lib at
https://code.google.com/p/httplib2/downloads/list
extract and run `python setup.py install`

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
AUTO_PAGES = ["members", "main"]
will upload mambaers.html to wikipage "members" and so on.

