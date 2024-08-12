# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

livehtml:
	sphinx-autobuild --open-browser "$(SOURCEDIR)" "$(BUILDDIR)/livehtml" $(SPHINXOPTS) $(O)

# Install build requirements in the current environment

develop:
	python -m pip uninstall -y -qq gurobi-sphinxtheme
	python -m pip install -r requirements.txt
	python -m pip install sphinx-autobuild==2024.02.04
	python -m pip install pre-commit
	pre-commit install

# This target is similar to how the PDF is built on RTD. `make latexpdf` is not the same and fails.
# Since latexmk currently always emits exit code 12, I've whitelisted that. Subsequently we check for the creation of
# the PDF file.
pdf:
	python -m sphinx -T -b latex -d _build/doctrees -D language=en source build/pdf

	cd build/pdf && \
	latexmk -r latexmkrc -pdf -f -dvi- -ps- -jobname=gurobi-optimization-gurobi-ai-modeling -interaction=nonstopmode || \
	{ exitcode=$$?; if [ "$$exitcode" -ne 12 ]; then exit $$exitcode; fi; }

	@if [ ! -f build/pdf/gurobi-optimization-gurobi-ai-modeling.pdf ]; then \
	    echo "Error: PDF was not created!"; \
	    exit 1; \
	else \
	    echo "PDF successfully created: build/pdf/gurobi-optimization-gurobi-ai-modeling.pdf"; \
	fi

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
