# Security Alliance mini-books

LaTeX sources for pocket editions of Security Alliance frameworks.
Trim size is 70 x 110 mm, matching the printed travel OpSec mini-book.

## Books

| Directory | Title |
| --- | --- |
| [`physical/`](physical/) | Physical Security pocket guide |

Travel OpSec will live in `opsec/` once the LaTeX edition is in.

## Build

Each book directory is self-contained. Podman or Docker is enough:

```sh
cd physical
./container/build.sh
```

The PDF and a source zip land in that book's `output/` directory.
See the book README for host-toolchain builds and editorial notes.

## License

Each book carries its own `LICENSE.md`. Framework text remains copyright
Security Alliance and contributors. Pocket-edition arrangement is
Creative Commons Attribution-ShareAlike 4.0 unless a book says otherwise.
