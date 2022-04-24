OUTPUTDIR=reports
GITHUB_PAGES_BRANCH=gh-pages

publish:
	# echo reports.mne.tools > $(OUTPUTDIR)/CNAME
	touch $(OUTPUTDIR)/.nojekyll
	ghp-import -m "New reports" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)
