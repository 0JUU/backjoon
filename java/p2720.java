
import java.util.Scanner;

public class p2720 {
    public void call(Scanner sc) {
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int c = sc.nextInt();
            int q = c/25;
            int d = (c%25)/10;
            int n = ((c%25)%10)/5;
            int p = ((c%25)%10)%5;
            System.out.println(q+" "+d+" "+n+" "+p);
        }
    }

}
