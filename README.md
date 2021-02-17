# lindertree

A lsystem generator and interpreter.

## Features

- Standard 2D turtle interpretation of produced lsystems.
- Simple rule specifications using string to symbols parsing.
- [TODO] Parametric rule specification and turtle interpretation.
- [TODO] Command line interface.
- [TODO] Load axioms and rules from file.
- [TODO] Speed optimization using a fast gui.

## Usage

See `example.py`.

## Format

### Symbols

A valid symbol is composed of one alphabetic character or one of `[`, `]`, `+`, `-`.

### Turtle interpreted symbols

- `F` : draw forward.
- `f` : move forward without drawing.
- `+` : rotate left.
- `-` : rotate right.
- `[` : start branch (push turtle state on the stack).
- `]` : end branch (pop turtle state from the stack).
- `X` : standard non-interpreted symbol used for developmental control
