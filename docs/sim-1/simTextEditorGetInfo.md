# sim.textEditorGetInfo

Retieves information from a text edition window previously opened with [sim.textEditorOpen](simTextEditorOpen.md)

## Synopsis

```lua
string text, int[2] pos, int[2] size, bool visible = sim.textEditorGetInfo(int handle)
```

```python
string text, list pos, list size, bool visible = sim.textEditorGetInfo(int handle)
```

## Parameters

- **handle**: handle of the text editor window

## Return values

- **text**: text of the editor, or None/nil if the given handle is not associated with any text editor window (or the window was already closed)
- **pos**: size of the editor
- **size**: absolute position the editor
- **visible**: visible state the editor
