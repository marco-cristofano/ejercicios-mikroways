package main
import "fmt"

func calcularVuelto(x, y int) {
    denominaciones := [10]int{1000, 500, 200, 100, 50, 20, 10, 5, 2, 1}
    vuelto := x - y
    respuesta := []int{}
    for i := 0 ; i < 10; i++ {
        billete := denominaciones[i]
        if billete > vuelto {
            continue
        }
        cantidad := int(vuelto / billete)
        for j := 0; j < cantidad; j++ {
            respuesta = append(respuesta, billete)
        }
        vuelto = vuelto % billete
    }
    fmt.Println(respuesta)
}

func main() {
    calcularVuelto(18, 10)
}
