import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        System.out.println(solve(n));
        sc.close();
    }

    public static int solve(int n){
        int temp;
        int result = 0;

        temp=n/5;
        if(n%2!=0){
            if (temp%2!=0){
                result+=temp;
                n-=5*temp;
            } else{
                if(temp==0) return -1;
                result+=temp-1;
                n-=5*(temp-1);
            }
        } else{
            if (temp%2!=0){
                result+=temp-1;
                n-=5*(temp-1);
            } else{
                result+=temp;
                n-=5*temp;
            }
        }
        result+=n/2;
        if (n%2!=0){
            return -1;
        }
        return result;
    }
    
}
