# Imagery

- `textures.html` + `render_textures.js`: generated "brand light" textures (fibre burst, light trails, neon tunnel,
  ribbon X, data wave, horizon grid) in the NEXA palette. No licence needed. `make imagery` re-renders them.
- `grade.py`: the Super Blue grade used for photography (matches the brandbook's in-situ pages).
  `python3 grade.py <in> <out>`.

The `ph-*.jpg` photos in `library/src/img/` are placeholders: Pexels photos reused from the Sonim brand system,
run through `grade.py`. Replace them with licensed NEXA photography, graded the same way.
