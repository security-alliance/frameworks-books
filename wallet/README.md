# Wallet Security Pocket Guide

Print companion for the Security Alliance Wallet Security framework,
sized to the same 70 x 110 mm trim as the travel OpSec mini-book.

This edition is rewritten for print. It is for the person who signs:
custody, hot and cold, hardware, seed handling, verification, and
approvals. Website "further reading," in-progress stubs (software
wallets, hardware wallets as a standalone page, signing schemes),
and the Safe / Squads operator walkthroughs are not in the book.
Those last two live in the Protocol Multisig companion and on the
site.

The reading order:

1. Who holds the keys.
2. Split spend from savings.
3. Put the pile on hardware.
4. Treat the seed as the wallet.
5. Never sign blind.
6. Cap what a contract can pull.
7. Add people when one key is too much.
8. Treat AA, 7702, and TEEs as extra surface.
9. If it breaks, move, do not reuse.

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

- Person who signs. Protocol treasury runbooks stay in `multisig/`.
- Stub pages stay on the website until they are real pages.
- Dollar figures, seed splits, and slippage ranges in the source are
  examples, not policy.
- Human safety takes precedence over asset recovery.

## Output

- `output/pdf/wallet-security-pocket-guide.pdf`
- `output/wallet-security-pocket-guide-latex-source.zip`
