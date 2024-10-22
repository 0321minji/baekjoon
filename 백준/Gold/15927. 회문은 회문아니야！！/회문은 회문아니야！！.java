import java.util.*;

public class Main {
    public static boolean check(String str, int n){
        String left, right;
        int length = str.length();
        int mid = length/2;
        
        //left,right 나눔
        if(length %2==1){
            left = str.substring(0, mid+1-n);
        }
        else{
            left=str.substring(0,mid-n);
        }
        right=str.substring(mid,length-n);

        //stringbuilder
        return !left.equals(new StringBuilder(right).reverse().toString());

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input=sc.nextLine();
        int result=-1;

        if(check(input,0)){
            result=input.length();
        }
        else if(check(input,1)){
            result=input.length()-1;
        }      
        
        System.out.println(result);
        sc.close();

    }
}
