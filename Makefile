step: version-update git-step

git-step:
	git add .
	git commit
	git push origin `git rev-parse --abbrev-ref HEAD`

version-update:
	./.toolkit/increment_version
