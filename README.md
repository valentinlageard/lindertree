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

A valid symbol is composed of one alphabetic character or one of `[`, `]`, `+`, `-`, `!`.

### Turtle interpreted symbols

- `F` : draw forward.
- `f` : move forward without drawing.
- `+` : rotate left.
- `-` : rotate right.
- `[` : start branch (push turtle state on the stack).
- `]` : end branch (pop turtle state from the stack).
- `X` : standard non-interpreted symbol used for developmental control

### Parametric symbols

A valid parametric symbol is composed of one alphabetic character or one of `[`, `]`, `+`, `-`, `!`. It may be followed by non-nested parentheses containing the parameters separated by `,`. A parameter must be a valid identifier of the form `[A-Za-z]+[A-Za-z\d]*` or a valid integer or float (with a `.` before decimals). Note that the parser automatically convert integers to floats. For now, there is no input validation, so beware !

### Turtle interpreted parametric symbols

- `F(x)` : draw `x` pixels forward.
- `f(x)` : move `x` pixels forward without drawing.
- `+(x)` : rotate of `x` angle (`x > 0` means counterclockwise, `x < 0` means clockwise).
- `!(x)` : set width to `x` pixels.
