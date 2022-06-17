fast: table
	cd book; make pdf

clean:
	cd book; rm -rf dest

all: clean table action
	cd book; make pdf

view:
	gopen book/dest/vonLaszewski-reu2022.pdf

action:
	@echo "# Lines contributed" > action.md
	@echo >> action.md
	@echo "\`\`\`" >> action.md
	@cms git contribution | fgrep -v "# Timer" >> action.md
	@echo "\`\`\`" >> action.md
	@echo >> action.md

publish: all
	cd ../pub/docs; git commit -m "update reu2022" vonLaszewski-reu2022.pdf vonLaszewski-reu2022.epub; git push

issues:
	cd .. ; cms git issues --repo=reu --refresh

table:
	python bin/generate-compare-table.py