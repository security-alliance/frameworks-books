# Security Frameworks Pocket Showcase

Print companion for the Security Alliance frameworks, sized to the
same 70 x 110 mm trim as the travel OpSec mini-book.

This edition is a 101. It takes the most developed public frameworks
and prints the takeaway, a few insights, and the first moves. It is
not a dump of the website. Dedicated pocket books still own the deep
cuts: physical coercion, travel OpSec, protocol multisig, and the
person who signs.

The reading order:

1. How you live (OpSec, physical, privacy, community, hiring).
2. How money moves (wallet, protocol multisig, treasury).
3. How you ship and run (DevSecOps, supply chain, infra, monitoring, AI).
4. What you do when it breaks (incident, Safe Harbor, testing).
5. How the rest stays alive (awareness).

Dev-only stubs, tool catalogs, and unfinished pages stay on the site.

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
FRAMEWORKS_REPO=/absolute/path/to/vocs ./container/build.sh sync
FRAMEWORKS_REPO=/absolute/path/to/vocs ./container/build.sh
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

- Public, reviewed frameworks only. Dev-gated pages stay off the page.
- Dedicated companions are not restated here. This book points at them.
- Dollar figures and thresholds in the source are examples, not policy.
- Human safety takes precedence over asset recovery.

## Output

- `output/pdf/security-frameworks-pocket-showcase.pdf`
- `output/security-frameworks-pocket-showcase-latex-source.zip`
