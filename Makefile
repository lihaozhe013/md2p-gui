default: run
run:
	md-to-pdf --stylesheet github-markdown.css --body-class markdown-body input_system_design.md
format:
	prettier . --write