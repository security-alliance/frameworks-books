# OpSec While Traveling

LaTeX pocket edition of the Security Alliance travel security guide,
sized to the printed mini-book: 70 x 110 mm.

The reading order is the same three-phase loop as the original:

1. Before traveling.
2. While traveling.
3. Returning home.
4. Extra controls for high-profile targets.

The manuscript lives in `editorial/`. It follows the printed v1.0
companion and the live `opsec/travel` pages. Website-only further
reading is not in the book.

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

- `output/pdf/opsec-while-traveling.pdf`
- `output/opsec-while-traveling-latex-source.zip`
