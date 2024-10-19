import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        if (input.charAt(input.length()-1)==':'){
            input+='0';
        }
        String[] ip = input.split(":");
        int cnt = 8-ip.length;

        List<String> result = new ArrayList<>();
        boolean check = false;

        for (String s : ip){
            int length = s.length();
            if(length==0){
                if (!check){
                    for (int i=0;i<cnt+1;i++){
                        result.add("0000");
                    }
                    check=true;
                }
                else{
                    result.add("0000");
                }
            }
            else{
                String temp = "0000".substring(length)+s;
                result.add(temp);
            }
        }
        System.out.println(String.join(":",result));
        sc.close();
    }    
}
