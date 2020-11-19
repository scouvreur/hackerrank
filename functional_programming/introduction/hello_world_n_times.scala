object Solution extends App {

    def f(n: Int) {
        for (w <- 0 until n) {
            println("Hello World")
        }
    }

    var N = scala.io.StdIn.readInt
    f(N)
}
