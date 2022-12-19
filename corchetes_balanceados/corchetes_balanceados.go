package main
import "fmt"

func corchetesBalanceados(cadena string) bool {
    corchetes_open := 0;
    for i := 0 ; i < len(cadena); i++ {
       
        char := cadena[i]
        if char == '[' {
            corchetes_open += 1
        } else if char == ']' {
            corchetes_open -= 1
        }
        if corchetes_open < 0 {
            return false
        }
    } 
    if corchetes_open != 0 {
        return false
    }
    return true
}

func main() {
    fmt.Println(corchetesBalanceados("]"))
}
