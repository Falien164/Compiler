# Compiler
My own compiler using ANTLR and LLVM

## Zmienne globalne

Zmienne globalne too wszystkie zmienne które zostały zadeklarowane poza ciałem funkcji.

Aby uzyskać dostęp do zmiennej globalnej należy użyć operatora "@"

```
zmienna = 0
fn main() -> int {
  
    @zmienna = 2.0
    return 0
}


```