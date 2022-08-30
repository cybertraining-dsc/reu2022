# Generating the book

A number of different repositories must
be cloned to your ~/cm folder before
generating the book. These are the required
repositories:

* <https://github.com/cloudmesh-community/pub>
* <https://github.com/cloudmesh-community/book>
* <https://github.com/cybertraining-dsc/su22-reu-385>

Docker must be running, as well. If you have
docker desktop, simply start the program and
have it running in the background.

To generate the book, stand in reu2022/book
and run `make -f Makefile.docker all`

If these instructions become outdated and there
is no Makefile.docker due to its removal, then
simply run `make all` instead.
