---
sidebar_position: 2
---

# Components

Components are the real meat of the games entities. Every entity you interact with in the game has a series of components attached to it, all controlling their functionality.

Within a YML you will often see things being defined like this. This example being the Crusher Glaive's YML.

```yaml  showLineNumbers=1
- type: entity
  parent: [ WeaponCrusher, BaseSecurityCargoContraband]
  id: WeaponCrusherGlaive
  name: crusher glaive
  description: An early design of the proto-kinetic accelerator, in glaive form. Provides better healing in exchange for less charged damage.
  components:
  - type: Sprite
    sprite: Objects/Weapons/Melee/crusher_glaive.rsi
    state: icon
  - type: Item
    size: Ginormous
    sprite: Objects/Weapons/Melee/crusher_glaive-inhands.rsi
  - type: Clothing
    sprite: Objects/Weapons/Melee/crusher_glaive.rsi
    quickEquip: false
    slots:
    - Back
    - suitStorage
  - type: UseDelay
    delay: 1.9
  - type: BasicEntityAmmoProvider
    proto: BulletChargeGlaive
    capacity: 1
    count: 1
  - type: LeechOnMarker
    leech:
      groups:
        Brute: -21
  - type: Tag
    tags:
      - Pickaxe
      - Crusher #imp
  - type: MeleeWeapon
    attackRate: 1
    wideAnimationRotation: -135
    damage:
      types:
        Blunt: 3
        Slash: 7
    angle: 0
    animation: WeaponArcThrust
  - type: IncreaseDamageOnWield
    damage:
      types:
        Blunt: 2
        Slash: 6
        Structural: 20
```

In code, all of these components are seperate from eachother, but when put together in this way they allow an entity to take on a new identity that differentiates it from other entities within the game. In this case allowing it to do things like, be wielded, used to attack, worn and more.

Components come with a plethora of variables that are all defined within their `.cs` file, so if you poke around within this file then you may find new variables to toy with for your YML.

:::info[Quick tip!]
The game engine will chop off the word `Component` from a components name, but don't get it mistaken! All components in the games files will follow the naming scheme of `ThingComponent` as the game engine mandates it. So if you are looking for the `.cs` of a component, remember that it will have component on the end!
:::

:::warning[Warning!]
Some components are a bit sneaky. Their name in YAML will be different from the actual component class name. An infamous example of this being `ContainerContainer` which is only named that in YAML, in its actual class name it is `ContainerManagerComponent`.
:::