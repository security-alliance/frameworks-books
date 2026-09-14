SHELL := /bin/bash

FRAMEWORKS_REPO ?= ../../vocs
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
	cp build/book.pdf output/pdf/opsec-while-traveling.pdf

verify: pdf
	$(PYTHON) scripts/verify_pdf.py output/pdf/opsec-while-traveling.pdf

render: pdf
	mkdir -p tmp/rendered
	$(PDFTOPPM) \
		-png -r 150 output/pdf/opsec-while-traveling.pdf tmp/rendered/page

package: verify
	mkdir -p output
	zip -FSqr output/opsec-while-traveling-latex-source.zip \
		book.tex style.tex Makefile README.md LICENSE.md Containerfile .dockerignore \
		assets config container editorial scripts generated tests common \
		-x '*/__pycache__/*'

container:
	./container/build.sh

clean:
	rm -rf build output tmp

distclean: clean
	rm -f generated/framework-content.md \
		generated/framework-content.tex generated/source-meta.tex
