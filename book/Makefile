NAME=reu2022
AI=ai
CM=../..
BOOK=${CM}/book
FINAL=${CM}/pub
HOME=..

include makefile.sys

all: pull epub pdf


docker-all:
	make -f Makefile.docker all

docker-shell:
	make -f Makefile.docker shell


# authors

pull:
	git pull
	cd ../../cloudmesh-common; git pull
	cd ../../cloudmesh-cc; git pull
	cd ../../su22-reu-385; git pull

info:
	ls ${CM}

epub: clean version bib
	mkdir -p dest
	# ./timeseries-references.bib
	cat $(CM)/su22-reu-385/*.bib $(CM)/book/bib/*.bib $(HOME)/*.bib  > dest/all.bib
	bookmanager $(NAME).yaml get
	bookmanager $(NAME).yaml epub
	cp ./dest/vonLaszewski-$(NAME).epub $(FINAL)/docs

pdf: epub
	bookmanager $(NAME).yaml pdf
	cp ./dest/vonLaszewski-$(NAME).pdf $(FINAL)/docs

ai: clean pull version bib
	mkdir -p dest
	cat $(CM)/su22-reu-385/*bib $(CM)/book/bib/*.bib $(HOME)/*.bib  > dest/all.bib
	bookmanager $(AI).yaml get
	bookmanager $(AI).yaml epub
	bookmanager $(AI).yaml pdf
	cp ./dest/vonLaszewski-$(AI).epub $(FINAL)/docs
	cp ./dest/vonLaszewski-$(AI).pdf $(FINAL)/docs


draft: clean version
	mkdir -p dest
	cat $(cm)/bib/*.bib > dest/all.bib
	bookmanager $(NAME)-draft.yaml get
	$(OPEN_EPUB) dest/vonLaszewski-$(NAME)-draft.epub


epub-pdf:
	ebook-convert \
	  $(FINAL)/docs/vonLaszewski-$(NAME).epub \
	  $(FINAL)/docs/vonLaszewski-$(NAME).pdf

dest: clean fonts version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME).yaml get
	ebook-convert \
	  dest/vonLaszewski-$(NAME).epub \
	  dest/vonLaszewski-$(NAME).pdf

publish:
	cd $(FINAL); git commit -m "update python book" \
	  docs/vonLaszewski-$(NAME).epub \
	  docs/vonLaszewski-$(NAME).pdf; git push
bib:
	mkdir -p dest/bib
	mkdir -p dest/book
	touch dest/book/empty.md
	touch dest/empty.md
	cp $(BOOK)/bib/*.bib dest/bib

version:
	TZ=":US/Eastern"; date > ../version.md

view:
	-killall Books
	$(OPEN_EPUB) $(FINAL)/docs/vonLaszewski-$(NAME).epub

authors:
	$(HOME)/bin/authors.py > $(HOME)/chapters/authors.md

clean:
	rm -rf dest

include ./Makefile.bibtex
