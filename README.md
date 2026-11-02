# termanat

Discover and learn anatomy inside your terminal.

`termanat` is a TUI (terminal user interface) for exploring the human body,
drawn in ASCII art. Version 0.1.0 covers the skeleton.

```
              .-"""""""""-.
             /             \
             |  .-.   .-.  |
             |  '-'   '-'  |
             \      ^      /
              \,,,,,,,,,,,/
               |'''''''''|
                \_______/
                    #
       .__.--------'#'--------.__.
       (__     ===\_|_/===     __)
       | |   =====\_|_/=====   | |
       | |  ======\_|_/======  | |
       | |   =====\_|_/=====   | |
       | |    ====\_v_/====    | |
       | |     ==\  #  /==     | |
       |_|          #          |_|
       / \          #          / \
       | |      _.-'#'-._      | |
       | |     /  .---.  \     | |
       | |     \  \ # /  /     | |
       | |      '._\v/_.'      | |
       {=}     | |     | |     {=}
      {###}    | |     | |    {###}
      |||||    | |     | |    |||||
      '''''    | |     | |    '''''
               | |     | |
               | |     | |
               |_|     |_|
               (_)     (_)
               | |     | |
               | |     | |
               | |     | |
               | |     | |
               |_|     |_|
              /###\   /###\
             (_____) (_____)
```

## Install

With [uv](https://docs.astral.sh/uv/):

```bash
uv tool install git+https://github.com/etiennebonnafoux/termanat@v0.1.0
```

Then run:

```bash
termanat
```

Or try it without installing:

```bash
uvx --from git+https://github.com/etiennebonnafoux/termanat@v0.1.0 termanat
```

## Usage

- **Explore** (`e`): move through the list with the arrow keys, or click a bone
  on the skeleton. The bone lights up and you get its Latin name, where it is,
  how many you have, and a fun fact.
- **Quiz** (`t`): a bone is highlighted; press `1`-`4` (or click) to name it,
  then `Enter` or `n` for the next question.
- `q` quits.

The skeleton is shown from the front in anatomical position (palms forward),
so the left side of the screen is the body's right side.

## Planned

- Organs, muscles and other body systems
- More detailed views (skull, hand, foot, spine)

## Development

```bash
uv sync
uv run termanat
uv run pytest
```

To release a new version, bump `version` in `pyproject.toml`, update
`CHANGELOG.md`, then push a matching tag (for example `v0.2.0`). The release
workflow builds the package and publishes a GitHub release.

## License

[MIT](LICENSE)
