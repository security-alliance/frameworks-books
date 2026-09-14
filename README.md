# Security Alliance mini-books

LaTeX sources for pocket editions of Security Alliance frameworks.
Trim size is 70 x 110 mm, matching the printed travel OpSec mini-book.
Shared cover and layout live in [`common/pocket.tex`](common/pocket.tex).
Look there before changing type, trim, or the night cover.

## Books

| Directory | Title |
| --- | --- |
| [`physical/`](physical/) | Physical Security pocket guide |
| [`opsec/`](opsec/) | OpSec While Traveling |
| [`multisig/`](multisig/) | Protocol Multisig |
| [`wallet/`](wallet/) | Wallet Security pocket guide |

## Build

Each book directory is self-contained. Podman or Docker is enough:

```sh
cd physical   # or: cd opsec  /  cd multisig  /  cd wallet
./container/build.sh
```

The PDF and a source zip land in that book's `output/` directory.
See the book README for host-toolchain builds and editorial notes.

## License

Each book carries its own `LICENSE.md`. Framework text remains copyright
Security Alliance and contributors. Pocket-edition arrangement is
Creative Commons Attribution-ShareAlike 4.0 unless a book says otherwise.
