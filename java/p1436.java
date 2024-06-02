
import java.util.Scanner;

public class p1436 {
    public void call(Scanner sc) {
        int n = sc.nextInt();
        int result = fn(n);
        System.out.println(result);
    }

    public int fn(int n) {
        int cnt = 0;
        int num = 666;

        while (true) { 
            if (String.valueOf(num).contains("666")) {
                cnt += 1;
                if (cnt == n) {
                    return num;
                }
            }
            num += 1;
        }
    }

}
