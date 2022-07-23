

# Stardew Valley Chest Layout Generator
A tool to generate the optimal chest/workbench layout for a provided set of priorities

## Description
At its heart, this is basically the inverse of a simple neural network.

Typically, we would start with a dataset and end up with a set of abstractions and weights for said abstraction's parameters.

Instead, we are starting with concrete factors and parameters, then using how well input data fits into our factors as the scoring itself.

Finally, we use the inherent tree like nature of the data to maintain a common structure for our decided factors 
(for example, Emerald is a gem, all gems are classified as minerals, all minerals are classified as items).

## Examples
The following are all preset factors and
#### Foo


![foo]()

- ![bar]()
- ![baz]()

## Installation
### Executable
Download the `stardew-chest-layout` executable from the [GitHub release page]()
### Package
#### Pip
```terminal
pip install stardew-chest-layout
```

#### Poetry
```terminal
poetry add stardew-chest-layout
```


