---
sidebar_position: 2
---

# Running SS14 Locally

Running the game locally is often referred to as 'creating a development environment (devenv)' or 'opening a localhost'. In order to run an instance of SS14, you'll need to start a local server (using Content.Server) and open a game client window (using Content.Client). For development purposes, it's preferred to run the game's Debug build (or occasionally the Tools build).

To open your localhost, you'll first need to follow the [Git Setup](./git/git-setup.md) guide to download the game locally. In addition, you will need to install a version of .NET (sometimes referred to as 'dotnet'). As of RobustToolbox v269.0.0, the [.NET 10.0 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) is used.

:::warning[for Apple Silicon (ARM64) Mac users]
Some older codebases will only work with the x64 .NET and not the ARM64 one. You can either download x64 .NET, or update your codebase's RobustToolbox version to at minimum 267.0.0 to add support. If you get a `System.DllNotFoundException` when you try to run the game, check that your codebase's RobustToolbox version is up to date, and that you're using the x64 version (as opposed to the x86 version)!
:::

:::info[Windows and Winget]
Windows users may prefer to use Winget for an easier install. Just open Command Line and enter the following:
```
winget install Microsoft.DotNet.SDK.10
```
:::

## Opening the Game

If you've followed the guide to [Setting up an IDE](./ide.md), you'll be able to easily run the `Content.Server` and `Content.Client` assemblies on your chosen IDE, as long as you have the solution file open. From there, just click `Direct Connect` in the client window to connect to your development server!

To compile without an IDE, run `dotnet build` in the Command Line in the root folder of your repository. Then, call the following commands to run the client and server.
* `dotnet run --project Content.Server`
* `dotnet run --project Content.Client`

Both these commands use the Debug configuration by default. To enable release optimizations, add `--configuration Release` to the end of the dotnet invocation.

You can learn more about the difference between `Content.Server` and `Content.Client` in the [Codebase Organization](../codebase/organization.md) guide.

:::note[If using OpenSSL]
If you're having problems with .NET not finding libssl, try setting the `CLR_OPENSSL_VERSION_OVERRIDE` environment variable to the appropriate version. For instance, set it to `48` if your `/usr/lib` contains `libssl.so.48`.

If that doesn't work you can also try running `ln -s /usr/lib/libssl.so /usr/local/lib/libssl.so.1.0.0` instead.
:::

:::warning[Run Content, not Engine!]
**It is recommended that you run `Content.Client` and `Content.Server` when developing from your IDE.** *Not* `Robust.Client` or `Robust.Server`. The reason is that running `Content.*` will make your IDE aware of dependencies correctly and ensure everything is rebuilt nicely. If you run `Robust.Client` directly you have to make sure the solution is fully built every time.
:::

## Reproducible Development Environment with Nix/NixOS

<WipHeader text="I don't personally use Linux or Nix, so I'm not qualified to speak on this. This guide might be better in the IDE section. -mqole"/>

An easier way to set up your development environment for Linux users is to leverage Nix. Nix is a package manager and a functional domain specific language that allows one to declare anything from development environments to entire systems. In order to prevent the dreaded "it works on my machine" conundrum, we can declare a development environment in Nix that spawns an isolated reproducible shell.

### Setting up Nix/NixOS with flakes

You can [install Nix](https://nixos.org/download) either through installing the NixOS distribution itself or by using the script that is compatible with all Linux distributions that use systemd (Ubuntu, Fedora, Mint etc). For the sake of simplicity and convenience, it is recommended that you install Nix in a distribution that you are comfortable with instead of making the jump to a different operating system entirely. It is also possible to use Nix with MacOS through `nix-darwin` though this has not been tested as of yet and thus not covered in this article.

Once Nix is installed, you should enable experimental features such as flakes. If you are on a non-NixOS distribution, you can just add the following to your `~/.config/nix/nix.conf`.

* `experimental-features = nix-command flakes`

If you're using NixOS, you only need to add these options to your `configuration.nix` file.

* `nix.settings.experimental-features = [ "nix-command" "flakes" ];`

For more information about how to enable Nix flakes, see [here](https://nixos.wiki/wiki/Flakes).

### Using Nix flakes for a Robust Development Environment

NB it is technically required that you already have Git installed but in the case with most Linux distributions it comes preinstalled. In the highly unlikely case that you do not:

* Use your distribution's package manager

* Declare it in your `configuration.nix` file if you're using NixOS. It's recommended that you check the [appropriate section in the NixOS manual](https://nixos.org/manual/nixos/stable/#sec-configuration-file) but in short you should add `pkgs.git` into the `environment.systemPackages` attribute.

Using your terminal you can simply navigate to the root directory of your SS14 repo and run:

* `nix develop`

Nix will automatically handle all dependencies as declared by `shell.nix` and called by the `flake.nix` file. You will have a new ephemeral shell (known as a `devShell`) that has everything that you need installed to build SS14 from source.

This remains the reason as to why flakes are highly recommended despite being considered an experimental feature. We can make sure that everyone has the same versions of dependencies by specifying the nixpkgs collection version in the input attribute of the flake and locking the versions in a `flake.lock` file. In this way, all contributors that use Nix/NixOS get to have the exact same development environment. No pun intended, but that is pretty robust!

### (Optional) Run JetBrains Rider through Nix

You can then use either use an editor or IDE of your choosing. However within the shell that you already spawned you can just specify that you require JetBrains Rider. Run this command in your devShell.

* `NIXPKGS_ALLOW_UNFREE=1 nix shell nixpkgs#jetbrains.rider --impure`

From your new shell you can start a "detached" JetBrains Rider process by running something like:

* `nohup rider >/dev/null 2>&1 &`

And voila! You have robustly set up your development environment in a way that doesn't result in pesky buildup of "state". You can practically work on SS14 from any Linux distribution (granted that they use systemd) without irreversibly changing your system.