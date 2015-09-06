gh-pages:
	git checkout gh-pages
	rm -rf doc
	git checkout master doc
	git reset HEAD
	cd doc
	make html
	mv -fv build/html/* ../
	cd ..
	rm -rf doc
	git add -A
	git commit -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`"
	git push origin gh-pages
	git checkout master