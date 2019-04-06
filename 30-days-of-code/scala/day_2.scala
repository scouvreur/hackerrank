import scala.math

object Solution {
    // Complete the solve function below.
    def solve(meal_cost: Double, tip_percent: Int, tax_percent: Int) {
        var totalCost: Double = ((100 + tip_percent.toDouble + tax_percent.toDouble) / 100) * meal_cost
        totalCost = Math.round(totalCost)
        println(totalCost.toInt)
    }

    def main(args: Array[String]) {
        val stdin = scala.io.StdIn
        val meal_cost = stdin.readLine.trim.toDouble
        val tip_percent = stdin.readLine.trim.toInt
        val tax_percent = stdin.readLine.trim.toInt

        solve(meal_cost, tip_percent, tax_percent)
    }
}