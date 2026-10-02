# Codebase Organization

<WipHeader/>

## Projects

SS14 (`Content`) and RobustToolbox (`Robust`) are split into several different projects. The main ones you'll care about are the `Client`, `Shared`, and `Server` projects. Other projects are for smaller things like integration tests, benchmarks, or database-specific code.

`Client`, `Shared`, and `Server` are each packaged into different 'assemblies', which is basically .NET talk for executables or shared libraries. These are represented in the repository by directories prepended by the parent project. For example, the folder `Content.Client` represents SS14's `Client` project, while `Robust.Server` is RobustToolbox's `Server` project.

The `Client` project in both Robust and SS14 contains client-specific code. This assembly is only sent to the client, the person actually playing the game.

The `Server` project contains server-specific code that no specific client should be able to interact with. This assembly is only located on the game server.

The `Shared` project contains shared code that can be used by the client or the server. This assembly is not executable, and it relies on the client or server to call functions in it or use data classes located within it. The purpose of shared is to allow for network prediction (where the client and server run the same code, to make things smoother) as well as to specify shared data classes, like network messages, so that the client and server can speak to each other effectively.

Shared code is only allowed to access other shared code, not client or server code. However, client and server code are always allowed to access shared code.

## Game Code

In SS14, code is organized by which game system is being handled (atmos/botany/buckling, etc) and then by the classes needed for it. The following conventions are used:

- All game code is organized in folders directly under `Content.`(`Client`/`Shared`/`Server` etc.).
- These game code folders are split into Components, EntitySystems, Visualizers, UI, Prototypes, etc. depending on their contents.
- If there would only be one file in a folder, it doesn't need a folder (unless that file would go directly into the project's top directory, which is undesirable).

:::warning[Do not use 'misc' folders!]
Miscellaneous folders are extremely undesirable for maintaining the organization of the codebase. You can encapsulate smaller game systems inside larger game systems if it unambiguously makes sense (eg. `Atmos/Piping`), but don't just throw all the smaller game systems into a 'misc' folder.
:::

<details>
<summary>A real example, under `Content.Server` at commit `da11cbd8e6bef3373ec1f570df7d7b9155a3890f`:</summary>

![](/img/general-development/codebase-info/codebase-organization/codebase-server-example.png)

- Atmos is a fairly large game system. It has many folders, and many files that do not need to go in these folders.
- Botany is a smaller game system. However, it only has one folder for Components since that's all that's really there.
- ItemCabinets are a very small game system. They just have a component and EntitySystem, and thus do not need folders for each.
</details>

## Resources

The resources folder contains excusively non-`.cs` files. These can include `.yml` prototypes, `.rsi` sprites, `.ogg` sound files, `.ftl` locale files, and more.

### Entity Prototypes

New folders should usually only be created for a new parent type. Parent prototypes should be contained in `base.yml` in this folder, while other prototypes go in a different file. If a prototype can be extracted into a parent prototype, it should go in its own folder.

This directory structure mirrors the prototype inheritance tree, making it obvious where to place new prototypes as well as being fairly unambiguous when choosing to create new folders.