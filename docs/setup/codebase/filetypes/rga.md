---
sidebar_position: 2
---
# Robust Generic Attribution

<WipHeader/>

The **RGA** (Robust Generic Attribution) standard is a flexible, open, and readable way to define various metadata such as licensing and attribution for an arbitrary collection of files of many types (such as sound effects or prototypes).

An RGA file contains metadata for all of the files in the same directory as the RGA file, not including subdirectories. The entries in an RGA file contain specific metadata, such as the author of the file(s) or a description of any modifications made to them (in compliance with many Creative Commons licenses).

When adding a new file to a directory, a new entry should be created in the attribution file. In the case where an existing entry has identical metadata to the new file, that new file may instead be appended to the existing entry.

## YAML

An RGA file must be named `attributions.yml`. All values within entries are wrapped in double-quotes (`""`).

The `.yml` file contains an arbitrary number of entries, encompassing all files in the same directory as the RGA file. An entry is defined using the following arguments:

Key | Meaning
--- | -------
`files` | An array of filenames (with extensions) that this entry applies to. The filename order is arbitrary. The `*` wildcard glob is supported (i.e. `*.ogg` denotes all OGG files in the directory).
`copyright` | The copyright holder and other relevant info. Any disclosure of modifications to comply with certain licenses should also go in this field.
`license` | A valid [SPDX License Identifier](https://spdx.org/licenses/) applying to all files within an entry. If a license does not have a valid SPDX identifier, `Custom` may be used (but a link to the license should be provided in the `copyright` field).
`source` |  A valid URL pointing to a location where the file can be downloaded. If you are the creator of the work and don't have an alternate download location (e.g. bandcamp), provide the link to the pull request that added the file to the game. If this is a derivative work, this should be mentioned in the copyright field. If the file has only been lightly modified, just link to the original file. If the file has been heavily modified, link the modified version but provide links to any original files in the copyright field.

### Example YAML

```yaml
- files: ["thunderdome.ogg"]
  license: "CC-BY-NC-SA-3.0"
  copyright: "-Sector11 by MashedByMachines. Converted from MP3 to OGG."
  source: "https://www.newgrounds.com/audio/listen/312622"
- files: ["endless_space.ogg"]
  license: "CC-BY-3.0"
  copyright: "Endless Space by SolusLunes. Converted from MP3 to OGG."
  source: "https://www.newgrounds.com/audio/listen/67583"
```