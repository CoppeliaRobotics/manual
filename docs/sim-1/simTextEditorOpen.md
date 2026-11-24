# sim.textEditorOpen

Opens a text edition window

## Synopsis

```lua
int handle = sim.textEditorOpen(string initText, string properties)
```

```python
int handle = sim.textEditorOpen(string initText, string properties)
```

## Parameters

- **initText**: initial text to be displayed.
- **xml**: XML description of the text editor's properties. Can be an empty string for default properties

## Return values

- **handle**: handle of the text editor

## XML example

```xml
<editor
title="Window title" editable="true" searchable="true"
tab-width="4" toolbar="false" statusbar="false" resizable="true" modal="false"
on-close="callbackFunction" closeable="true" position="100 100" size="800 600"
placement="absolute" font="Courier" font-size="14" activate="false" editable="true"
line-numbers="true" max-lines="0" lang="lua" wrap-word="false"
text-col="50 50 50" background-col="190 190 190" selectionColor="128 128 255"
comment-col="0 140 0" number-col="220 0 220" string-col="255 255 0"
character-col="255 255 0" operator-col="0 0 0" identifier-col="64 64 64"
preprocessor-col="0 128 128" keyword1-col="152 0 0" keyword2-col="220 80 20"
keyword3-col="0 0 255" keyword4-col="152 64 0">

<keywords1>
  <item word="sim.getObject" autocomplete="true"
    calltip="int handle=sim.getObject(string path)" />
  <item word="sim.getObjectPosition" autocomplete="true"
    calltip="float[3] pos=sim.getObjectPosition(int handle,
      int relHandle)" />
</keywords1>

<keywords2>
  <item word="sim.getObjectOrientation" autocomplete="true"
    calltip="float[3] euler=sim.getObjectOrientation(int handle,
      int relHandle)" />
</keywords2>

</editor>

placement attribute recognizes following values: center, absolute and relative
```

## See also

- [sim.textEditorClose](simTextEditorClose.md)
- [sim.textEditorShow](simTextEditorShow.md)
- [sim.textEditorGetInfo](simTextEditorGetInfo.md)
