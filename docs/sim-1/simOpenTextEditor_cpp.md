# simOpenTextEditor

Opens a text edition window. The C version of this function opens a modal window

## Synopsis

```cpp
char* simOpenTextEditor(const char* initText, const char* xml, int* various)
```

## Parameters

- **initText**: pointer to the initial text to be displayed.
- **xml**: pointer to an XML description of the text editor's properties. Can be nullptr for default properties
- **various**: optional pointer holding the window size (various[0]-various[1]) and position (various[2],various[3])

## Return values

- nullptr in case of an error. Otherwise a pointer to the text. The user is in charge of releasing the returned buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md).

## XML example

```xml
<editor title="Window title" editable="true" searchable="true"
  tabWidth="4" textColor="50 50 50" backgroundColor="190 190 190"
  selectionColor="128 128 255" size="800 600" position="100 100" >

  <keywords1 color="152 0 0" >
    <item word="sim.getObject" autocomplete="true"
      calltip="int handle=sim.getObject(string path)" />
    <item word="sim.getObjectPosition" autocomplete="true"
      calltip="double[3] pos=sim.getObjectPosition(int handle,
        int relHandle)" />
  </keywords1>

  <keywords2 color="220 80 20" >
    <item word="sim.getObjectOrientation" autocomplete="true"
      calltip="double[3] euler=sim.getObjectOrientation(int handle,
        int relHandle)" />
  </keywords2>
</editor>


Other editor attributes with their default values are:

isLua = "false"
useSimKeywords = "false"
commentColor = "0 140 0"
numberColor = "220 0 220"
stringColor = "255 255 0"
characterColor = "255 255 0"
operatorColor = "0 0 0"
preprocessorColor = "0 128 128"
identifierColor = "64 64 64"
wordColor = "0 0 255"
word4Color = "152 64 0"
```

## See also

- [sim.textEditorOpen](simTextEditorOpen.md)
