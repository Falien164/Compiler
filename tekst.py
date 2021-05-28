fn condition(int a) -> int {
    print a
    x = 0
    y = 0
    read x
    read y 
    if ( x == 2 and y > 5 ){
        qwe1 = "spelniony warunek 1"
        print qwe1
        if ( y == 6 or y == 8){
            qwe10 = "y = 6 lub 8"
            print qwe10 
        }
    } else if ( x ==  2 and y < 5){
        qwe2 = "spelniony warunek 2"
        print qwe2
    } else if (x == 2 and y == 5) {
        qwe5 = "spelniony warunek 3"
        print qwe5
    } else {
        qwe4 = "zodyn warunek nie spelniony"
        print qwe4
    }
    return 0
}



glob = 2

fn foo() -> int {
    glob = 5
    @glob = 10
    @zmienna = 3.0
    return glob
}

fn bar(int a) -> int {
    return a
}


fn main() -> int {
    @zmienna = 2.0

    x = foo()
    print @zmienna
    print x
    glob = @glob + 2
    print glob

    a = 99
    cond = condition(a)

    tab = {0, 0, 0, 0, 0, 0}
    i = 0
    
    while (i < 6){
        tab[i] = i
        print tab[i]
        i = i + 1
    }
    
    return 0
}
