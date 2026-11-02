# termanat

Discover and learn anatomy inside your terminal.

`termanat` is a TUI (terminal user interface) for exploring the human body,
drawn in ASCII art, at first-year medicine level (PASS / L.AS in France), in
English and French. It covers five systems: skeleton, muscles, digestive
system, circulation and nervous system.

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
uv tool install git+https://github.com/etiennebonnafoux/termanat@v0.2.0
```

Then run:

```bash
termanat
```

Or try it without installing:

```bash
uvx --from git+https://github.com/etiennebonnafoux/termanat@v0.2.0 termanat
```

## Usage

- **Systems** (`s`): switch between skeleton, muscles, digestive system,
  circulation and nervous system, or click the bar under the title.
- **Explore** (`e`): move through the list with the arrow keys, or click a
  structure on the figure. It lights up and you get its Latin name, type and a
  detailed description (landmarks, joints, attachments, innervation, course,
  relations, blood supply, clinical notes...) and a fun fact. Press `Tab` to
  move to the info panel and scroll it with the arrow keys.
- **Quiz** (`t`): a structure of the current system is highlighted; press
  `1`-`4` (or click) to name it, then `Enter` or `n` for the next question.
- `l` switches between English and French.
- `q` quits.

The language follows your system locale (`LANG`). To force it:

```bash
termanat --lang fr
```

To open a given system first:

```bash
termanat --system nervous
```

The French version uses the current international nomenclature (fibula,
patella, ulna...) with the former names (péroné, rotule, cubitus...) shown
alongside.

Every figure is shown from the front in anatomical position (palms forward),
so the left side of the screen is the body's right side.

## Planned

- More systems (respiratory, urinary, lymphatic...)
- More detailed views (skull, hand, foot, spine, heart)
- Quiz on landmarks and innervation

## Development

```bash
uv sync
uv run termanat
uv run pytest
```

Each body system lives in `src/termanat/systems/<id>/`: an ASCII figure with a
mask saying which structure each character belongs to (`art.py`), and the texts
in each language (`texts_en.py`, `texts_fr.py`). `src/termanat/model.py`
describes the format, and `validate_system` checks it (run by the tests).

To release a new version, bump `version` in `pyproject.toml`, update
`CHANGELOG.md`, then push a matching tag (for example `v0.2.0`). The release
workflow builds the package and publishes a GitHub release.

## License

[MIT](LICENSE)
