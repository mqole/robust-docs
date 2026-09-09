---
sidebar_position: 2
---

# Adding your own Structure

Structures are the next type of entity we are going to be focusing on. They make up a large part of what you will interact with within the game, be it a simple wall, a table or things such as machines. All of these things are structures.

Structures themselves are not too different from items in the way that they are created through YML, but they do have some more to them that is important to know for the sake of this tutorial.

### Visuals

Once again this is the first step. First make yourself a new `.rsi`

`Resources/Textures/_OurFork/Structures/Tutorial/mystructure.rsi`

Most of this is the same as it was in [Your first item](your-first-item) so I won't go as into detail. Drop your sprite and JSON into this folder

```jsonld showLineNumbers=1
{
  "version": 1,
  "license": "CC-BY-SA-3.0",
  "copyright": "FancyPlanks from hackmd.io/@FancyPlanks",
  "size": {
    "x": 32,
    "y": 32
  },
  "states": [
    {
      "name": "icon"
    }
  ]
}
```
-----
### The YML Code

So let's use what we learned in [Your first item](your-first-item) to get the YML all set up. Generally all of the base steps are the same, the only real different will be what our `parent` is, which in this case will be `BaseStructure`.

```yaml showLineNumbers=1
- type: entity
  name: my structure
  parent: BaseStructure
  id: TutorialStructure
  description: "My Tutorial Structure."
  components:
  - type: Sprite
    sprite: _OurFork/Structures/Tutorial/mystructure.rsi
    state: icon
```

So what actually differentiates a structure, from an item? 

This answer will vary from structure to structure. In our case, this is going to be a structure that does several things
- It will be anchorable
- It will be unable to rotate
- It will be pullable

:::info[Quick tip!]
Structures don't need these three things to become structures! All they require is `BaseStructure`. Remember this when you start playing around with your own structures!
:::

So let's tackle the first one of this list, anchoring. This is one of the most common features of structures around a station and will be a key thing to understand.

On your YML, add in two new components. `Anchorable` and `Transform`. When you have done so, your YML should look something like this;

```yaml showLineNumbers=1
- type: entity
  name: my structure
  parent: BaseStructure
  id: TutorialStructure
  description: "My Tutorial Structure."
  components:
  - type: Sprite
    sprite: _OurFork/Structures/Tutorial/mystructure.rsi
    state: icon
  - type: Anchorable
  - type: Transform
```
- `Anchorable` is the component which allows a structure to be anchored and unanchored.
- `Transform` is the component which controls an entity's position and rotation. All Entities will have this by default, we are defining it so we can edit the variables.

Under the `Transform` component add in `anchored: true`, this will start our structure anchored upon creation.

```yaml showLineNumbers=1
- type: entity
  name: my structure
  parent: BaseStructure
  id: TutorialStructure
  description: "My Tutorial Structure."
  components:
  - type: Sprite
    sprite: _OurFork/Structures/Tutorial/mystructure.rsi
    state: icon
  - type: Anchorable
  - type: Transform
    anchored: true
```

Just like that we now have a structure that can be anchored and unanchored. So what about rotations? These are, much like anchoring, incredibly simple to handle.

Under `Transform` add in `noRot: true`.
Under `Sprite` add in `noRot: true`.

You're all set! This is how incredibly easy working with entities is through YML. The difference between an item and a structure is simply the parent. This continues with pullable structures, which only require the `Pullable` component. 

With all these variables and components set, you should have a YML that looks something like this.

```yaml showLineNumbers=1
- type: entity
  name: my structure
  parent: BaseStructure
  id: TutorialStructure
  description: "My Tutorial Structure."
  components:
  - type: Sprite
    sprite: _OurFork/Structures/Tutorial/mystructure.rsi
    state: icon
    noRot: true
  - type: Anchorable
  - type: Transform
    anchored: true
    noRot: true
  - type: Pullable
```

Now if you go into your Entity Spawn Panel, you will find your structure there, sprite and all! Spawn it in, anchor it, play around with it all you like.

![image](https://hackmd.io/_uploads/ByIsRV1ffl.png)

:::info[Quick tip!]
If you want to see more variables within each component, you are able to look into the components C# file. In the case of `Transform` this file would be `TransformComponent.cs`. Usually variables that can be edited through YML will have a `[DataField("")]` defined above it. Though some don't.
:::