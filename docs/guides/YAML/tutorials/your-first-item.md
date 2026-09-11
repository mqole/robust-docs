---
sidebar_position: 1
---

# Adding your own Item
Adding an item into SS14 is a fairly straight forward process thanks to how robust YML is. For a majority of cases a lot of the work needed to create items is already done for you. 

---

### Visuals

First off is the visuals. This is key to having a new item in the game since for anything to be interacted with, it needs to be able to be seen.

All sprite related files will go into the `Resources/Textures` directory as a base, but you shouldn't place regular sprites in that exact spot. For the purpose of this tutorial, we're going to place our sprite in;

`Resources/Textures/_OurFork/Objects/Tutorial/myitem.rsi`

:::info[Quick note!]
All forks will place their specific files within a folder thats name starts with _, in this case ours is _OurFork. This is done for organisational purposes so we know what content is from what fork!

This process is called namespacing and will come up more during the C# tutorials!

**Additional note!**
All `.rsi` folders use lowercase names with no spaces!
:::

In this folder you will place 2 files. First is your sprites `.png` file, and the second is a new file called `meta.json`. This is a file which the game uses to communicate between the engine, and your sprite. Don't worry though, this file is pretty simple.

This is what our JSON file is going to look like;

```jsonld showLineNumbers=1
{
  "version": 1,
  "license": "CC-BY-SA-3.0",
  "copyright": "FancyPlanks from https://github.com/FancyPlanks",
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

:::warning[Warning!]
JSON files can be very picky about formatting, if you find your sprite isn't working for whatever reason, then be sure to make sure you've formatted the JSON correctly.
:::

- `license` is our copyright license. Generally this will be the same unless you want a different license for your sprite.
- `copyright` is the person the sprite is credited to.
- `size` is how big our sprite will be in game. Most items use 32 x 32
- `states` is the part used by the `SpriteComponent` in our items `.yml`. We'll get into this more later.

:::info
**Quick note!**
The `name` within a given state should match the _exact_ name of the sprite in the folder! Remember to double check capitalisations and spelling!
:::

With the `.json` and `.png` files now in the folder, you should be set on the visuals part of making the item.

---

### The YML code

Now that the visuals are setup, the `.yml` is all that is left to be done. Similarly to our sprite we will be putting the `.yml` in a particular location;

`Resources/Prototypes/_OurFork/Objects/Tutorial`

`Prototypes` is the folder where all the `.yml`'s the game uses goes.

In this folder, make a file called `tutorial_items.yml`

:::info[Quick note!]
`.yml` files cannot use spaces! If you want to seperate 2 words, just use an underscore.

All of them are also done in all lowercase.
:::

In this file is where we are going to be placing our item's code. First let's start with a similar outline to what was laid out in [What's an Entity?](../introduction/whats-an-entity.md)

```yaml  showLineNumbers=1  
- type: entity
  name: my item
  description: "My tutorial item."
  id: TutorialItem
```

---

Now if you enter the game and enter either the `name` or `id` into your Entity Spawn Panel, your item will be there!

![image](https://hackmd.io/_uploads/BklYPoA-Gl.png)

But there's no visuals. So how do we get those? Like this;

```yaml  showLineNumbers=1 
- type: entity
  name: my item
  description: "My tutorial item."
  id: TutorialItem
  components:
  - type: Sprite
    sprite: _OurFork/Objects/Tutorial/myitem.rsi
    state: icon
```

As mentioned in the [Components](../introduction/components) section, all entities will come with a list of attached components to make themselves function within the game. In this case the component we need is `Sprite`

- `sprite` is the location of our `.rsi`
- `state` is the state we set within the `.json` file that we want to use.

You might notice that the directory we laid out in `sprite` is missing the `Resources/Textures` part. This is because the `SpriteComponent` will already assume your sprite is located within that directory, so you only need to focus on the exact file you placed your sprite in.

:::danger[Important!]
A majority of "Why isn't my sprite working?" issues come down to a spelling mismatch within either `sprite` or `state`. If your sprite isn't working, be sure to double check that your spellings & location match the **exact** spelling & location of your sprites directory!

**Additional warning!**
The directory you put in `sprite` **must** use / and not \ otherwise the game will crash!

**Additional warning!**
You must be careful with directories! Sometimes a directory can work in your development environment but fail when connecting from the main client. An example of this is making a mistake such as 

`_MyFork//Textures/Objects/mything.rsi`

