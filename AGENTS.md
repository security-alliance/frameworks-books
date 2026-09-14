# Mini-book playbook

Pocket editions of Security Alliance frameworks. Trim matches the
printed travel OpSec mini-book. Each book is a directory under this
repo. Do not invent a third layout.

Repo: https://github.com/security-alliance/frameworks-books
Live site: https://frameworks.securityalliance.dev
MDX source (local): `../../vocs/docs/pages/` from a book directory when
this checkout sits at `frameworks/books/`.

## Books

| Dir | Title | Voice |
| --- | --- | --- |
| `physical/` | Physical Security pocket guide | Rewritten for print. Coercion & Duress only. Stubs stay off the page. |
| `opsec/` | OpSec While Traveling | Follow the printed v1.0 companion. Update facts from live `opsec/travel` without changing the three-phase spine. |
| `multisig/` | Protocol Multisig | Rewritten for print from `multisig-for-protocols`. Signer-first. Safe is the default stack. Spine: separate / delay / verify. |

Start a new book by copying an existing book directory. Do not design a
new cover or trim. Identity lives in that book's `style.tex`.

## Trim, type, color

Hard numbers. Copy them.

- Paper: 70 x 110 mm = `198bp` x `311.754bp`
- Margins: inner/outer 9.5 mm, top/bottom 13 mm, headheight 8 pt, headsep 4.5 mm, footskip 8 mm
- Body: Gentium Book 9 / 11.4 pt, stretch 1.12, ragged right, no parindent, parskip 2.1 mm
- Sans / mono: Latin Modern (`lmsans10-*`, `lmmono10-*`) from `assets/fonts/`
- Font licenses travel with the files: Gentium SIL OFL, Latin Modern GUST
- Colors: Night `#121A26`, ShieldBlue `#21409A`, SignalRed `#ED3C3B`, GuildRed `#9B2B2B`, SafetyOrange `#F26A2E`, Quiet `#6B7280`, Concrete `#ECEBE7`
- Engine: LuaLaTeX via `latexmk -lualatex`
- Class: `\documentclass[10pt,twoside,openany]{book}`
- No section numbers: `\setcounter{secnumdepth}{-1}`
- `\let\cleardoublepage\clearpage` so twoside does not insert blank versos

Running header: even pages `TITLE -- vX.X` in Quiet 6 pt. Odd pages
`\leftmark` (chapter). Footer: page number 8 pt, outer corners.
No header/footer rules.

## Directory layout

Shared, read before every build:

```
common/pocket.tex        % trim, type, color, keepblock, night cover
```

Every book directory:

```
book.tex                 % inputs only
style.tex                % identity macros, then \input{common/pocket.tex}
common -> ../common      % symlink; container also bind-mounts this
editorial/               % the manuscript. This is the book.
generated/source-meta.tex
config/chapters.json     % MDX paths for sync metadata, not the printed body
assets/fonts/
container/               % anonymous Podman/Docker wrapper
scripts/sync_framework.py
scripts/verify_pdf.py
Makefile
Containerfile
LICENSE.md
README.md
tests/                   % wrapper tests, not layout tests
```

Gitignores `tmp/` and `build/`. Commit `output/` PDFs and source zips.

`generated/framework-content.md` / `.tex` are optional sync artifacts.
The printed body is `editorial/*.tex`. Pandoc of live MDX is a research
aid, not the book. Website nav, further-reading, and in-progress stubs
do not belong in print.

## How to start another book

1. Copy an existing book directory. Rename it. Short name: `wallet/`,
   `dns/`, not `wallet-security-pocket-guide/`. Keep the `common` symlink.
2. Change, in this order:
   - `container/build.sh` image tag (`seal-<name>-book:anonymous-v1`)
   - `Containerfile` LABEL title + source URL (this repo)
   - `style.tex` `\BookTitleA` / `\BookTitleB` / `\BookVersion` /
     `\BookSubtitle` / `\BookRunning` / `\BookPdfTitle` / `\BookPdfSubject`
   - `Makefile` PDF and zip names
   - `scripts/verify_pdf.py` required strings and minimum page count
   - `config/chapters.json` MDX paths
   - `generated/source-meta.tex` snapshot
   - `LICENSE.md` (do not copy physical's CC-BY-SA onto a book whose print
     license is all-rights-reserved, or the reverse)
   - wrapper autodetect path (`docs/pages/<framework>/...`)
3. Replace `editorial/` with that book's spine. Keep `orgs.tex`,
   `frontmatter.tex`, `conclusion.tex`, `acknowledgments.tex`,
   `source-and-license.tex` as the sandwich.
4. Add a row to the root README and a job in `.github/workflows/build.yml`.
5. Build in the container before claiming done.

Cover, flyleaf, and interior title come from `common/pocket.tex`. Do not
fork them in the book. Night field, SEAL in ShieldBlue, white title,
`feat. THE RED GUILD` in GuildRed. Publisher line is Security Alliance.

## `book.tex` order

Fixed front:

1. `\coverpage` (page 1, empty pagestyle)
2. arabic numbering, `\setcounter{page}{2}`
3. `\flyleaf` then `\interiorTitle`
4. `\pagestyle{fronthead}`
5. TOC
6. `editorial/orgs.tex` (ABOUT blocks)
7. `editorial/frontmatter.tex` (about this book, donate, disclaimers)

