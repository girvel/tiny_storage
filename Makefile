step: version-update git-step

git-step:
	git add .
	git commit
	git push

version-update:
	./.toolkit/increment_version
