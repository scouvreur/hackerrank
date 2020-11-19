import java.util.Scanner;

/**
 * @author Stephane Couvreur
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int array[];
        array = new int[3];
        for (int i = 0; i < array.length; i++) {
            array[i] = scan.nextInt();
            System.out.println(array[i]);
        }
    }
}
