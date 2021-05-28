fn condition(int a) -> int {
    print a
    x = 0
    y = 0
    read x
    read y 
    if ( x == 2 and y > 5 ){
        qwe1 = "spelniony warunek 1"
        print qwe1
    } else if ( x ==  2 and y < 5){
        qwe2 = "spelniony warunek 2"
        print qwe2
    }
    return x
}


glob = 2

fn foo() -> int {
    glob = 5
    @glob = 10
    @zmienna = 3.0
    return glob
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



    return 0
}

