
import java.util.Scanner;

public class p2903 {
    public void call(Scanner sc) {
        int n = sc.nextInt();
        int m = (int)Math.pow(2, n)+1;
        int r = (int)Math.pow(m, 2);
        System.out.println(r);
    }

}
