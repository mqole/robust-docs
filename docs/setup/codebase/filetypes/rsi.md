---
sidebar_position: 1
---
# Robust Station Image

The **RSI** (Robust Station Image) format is  a flexible, open, and readable way to define icons inside sprite sheets in the same vein as the BYOND `.dmi` format. An RSI is considered an "icon", and it can contain "states" which are subsections of this icon. These states can define custom flags, animations, and directional icons out of the box.

An RSI is a folder with a name that ends in `.rsi`, and contains a `meta.json` and one or more PNG files according to the names of states.

The image metadata (what defines states, animations, etc.) is stored in the `meta.json` file as JSON. The actual sprites are stored in sprite sheets as PNG files in the folder. Each unique state corresponds to a sprite sheet with the same name.

## JSON

The root of the JSON file contains the following values:

Key | Meaning
--- | -------
`version` | An integer corresponding to the RSI format version. This can be used to identify what version an RSI is, and allow the implementation to correctly enable backwards compatibility modes when needed.
`size` | The dimensions of the sprites inside the RSI, stored as an associative list of `{x: ?, y: ?}`. This is _not_ the size of the PNG files that store the sprite sheet. It is used to correctly crop individual sprites out of the sprite sheet files.
`states` | A list of _states_ that store the actual meat of the RSI, see below.
`license` | **Required.** A valid [SPDX License Identifier](https://spdx.org/licenses/) applying to this work.
`copyright` | **Required.** Other arbitrary copyright info such as name, source, etc.
`load` | Special loading parameters that will change how the sprites are interpreted by the engine.
`metaAtlas` | Boolean that indicates whether the sprite is added together to a larger atlas at load. Enabled by default, this should be disabled for large RSIs.

### States

A state is a container of metadata for a specific sprite sheet. Each state stores data related to their same-named sprite sheet, such as animation timing or directional information.

Each state must have an accompanying sprite sheet, and that sprite sheet must be the name of the state. For example, a state with name "hello" would be stored as a file named `hello.png`.

States have one field that can be used to distinguish them:

Key | Meaning
--- | -------
`name` | The name of the state. Can only contain lowercase alphabetic, numerical, and some special (`_-`) characters.

States cannot have the same identifying value. Two states with the same name may not exist.

Other than the identifier, a state has three other fields in relation to the actual sprites as seen in game:

Key | Meaning
--- | -------
`flags` | An optional associative list of `key: object` for defining extra data. There is currently no usage yet.
`directions` | A number corresponding to the amount of directions a state has. This should be a `1`, a `4` or an `8`.
`delays` | If defined, a list containing lists of delays for an animated icon state. Each list in the container list corresponds to a direction. The delays are floats and represent seconds.

States are always ordered alphabetically by their corresponding file name.

#### Directions

There are currently three supported direction types: `1` (no directions), `4` (North South East West), and `8` (North South East West plus diagonals).
These directions are ordered (for layout in the `delays` field and ordering in the sprite sheet) in the following order:

* South
* North
* East
* West
* South East
* South West
* North East
* North West

#### Sprite sheet

A single sprite sheet contains information for a single RSI state, but a state may contain multiple sprites in the case of a state which uses animations or directional data. In these cases, the RSI's `size` is used as a bounding box to crop each icon for an individual frame or direction from the overall sheet.

Sprites are written into a `.json` grouped by direction, then by writing each animated frame's icon in a direction in order. For example, with 4 directions, *all* south states get written first, then north states, etc.

The size of the file must always be multiple of the RSI's `size`. Sprites are ordered from the top left to the bottom right, always going horizontally first. The amount of sprites per row or column should be as equal as possible, preferring rows to be longer than columns if the amount of states is not able to be divided perfectly.

As an example, here is how you would format the sprite sheet for a ball that has four directionals, each with four 'blinking' frames:

![](/img/docs/setup/codebase/example-sprite.png)

:::tip[Saving on Sprite Size]
In the example above, four sprites are included for the south state, but since they're all the same, you only need one. **Be careful when doing this**, as sprite frames are constructed from each size box in order no matter what.

In order to reduce the size of our above example, we'll need to move our East states up a row, like so.

![](/img/docs/setup/codebase/example-sprite-small.png)
:::

### Example JSON

Note that in practice the JSON writer probably writes the most compact JSON possible to reduce file size.

```json
{
    "version": 1,

    "license": "CC0-1.0",
    "copyright": "GitHub @PJB3005",

    "size": {
        "x": 32,
        "y": 32
    },
    "states": [
        {
            "name": "hello",
            "flags": {},
            "directions": 4,
            "delays": [
                [1, 1, 1],
                [2, 3, 4],
                [3, 4, 5],
                [4, 5, 6]
            ]
        }
    ]
}
```

### Loading Parameters

The `load` key allows various load parameters that change how the engine loads the sprite. Keys are as such:

Key | Meaning
--- | -------
`srgb` | Boolean that indicates whether the sprite is interpreted as sRGB by shaders and such. Default `true`. If creating an RSI intended to be used as displacement data, this should be set to `false`.