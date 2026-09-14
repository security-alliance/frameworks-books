SHELL := /bin/bash

FRAMEWORKS_REPO ?= ../frameworks
REF ?= develop
BASE_URL ?= https://frameworks.securityalliance.dev
USE_GENERATED ?= 0
PYTHON ?= python3
PANDOC ?= pandoc
LATEXMK ?= latexmk
LATEXMK_ENGINE ?= -lualatex
PDFTOPPM ?= pdftoppm

.PHONY: all sync pdf verify render package container clean distclean

all: pdf verify

sync:
	mkdir -p generated
	$(PYTHON) scripts/sync_framework.py \
		--repo "$(FRAMEWORKS_REPO)" \
		--ref "$(REF)" \
		--base-url "$(BASE_URL)" \
		--config config/chapters.json \
		--output generated/framework-content.md \
		--meta-output generated/source-meta.tex
	$(PANDOC) generated/framework-content.md \
		--from=markdown+raw_tex-smart \
		--to=latex \
		--top-level-division=chapter \
		--wrap=none \
		--output=generated/framework-content.tex

pdf:
	test -s generated/source-meta.tex
	mkdir -p build output/pdf
	$(LATEXMK) $(LATEXMK_ENGINE) -interaction=nonstopmode -halt-on-error -file-line-error \
		-outdir=build book.tex
	cp build/book.pdf output/pdf/physical-security-pocket-guide.pdf

verify: pdf
	$(PYTHON) scripts/verify_pdf.py output/pdf/physical-security-pocket-guide.pdf

render: pdf
	mkdir -p tmp/rendered
	$(PDFTOPPM) \
		-png -r 150 output/pdf/physical-security-pocket-guide.pdf tmp/rendered/page

package: verify
	mkdir -p output
	zip -FSqr output/physical-security-pocket-guide-latex-source.zip \
		book.tex style.tex Makefile README.md LICENSE.md Containerfile .dockerignore \
		assets config container editorial scripts generated tests .github \
		-x '*/__pycache__/*'

container:
	./container/build.sh

clean:
	rm -rf build output tmp

distclean: clean
	rm -f generated/framework-content.md \
		generated/framework-content.tex generated/source-meta.tex
