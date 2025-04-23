import java.io.*;
import java.util.*;

public class Main{
    public static int t;
    
    public static int solve(HashMap<String,Integer> clothes){
        int res = 1;
        for ( int cnt: clothes.values()){
            res*=(cnt+1);
        }        
        return res-1;
    }
    
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t=Integer.parseInt(br.readLine());

        for (int i=0;i<t;i++){
            int n = Integer.parseInt(br.readLine());
            HashMap<String,Integer> clothes = new HashMap<>();
            for (int j=0;j<n;j++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                String name = st.nextToken();
                String type = st.nextToken();
                clothes.put(type,clothes.getOrDefault(type, 0) + 1);
            }
            System.out.println(solve(clothes));
        }

    }
}