import java.util.Scanner;

/**
 * @author Stephane Couvreur
 */
public class Solution {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        Integer n = scanner.nextInt();
        String ans = "";
        if (n % 2 == 1 || n >= 6 && n <= 20) {
            ans = "Weird";
        }
        else if (n % 2 == 0 || n >= 2 && n <= 5) {
            ans = "Not Weird";
        }
        else {
            ans = "Not Weird";
        }
        System.out.println(ans);
        scanner.close();
    }
}
