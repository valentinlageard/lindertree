# lindertree

A lsystem generator and interpreter.

## Features

- Standard 2D turtle interpretation of produced lsystems.
- Simple rule specifications using string to symbols parsing.
- Parametric rule specification and turtle interpretation.
- Stochastic rules, parameters and drawing deviation.
- [TODO] Command line interface.
- [TODO] Load axioms and rules from file.
- [TODO] Speed optimization using a fast gui.

## Usage

See `example.py` and `example_parametric.py`.

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

A valid parametric symbol is composed of one alphabetic character or one of `[`, `]`, `+`, `-`, `!`. It may be followed by non-nested parentheses containing the parameters separated by `,`. A parameter must be a valid identifier of the form `[A-Za-z]+[A-Za-z\d]*` or a valid integer or float (with a `.` before decimals). Note that the parser automatically convert integers to floats. For now, there is no input validation, so beware ! You may also use `+`, `-`, `/` and `*` for operations in rules. To compute parameters on the fly, we use `eval()` so beware again !

### Turtle interpreted parametric symbols

- `F(x)` : draw `x` pixels forward.
- `T(x, y)` : draw `x` pixels forward with width `y`.
- `f(x)` : move `x` pixels forward without drawing.
- `+(x)` : rotate of `x` angle (`x > 0` means counterclockwise, `x < 0` means clockwise).
- `!(x)` : set width to `x` pixels.

### Random

3 kinds of random are provided :
- Stochastic rules with the `StochasticRule` class.
- Stochastic parameters with `^` for polar random [0,1] and `~` for bipolar random [-1,1]
- Stochastic drawing with `distance_dev` and `angle_dev` : (proportional_offset, proportional_scale, uniform_offset, uniform_range).

### Examples

`example.py` :
- Axiom : $X$
- Rules :
  - $F \rightarrow FF$
  - $X \rightarrow F[+X][-X]FX$

`example_parametric.py` :
- Axiom : $!(1)F(5)X$
- Constants : $w=5, e=1.6, a=1.1$
- Rules :
  - $!(x) \rightarrow !(x*w)$
  - $F(x) \rightarrow F(x*e)$
  - $+(x) \rightarrow +(x*a)$
  - $-(x) \rightarrow -(x*a)$
  - $X \rightarrow!(1)[+(25)F(2)X]F(2)[-(25)F(2)X]!(1)F(5)X$