Notice the `//`? This would not crash when connecting from your build client, but when connecting from the main SS14 client it **will** cause severe memory issues and make the game unplayable when that entity is on screen!
:::
   
---
   
Now if we look again

![image](https://hackmd.io/_uploads/rJTpKs0-fl.png)

It's there! You're now able to freely place the item, but we still can't actually touch it. Why not? Well that's because there's still one key thing we are missing here which is all the information that actually makes this entity into an item. This would involve giving our entity multiple different components and inflate the YML to a massive size.

So is there an easier way to turn it into an item? Well yes there is, as there already exists an entity with all of the needed item information attached, `BaseItem`

```yaml  showLineNumbers=1  showLineNumbers=1
- type: entity
  name: my item
  description: "My tutorial item."
  parent: BaseItem
  id: TutorialItem
  components:
  - type: Sprite
    sprite: _OurFork/Objects/Tutorial/myitem.rsi
    state: icon
```

- `parent` is the YML we inherit from. This copies all the components and their information over from that YML, to our one. Saving us a tremendous amount of time.

:::info[Quick note!]
Check back to [YML Parenting](../introduction/yml-parenting) if you need a more detailed explanation on how Parenting works!
:::

`BaseItem` in this case is as the name implies, the base of all items within the game. Without it an item will not function like a standard item would.

If you want an idea of just how big `BaseItem` is, this is how its YAML looks. (Don't worry, you don't need to understand it. This is just here for those who want an idea of the amount of work parenting saves them!)
:::spoiler BaseItem YAML
```yaml  showLineNumbers=1  showLineNumbers=1
- type: entity
  name: "item"
  id: BaseItem
  abstract: true
  components:
  - type: Item
    size: Small
  - type: Animateable
  - type: Clickable
  - type: InteractionOutline
  - type: MovedByPressure
  - type: EmitSoundOnCollide
    sound:
      collection: WeakHit
  - type: EmitSoundOnLand
    sound:
      path: /Audio/Effects/drop.ogg
      params:
        volume: 2
  - type: DamageOnHighSpeedImpact
    damage:
      types:
        Blunt: 5
    soundHit:
      collection: MetalThud
  - type: CollisionWake
  - type: GravityAffected
  - type: Physics
    bodyType: Dynamic
    fixedRotation: false
  - type: Fixtures
    fixtures:
      fix1:
        shape:
          !type:PhysShapeAabb
          bounds: "-0.25,-0.25,0.25,0.25"
        density: 20
        mask:
        - ItemMask
        restitution: 0.3  # fite me
        friction: 0.2
  - type: Sprite
    drawdepth: Items
    noRot: false
  - type: Pullable
  - type: DamageExaminable
```

With that final piece, now when you return to the game and spawn in a new version of your item, you'll be able to pick it up, throw it, drag it and all the other things you would do with a plain item!

Obviously this item is still fairly simple and uninteresting, all you can do really is move it around, but this is a start! Now you can begin toying with different components to attach to it.

---

As an example, let's try having our item emit some light. How do we do this? Well in our item's YML we would need to give it a component specific for this purpose.

In some cases, depending on what you want, you may need to make a brand new component from scratch using C#. This will be explained in the C# tutorials later on. For now, there is already a component that does exactly what we want;

```yaml  showLineNumbers=1  showLineNumbers=1
- type: entity
  name: my item
  description: "My tutorial item."
  parent: BaseItem
  id: TutorialItem
  components:
  - type: Sprite
    sprite: _OurFork/Objects/Tutorial/myitem.rsi
    state: icon
  - type: PointLight
    enabled: true
    color: "#c222e2"
    radius: 5.0
    energy: 10.0
```

- `PointLight` is the component that allows any entity to emit a radius of light around itself.
    - `enabled` states if our light is on.
    - `color` is the hexcode value for the color. 
    - `radius` is how wide the area of light around the entity will be.
    - `energy` is how strong the brightness will be.

This is how easy it is to toy with your item. So feel free to start playing around with it!

:::info[Quick info!]
Some components will rely on other components being attached in order to function. So it's good to know what a component will require before attaching it.

If you are confused at all, ask within your specific forks community!
:::