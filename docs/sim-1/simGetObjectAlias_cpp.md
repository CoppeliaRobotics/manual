# simGetObjectAlias

Retrieves the alias or path of an object based on its handle

## Synopsis

```cpp
char* simGetObjectAlias(int objectHandle, int options)
```

## Parameters

- **objectHandle**: handle of the object.
- **options**: alias formating options:

    - -1: naked alias (e.g. "alias")
    - 0: ordered alias (e.g. "alias[0]")
    - 1: short path that fully identifies the object (e.g. "/parent/alias[0]")
    - 2: full path (e.g. "/parentA/parentB/alias[0]")
    - 3: naked alias with handle, if the alias is not unique (e.g. "alias" or "alias__42__")
    - 4: naked alias with handle (e.g. "alias__42__")
    - 5: print version of the short path, not guaranteed to be unique (e.g. "/parent/ ... /alias")
    - 6: path using just the alias and an index number (e.g. "/alias{3}")
    - 7: same as 6, but using the first parent model, if present (e.g. "/parentModel{2}/alias{3}")
    - 8: same as 6, but using the first 2 parent models, if present (e.g. "/parentModelA{4}/parentModelB{2}/alias{3}")
    - 9: same as 6, but using all parent models, if present (e.g. "/parentModelA{4}/.../parentModelN{2}/alias{3}")

## Return values

- Alias or path of the object if operation was successful, nullptr otherwise. The user is in charge of destroying the returned buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md)

## See also

- [simSetObjectAlias](simSetObjectAlias_cpp.md)
