# Physical Security Pocket Guide

Print companion for the Security Alliance Physical Security framework,
sized to the same 70 x 110 mm trim as the travel OpSec mini-book.

This edition is rewritten for print. It follows the reviewed Coercion &
Duress core. Website "further reading," in-progress stubs (facility,
counter-surveillance, supply chain), and MDX navigation are not in the
book.

The reading order:

1. See the threat.
2. See how you get picked.
3. Design keys so one coerced person is not enough.
4. Shrink what follows people around.
5. If it happens, protect life first.
6. Afterward, support people and rebuild from clean material.

## Build

Only Podman or Docker is required on the host. The manuscript lives in
`editorial/`. `generated/source-meta.tex` records the framework snapshot
this cut was based on.

```sh
./container/build.sh
```

Set `CONTAINER_ENGINE=docker` to force Docker. Podman is selected first
when both exist. See `container/README.md` for the execution model.

To refresh snapshot metadata from a local Frameworks checkout (does not
replace the print manuscript):

```sh
FRAMEWORKS_REPO=/absolute/path/to/frameworks ./container/build.sh sync
FRAMEWORKS_REPO=/absolute/path/to/frameworks ./container/build.sh
```

Host toolchain, if you are not using the container:

```sh
make pdf
make verify
make package
```

Latin Modern (GUST) and Gentium Book (SIL OFL) are bundled under
`assets/fonts/`.

## Editorial boundaries

- Coercion & Duress is the mature core. That is the book.
- Facility & Perimeter, Physical Counter-Surveillance, and Supply Chain
  Physical Integrity stay on the website until they are real pages.
- Dollar figures and wallet splits in the source are examples, not
  policy.
- Human safety takes precedence over asset recovery.

## Output

- `output/pdf/physical-security-pocket-guide.pdf`
- `output/physical-security-pocket-guide-latex-source.zip`
