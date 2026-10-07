---
sidebar_position: 6
---
# Bonus Stage: YAML Anchors & Graphs

When you poke around the games various construction graphs you are going to find some that are a little... disgusting. Let's look at this graph for example

```yaml=
- type: constructionGraph
  id: LoungerSofaGraph
  start: start
  graph:
    - node: start
      actions:
        - !type:DestroyEntity {}
      edges:
        - to: BenchLoungerSofaMiddleNode
          completed:
            - !type:SnapToGrid { }
          steps:
            - material: Steel
              amount: 2
              doAfter: 1
            - material: Cloth
              amount: 2
              doAfter: 1
        - to: BenchLoungerSofaLeftNode
          completed:
            - !type:SnapToGrid { }
          steps:
            - material: Steel
              amount: 2
              doAfter: 1
            - material: Cloth
              amount: 2
              doAfter: 1
        - to: BenchLoungerSofaRightNode
          completed:
            - !type:SnapToGrid { }
          steps:
            - material: Steel
              amount: 2
              doAfter: 1
            - material: Cloth
              amount: 2
              doAfter: 1
        - to: BenchLoungerSofaCornerNode
          completed:
            - !type:SnapToGrid { }
          steps:
            - material: Steel
              amount: 2
              doAfter: 1
            - material: Cloth
              amount: 2
              doAfter: 1

    - node: BenchLoungerSofaMiddleNode
      entity: BenchLoungerSofaMiddle
      edges:
        - to: start
          completed:
            - !type:SpawnPrototype
              prototype: SheetSteel1
              amount: 2
            - !type:SpawnPrototype
              prototype: MaterialCloth1
              amount: 2
          steps:
            - tool: Screwing
              doAfter: 1
    - node: BenchLoungerSofaLeftNode
      entity: BenchLoungerSofaLeft
      edges:
        - to: start
          completed:
            - !type:SpawnPrototype
              prototype: SheetSteel1
              amount: 2
            - !type:SpawnPrototype
              prototype: MaterialCloth1
              amount: 2
          steps:
            - tool: Screwing
              doAfter: 1
    - node: BenchLoungerSofaRightNode
      entity: BenchLoungerSofaRight
      edges:
        - to: start
          completed:
            - !type:SpawnPrototype
              prototype: SheetSteel1
              amount: 2
            - !type:SpawnPrototype
              prototype: MaterialCloth1
              amount: 2
          steps:
            - tool: Screwing
              doAfter: 1
    - node: BenchLoungerSofaCornerNode
      entity: BenchLoungerSofaCorner
      edges:
        - to: start
          completed:
            - !type:SpawnPrototype
              prototype: SheetSteel1
              amount: 2
            - !type:SpawnPrototype
              prototype: MaterialCloth1
              amount: 2
          steps:
            - tool: Screwing
              doAfter: 1
```

This graph is for building a sofa, but it's a tiny bit big. All the different lines make reading it a hastle and might make you want to avoid working on it. When you read it however you'll notice that a lot of it is repeated YAML. This one chunk repeats itself four whole times

```yaml=
      edges:
        - to: start
          completed:
            - !type:SpawnPrototype
              prototype: SheetSteel1
              amount: 2
            - !type:SpawnPrototype
              prototype: MaterialCloth1
              amount: 2
          steps:
            - tool: Screwing
              doAfter: 1
```

That is 12 lines that get repeated over and over. 48 lines of code overall. How can we cut this down?

This is where [YAML Anchoring](https://support.atlassian.com/bitbucket-cloud/docs/yaml-anchors/) comes into play. This is a feature of YAML that lets us turn repeated code into a single pointer reference within the file. This is done through declaring a reference pointer and then having YAML point back to it. Let's reuse the above code for example.

```yaml=
      edges: &edgeDecon
        - to: start
          completed:
            - !type:SpawnPrototype
              prototype: SheetSteel1
              amount: 2
            - !type:SpawnPrototype
              prototype: MaterialCloth1
              amount: 2
          steps:
            - tool: Screwing
              doAfter: 1
```

What `&edgeDecon` here does is declare the reference edge for future use. This means that any future edges which need to reuse this YAML can instead of requiring you to rewrite the same lines repeatedly, instead be defined like this.

```yaml=
      edges: *edgeDecon
```

The YAML parser will then place the code from the original `&edgeDecon` on each edge using `*edgeDecon`. If we apply anchors to the graph mentioned at the top of this Stage, it will end up looking like this.

```yaml=
- type: constructionGraph
  id: LoungerSofaGraph
  start: start
  graph:
    - node: start
      actions:
        - !type:SpawnPrototype
          prototype: SheetSteel1
          amount: 2
        - !type:SpawnPrototype
          prototype: MaterialCloth1
          amount: 2
        - !type:DestroyEntity {}
      edges:
        - to: BenchLoungerSofaMiddleNode
          completed:
            - !type:SnapToGrid { }
          steps: &constructSteps
            - material: Steel
              amount: 2
              doAfter: 1
            - material: Cloth
              amount: 2
              doAfter: 1
        - to: BenchLoungerSofaLeftNode
          completed:
            - !type:SnapToGrid { }
          steps: *constructSteps
        - to: BenchLoungerSofaRightNode
          completed:
            - !type:SnapToGrid { }
          steps: *constructSteps
        - to: BenchLoungerSofaCornerNode
          completed:
            - !type:SnapToGrid { }
          steps: *constructSteps

    - node: BenchLoungerSofaMiddleNode
      entity: BenchLoungerSofaMiddle
      edges: &deconEdge
        - to: start
          steps:
            - tool: Screwing
              doAfter: 1
    - node: BenchLoungerSofaLeftNode
      entity: BenchLoungerSofaLeft
      edges: *deconEdge
    - node: BenchLoungerSofaRightNode
      entity: BenchLoungerSofaRight
      edges: *deconEdge
    - node: BenchLoungerSofaCornerNode
      entity: BenchLoungerSofaCorner
      edges: *deconEdge
```

From 105 lines, all the way down to 53. As you can see this also doesn't only apply to edges, it can apply to any definition. Be it `edges`, `steps` or `completed`. Anchoring also doesn't only just work for Graphs! Look around online if you really want to learn how useful tools like Anchoring can be!