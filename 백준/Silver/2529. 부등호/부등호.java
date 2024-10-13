import java.util.*;

public class Main {
    static int k;
    static String[] arr;
    static int[] visit = new int[10];
    static ArrayList<String> result = new ArrayList<String>();

    // 부등호 체크
    public static boolean check(char x, char y, char eq){
        if (eq=='>' &&x<y){
            return false;
        }
        if (eq=='<' && x>y){
            return false;
        }
        return true;
    }

    // 숫자 조합 찾기
    public static void solve(int depth, String now){ 
        if (depth==k+1){
            result.add(now);
            return;
        }
        for (int i=0;i<10;i++){
            if (visit[i]==1){
                continue;
            }
            if (depth==0 || check(now.charAt(depth-1),(char)(i+48),arr[depth-1].charAt(0))){
                visit[i]=1;
                solve(depth+1,now+i);
                visit[i]=0;
            }
        }
    }

    // 메인: 가능한 모든 조합을 찾고 정렬 후 출력
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        k=Integer.parseInt(sc.nextLine());
        arr=sc.nextLine().split(" ");
        
        solve(0,"");
        Collections.sort(result);
        System.out.println(result.get(result.size()-1));
        System.out.println(result.get(0));
        sc.close();
    }
}   
