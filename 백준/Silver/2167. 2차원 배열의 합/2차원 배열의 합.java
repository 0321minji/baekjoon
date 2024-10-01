import java.util.*;

public class Main{
    public static int check(int i, int j, int x, int y, int arr[][]){
        int result=0;
        for (int a=i-1;a<x;a++){
            for (int b=j-1;b<y;b++){
                result+=arr[a][b];
            }
        }
        return result;
    }
    public static void main(String[] args){
        //입력
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        // int m=Integer.valueOf(sc.nextLine());
        int m=sc.nextInt();

        int arr[][] = new int[n][m];
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                arr[i][j]=sc.nextInt();
            }
        }
        int k=sc.nextInt();
        for (int c =0; c<k;c++){
            int i=sc.nextInt();
            int j=sc.nextInt();
            int x=sc.nextInt();
            int y=sc.nextInt();
            int result=check(i,j,x,y,arr);
            System.out.println(result);
        }
        sc.close();
    }
}