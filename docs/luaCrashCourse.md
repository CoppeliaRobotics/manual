# Lua crash course

The following crash course is an extremely condensed extract from the official Lua reference manual. For more details refer to the free [Lua Quick Reference](https://orbitalquark.github.io/lua-quick-reference/) e-book, to the [Lua website](http://www.lua.org) and to the numerous examples contained in the demo scenes.

## <a id="lexicalConventions"></a>Lexical conventions

- Lua is a case-sensitive language. "and", "And" or "AND" are not the same.
- The following are Lua keywords: `and` `break` `do` `else` `elseif` `end` `false` `for` `function` `if` `in` `local` `nil` `not` `or` `repeat` `return` `then` `true` `until` `while`
- The following strings denote other tokens: `+` `-` `*` `/` `%` `^` `#` `==` `~=` `<=` `>=` `<` `>` `=` `(` `)` `{` `}` `[` `]` `;` `:` `,` `.` `..` `...`
- Literal strings can be delimited by matching single or double quotes (e.g. `'hello'` or `"hello"`)
- A comment starts with a double hyphen (--) anywhere outside of a string. e.g.:

```lua
a=4 -- variable a is now 4!
```

## <a id="valuesAndTypes"></a><a id="typesAndValues"></a>Types and values

- Lua is a dynamically typed language which means that variables do not have types; only values do.
- There are 8 basic types in Lua:
  - `nil` Type of the value nil whose main property is to be different from any other value. It usually represents the absence of a useful value
  - `bool` Values false and true (both nil and false make a condition false; any other value makes it true)
  - `number` Both integer and floating-point numbers (has internally two distinct representations: long integer and double)
  - `string` Arrays of characters (strings may contain any 8-bit character, including embedded zeros)
  - `function` Lua functions
  - `userdata` Can hold arbitrary C data (corresponds to a block of raw memory)
  - `thread` Independent threads of execution used to implement coroutines
  - `table` Arrays that can hold values of any type except nil

## <a id="variables"></a>Variables

- There are 3 kinds of variables: global variables, local variables and table fields. Any variable is assumed to be global unless explicitly declared as local
- Before the first assignment to a variable, its value is nil
- Square brackets are used to index a table (e.g. `value=table[x]`). The first value in a table is at position 1 (and not 0 as for C arrays)

## <a id="statements"></a>Statements

- Relational operators (always result in **false** or **true**)
  - `==` equality
  - `~=` Negation of equality
  - `<` Smaller than
  - `>` Bigger than
  - `<=` Smaller than or equal to
  - `>=` Bigger than or equal to
- Lua allows multiple assignments. The syntax for assignments defines a list of variables on the left side and a list of expressions on the right side. The elements in both lists are separated by commas:

```lua
x,y,z = myTable[1],myTable[2],myTable[3]
```

- **If** control structure (by example):

```lua
if value1==value2 then
    print('value1 and value2 are same!')
end
```

- **For** control structure (by example):

```lua
for i=1,4,1 do -- count from 1 to 4 with increments of 1
    print(i)
end
```

- **While** control structure (by example):

```lua
i=0
while i~=4 do
    i=i+1
end
```

- **Repeat** control structure (by example):

```lua
i=0
repeat
    i=i+1
until i==4
```

- **Table** operations (by example):

```lua
myTable={'firstValue',2,3} -- builds a table with 3 values

print(myTable[1]) -- prints the first element in the table

table.insert(myTable,4) -- appends the number 4 to the table
```

- Concatenation (by example):

```lua
a='hello'
b=' world'
c=a..b -- c contains 'hello world'
```

- Length operator #:

```lua
stringLength=#'hello world'

tableSize=#{1,2,3,4,5}
```

## <a id="bitwiseOperators"></a>Bitwise operators

- Lua supports the following bitwise operators:

- `&` Bitwise AND
- `|` Bitwise OR
- `~` Bitwise exclusive OR
- `>>` Right shift
- `<<` Unary bitwise NOT
- `~` Unary bitwise NOT

## <a id="coroutines"></a><a id="threads"></a>Coroutines or threads

- Coroutines are easily created and resumed with:

```lua
-- Create a coroutine:
corout = coroutine.create(coroutineMain)

-- Start/resume a coroutine:
if coroutine.status(corout) ~= 'dead' then
    local ok, errorMsg = coroutine.resume(corout)
    if errorMsg then
        error(debug.traceback(corout, errorMsg), 2)
    end
end

-- The coroutine itself:
function coroutineMain()
    while true do
        -- some code
    end
end
```
