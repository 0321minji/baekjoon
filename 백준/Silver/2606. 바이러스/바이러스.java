import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static int cnt=0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //init
        int n=Integer.parseInt(sc.nextLine());
        int m=Integer.parseInt(sc.nextLine());
        // sc.nextLine();
        ArrayList<ArrayList<Integer>> com = new ArrayList<>();
        for (int i=0;i<n;i++){
            com.add(new ArrayList<>());
        }
        
        int x,y;
        for(int i=0;i<m;i++){
            x=sc.nextInt();
            y=sc.nextInt();
            com.get(x-1).add(y-1);
            com.get(y-1).add(x-1);
        }

        //함수 호출
        ArrayList<Integer> virous = new ArrayList<>();
        virous.add(0);
        solve(0,com,virous);
        System.out.println(cnt);

    }

    public static void solve(int i, ArrayList<ArrayList<Integer>> com,ArrayList<Integer> virous){
        for (Integer next : com.get(i)){
            if (!virous.contains(next)){
                virous.add(next);
                cnt+=1;
                solve(next,com,virous);
            }
        }
    }
}
