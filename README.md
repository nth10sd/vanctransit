[![codecov](https://codecov.io/gh/nth10sd/vanctransit/graph/badge.svg?token=H94BWJ1SOY)](https://codecov.io/gh/nth10sd/vanctransit)

# README

This demo was tested with Python 3.11 - 3.12.

## Prerequisites

Ensure Python is installed, especially on Windows.

Install Rust by following the [instructions on their website](https://www.rust-lang.org/).

After Rust installation,
```
rustup --version
```

You should have at least the following output:
```
rustup 1.26.0 (5af9b9484 2023-04-05)
info: This is the version for the rustup toolchain manager, not the rustc compiler.
info: The currently active `rustc` version is `rustc 1.74.0 (79e9716c9 2023-11-13)`
```

Ensure you do not have any existing `venv` at `~/venv-vanctransit`.

Create a new Python 3.11 (install it beforehand) virtual environment using `venv` and switch to it.

Linux or macOS:
```
python3.11 -u -m venv --upgrade-deps ~/venv-vanctransit ; . ~/venv-vanctransit/bin/activate ;
```

Windows:
```
pushd ~ ; python -u -m venv --upgrade-deps venv-vanctransit ; popd ; Set-ExecutionPolicy Unrestricted -Scope Process; ~/venv-vanctransit/Scripts/Activate.ps1 ; ~/venv-vanctransit/Scripts/Activate.ps1 ;
```

Install [cargo-binstall](https://github.com/cargo-bins/cargo-binstall).

Make sure Cargo is usable and use `cargo-binstall` to install `cargo-tarpaulin` (code coverage).
```
cargo binstall -y cargo-tarpaulin
```

Clone the repository and cd into it (replace `<repo>` with desired location):
```
$ git clone <repo> ; cd <repo> ;
```

## maturin-related (Rust)

Development command for Linux and Windows:
```
cargo clippy --all-targets -- -D warnings ; python -u -m pip install --upgrade pip ; pip install --upgrade -r requirements.txt ; cargo tarpaulin --all-targets --count --exclude-files=target/* --engine=llvm --fail-under=80 --ignored --no-dead-code --out=stdout --skip-clean --target-dir=target/tarpaulin-target/ ; maturin develop --release --strip ;
```

Development command for macOS (which uses `zsh`):
```
cargo clippy --all-targets -- -D warnings ; python -u -m pip install --upgrade pip ; pip install --upgrade -r requirements.txt ; setopt +o nomatch ; cargo tarpaulin --all-targets --count --exclude-files=target/* --engine=llvm --fail-under=80 --ignored --no-dead-code --out=stdout --skip-clean --target-dir=target/tarpaulin-target/ ; setopt -o nomatch ; maturin develop --release ;
```

Switch `maturin develop` for debug Rust code with symbols if needed.

## Run tools on your package

(All commands here must be run within the `venv`, in the main repository directory - not any subfolders)

For comprehensive tests and all linters:
```
python -u -m pytest --cov --mypy --pylint --ruff --ruff-format
```

## Running

Run the module using:
```
python -u -m vanctransit
```

## Documentation generation via Sphinx (Linux-only)

* Change into `docs/` folder: `cd docs/`
* Run generation command - you **must** first be in the `docs/` directory: `./gen-sphinx-html.sh`
* Your generated HTML files are now in `docs/build/html/` directory
* Open `index.html` to start