Then chapters. Then conclusion, acknowledgments, source-and-license.

Cover, flyleaf, interior title stay empty-pagestyle. Do not put the
TOC or ABOUT on the title leaf.

## Page-fit contract

70 mm is intolerant. These rules were learned by splitting ABOUT,
donate URLs, and acknowledgments.

**Designed blocks stay whole.** ABOUT (Red Guild + SEAL), donate,
human-safety callout, field cards, acknowledgments, license colophon.
Use `\keepblock{...}`.

`\keepblock` must ship an unbreakable box:

```tex
\newcommand{\keepblock}[1]{%
  \par
  \setbox0=\vbox{\hsize=\linewidth\relax #1}%
  \Needspace{\dimexpr\ht0+\dp0+2mm\relax}%
  \noindent\box0
  \par
}
```

Never `\unvbox`. Unpacking lets TeX break the block again.
If the box is taller than the live area, shrink type and parskip until
it fits. Overflow into the footer is a bug even when verify_pdf passes.

Load `needspace` before `titlesec` uses `\Needspace` in `\titleformat`.

**URLs.** Never hyphenate. `\plainurl{example.org/path}` for short
ones (`\ttfamily\mbox{...}`). Long ones: `\url{...}` with `xurl` so
breaks happen at slashes only. A donate link that becomes
`liance.org/donate` on the next page is a fail.

**Headings.** `\Needspace` on chapter (28 mm), section (20 mm),
subsection (16 mm). A heading must not sit on a leftover line above a
block that jumped.

**No extra `\clearpage`** before ABOUT, acks, or license "to be safe".
That is how you get a blank page 8 with only a header.

**Check with eyes, not only verify_pdf.** After a layout change:

```sh
pdftotext -layout -f N -l M output/pdf/<name>.pdf -
```

Look for: blank pages, last word of a block on the next page, URL
split mid-token, heading stranded, page number colliding with the last
line of a keepblock.

Footnote marks split `pdftotext` / pypdf extraction. Do not require a
phrase that a footnote sits inside (`juice jacking` failed that way).
Require a nearby stable token (`USBGuard`).

## Editorial rules

- Print is a companion, not a dump of the website.
- Do not invent controls to fill unfinished framework pages. Point at
  the site or omit.
- Do not replace a printed book's structure with the live MDX IA.
  Update facts (new attacks, tool names, "delay posts 1-2 days")
  inside the existing spine.
- A pocket book must stand alone. Do not replace a working section
  with "see the website" unless the printed edition already did that.
- Human safety beats asset recovery. Physical book: life first.
- Dollar figures and wallet splits in source are examples, not policy.
- Cover is SEAL first. Guild is the cover feat line only. ABOUT pages may
  still list both; SEAL first unless that book's print edition already
  reversed them and you are matching it on purpose.
- Acknowledgments: real names from Spotlight Zone / the printed
  colophon, not a travel-book dump pasted into another title.
- Cover illustration (Constanza Tarantelli on the travel book) is not
  in the TeX tree. Do not fake it.

Voice: short sentences, second person, concrete verbs. No "evolving
landscape". No em dashes. Ragged-right 9 pt already punishes long
clauses.

## Build

Host needs only Podman or Docker:

```sh
cd <book>
./container/build.sh
```

Wrapper picks Podman first. `CONTAINER_ENGINE=docker` to force.
Image holds the toolchain. Source bind-mounts at runtime. Runtime
network is off. Registry creds stay off the container.

`make pdf && make verify && make package` inside the container.
`pdf` requires `generated/source-meta.tex`. Sync from a frameworks
checkout only when refreshing snapshot metadata:

```sh
FRAMEWORKS_REPO=/absolute/path/to/vocs ./container/build.sh sync
```

`FRAMEWORKS_REPO` must contain `docs/pages/...` as in `chapters.json`.
From this repo that is usually the `vocs/` checkout, not `frameworks/`
root.

Verify must fail on: wrong page size, too-short book, missing
title/spine phrases. Blank pages in `textless_pages` are a smell;
cover/flyleaf should still extract the byline.

## CI

Root `.github/workflows/build.yml` runs each book's wrapper tests
then `./<book>/container/build.sh` with Docker. Nested
`<book>/.github/` is leftover from the old frameworks monorepo path
(`publishing/...`) and is not what GitHub Actions reads.

## Common failures

| Symptom | Cause | Fix |
| --- | --- | --- |
| ABOUT splits after "Phishing" | `\unvbox` or minipage overflow | `\box0` keepblock + shrink |
| `liance.org/donate` on next page | `\url` hyphenation | `\plainurl` or slash-only breaks |
| Heading then leftover URL | block jumped, heading did not | put heading inside keepblock or Needspace more |
| Blank page after TOC | extra `\clearpage` | delete it |
| keepblock collides with page number | box taller than live area | shrink 7–7.5 pt / tighter parskip |
| verify wants a phrase pypdf cannot see | footnote in the middle of the phrase | require a different token |
| Image rebuild every book | LABEL/tag change is enough; RUN layer can stay | keep Containerfile RUN identical |

## License

Each book ships its own `LICENSE.md`. Physical pocket arrangement is
CC BY-SA 4.0 on top of Security Frameworks copyright. Travel OpSec
print edition is all-rights-reserved for sale of the physical copy.
Do not unify them.
