# sim.textEditorClose

Closes a text edition window previously opened with [sim.textEditorOpen](simTextEditorOpen.md)

## Synopsis

```lua
string text, int[2] pos, int[2] size = sim.textEditorClose(int handle)
```

```python
string text, list pos, list size = sim.textEditorClose(int handle)
```

## Parameters

- **handle**: handle of the text editor window

## Return values

- **text**: text of the editor
- **pos**: size of the editor
- **size**: absolute position the editor
