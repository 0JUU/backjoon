
import java.util.*;

public class p1676 {
    public void call(Scanner sc) {
        int n = sc.nextInt();
        int cnt = 0;
        for (int i = 5; n/i >= 1; i *= 5) {
            cnt += n/i;
        }
        System.out.println(cnt);
    }
}
