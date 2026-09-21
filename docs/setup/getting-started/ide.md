# Setting Up an IDE

An IDE (Integrated Development Environment) is software that makes editing files and navigating folders in a workspace much easier. Most IDEs will allow users to have multiple folders open at once, tab between files or view them side by side, use an integrated command line to run files, use syntax highlighting to make files easier to read, search for a single line of text across an entire folder's worth of files... the list goes on!

While you *can* technically develop for SS14 using a text editor like Notepad++ and a lot of resilience, you will have a much easier time doing so if you use an IDE.

![](/img/docs/setup/ide/use-an-ide.png)

## Choosing your IDE

There are several options available to you if you haven't yet downloaded an IDE, depending on what OS you're using and what your priorities are. The best free ones are:

  * For **all platforms**, [Rider](https://www.jetbrains.com/rider/) by JetBrains, which is free for non-commercial use. Fantastic for use with C#, especially if you're going to be running a lot of tests.
  * For **all platforms**, [Visual Studio Code](https://code.visualstudio.com/) (VSCode) is a nice minimalist IDE by Microsoft which has a lot of great user-made plugins available. Don't get it confused with VSC (Visual Studio Community), which is a lot bulkier.
  * For **all platforms**, [VSCodium](https://vscodium.com/) is an open source version of VSCode without the AI bloat and tracking.

:::tip[VSCode and VSCodium extension]
If using one of these IDEs, you'll want to install the requisite extensions to enable support for any additional coding languages used by your project. RT and SS14 are mostly coded in C#, so you'll want to make sure you've installed Microsoft's official [C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit) extension.

**Exclusive to VSCode and VSCodium**, you also can install our community made [Robust YAML](https://marketplace.visualstudio.com/items?itemName=slava0135.robust-yaml) extension for better Robust Toolbox YAML experience on top of the [YAML Language Support](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) extension.
:::

:::warning[VSCodium and SLNX]
Currently VSCodium seemingly does [not support SLNX](https://github.com/muhammadsammy/free-vscode-csharp/issues/95), although you may be able to get around this by using the [Resharper](https://open-vsx.org/extension/JetBrains/resharper-code) plugin in place of C# Dev Kit.
:::


## Setup

:::tip[Windows and Winget]
Windows users may prefer to use Winget for an easier install. Just open Command Line and enter one of the following:
```
winget install JetBrains.Toolbox (or 'JetBrains.Rider' if you don't want the whole toolbox app)
winget install Microsoft.VisualStudioCode (Visual Studio Code)
winget install VSCodium.VSCodium (VSCodium)
```
:::

### JetBrains Rider
1. Install Rider from the [official site](https://www.jetbrains.com/rider/). It's suggested that you use [Jetbrains Toolbox](https://www.jetbrains.com/toolbox-app/) to enable automatic updates.
   
2. Go through the setup.
   
3. Press "Open" and select your `SpaceStation14.slnx` file.
   
4. If you plan to do engine development, you'll need to add Robust Toolbox to the Directory Mappings so that Rider's Version Control Software (VCS) can detect changes to Robust. Open Rider's settings and go to the `Version Control` section > `Directory Mappings` and press the plus `+` button. For `Directory` point it to the `RobustToolbox` folder in the project and use Git as the VCS.
   
5. Choose the branch you want to use in the top left
   
6. You can now select what you want to run (Server, Client, or both) using the dropdown button in the top right, then press the play button to compile and run it.

C# IDEs like Rider don't automatically show the `Resources` folder in the project. This folder contains all non-C# files such as sprites, audio, and most importantly, YAML prototypes. You'll need to follow a few extra steps to be able to see these.

In Rider, you can "attach" the resources directory to the solution. Do this by right clicking the solution in the explorer, then clicking `Add` -> `Existing Folder...`. Select the `Resources` directory in the file picker.

![](/img/docs/setup/ide/rider-attach-folder-1.png)
![](/img/docs/setup/ide/rider-attach-folder-2.png)

After this, your solution view should look something like this, and you should be able to easily access the `Resources` folder.

![](/img/docs/setup/ide/rider-attach-folder-3.png)

### VSCode

1. Download VSCode from the [official site](https://code.visualstudio.com/).
   
2. Once installed, click `Open Folder`, then navigate to your repository and open this full folder.
   
3. Navigate to the Extensions tab (part way down on the top left corner bar, looks like 4 tiles) and install the [C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit) extension. (And pick up [YAML Language Support](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) and [Robust YAML](https://marketplace.visualstudio.com/items?itemName=slava0135.robust-yaml) while you're here!)
   
4. When asked to open a solution, select `SpaceStation14.slnx`. Alternatively, set `dotnet.defaultSolution` setting to `SpaceStation14.slnx` in your workspace settings.
   
5. Now you can run and debug your game. Select the icon above "Extensions" from earlier for "Run and Debug" and from the dropdown next to the green play button you can select "Server/Client". This will run both the client and server, opening the game for you to debug. Relevant information will pop up in the debug along the bottom. Select the processes in the call stack on the left to change what you are debugging.
   
### VSCodium
1. Download [VSCodium Here](https://vscodium.com/) or more directly [on Github Here](https://github.com/VSCodium/vscodium/releases) (On the latest release, click the assets dropdown then scroll to the ZIP or .exe for your OS).
   
2. Run the installer or extract the zip file to a location of your choice and run the .exe once extracted.
   
3. Once installed, click `Open Folder`, then navigate to your repository and open this full folder.
   
4. Navigate to the Extensions tab (part way down on the top left corner bar, looks like 4 tiles) and install the [C#](https://open-vsx.org/extension/muhammad-sammy/csharp) extension.
   
5. When asked to open a solution, select `SpaceStation14.slnx`. Alternatively, set `dotnet.defaultSolution` setting to `SpaceStation14.slnx` in your workspace settings.
   
6. Now you can run and debug your game. Select the icon above "Extensions" from earlier for "Run and Debug" and from the dropdown next to the green play button you can select "Server/Client". This will run both the client and server, opening the game for you to debug. Relevant information will pop up in the debug along the bottom. Select the processes in the call stack on the left to change what you are debugging.

## What's Next?

If you want to run the game from this point, you'll need to have the requisite version of .NET installed. Read more about this on the guide to [Running SS14 Locally](./localhost.md).