gh-pages:
	git checkout gh-pages
	rm -rf *
	git checkout master doc
	touch .nojekyll
	git reset HEAD
	make -C doc html
	mv -fv doc/build/html/* ./
	rm -rf doc
	git add .
	git commit -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`"
	git push origin gh-pages
	git checkout master