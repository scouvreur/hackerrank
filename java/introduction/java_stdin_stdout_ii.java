import java.util.Scanner;

/**
 * @author Stephane Couvreur
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        Integer i = Integer.parseInt(scan.nextLine());
        Double d = Double.parseDouble(scan.nextLine());
        String s = scan.nextLine();

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}
