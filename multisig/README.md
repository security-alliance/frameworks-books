# Protocol Multisig

LaTeX pocket edition of the Security Alliance Multisig for
Protocols framework, sized to the printed mini-book: 70 x 110 mm.

The reading order is the life of a signature:

1. What actually fails.
2. Map the powers, then split the sets.
3. Delay what can wait.
4. Join, then verify before you sign.
5. Survive loss, keep the set alive.

The manuscript lives in `editorial/`. It is a rewrite for print,
not a dump of the website. Safe is treated as the default stack.
Squads and other clients keep the same checks.

## Build

Podman or Docker is enough:

```sh
./container/build.sh
```

Set `CONTAINER_ENGINE=docker` to force Docker. See `container/README.md`.

Host toolchain:

```sh
make pdf
make verify
make package
```

## Output

- `output/pdf/protocol-multisig.pdf`
- `output/protocol-multisig-latex-source.zip`
