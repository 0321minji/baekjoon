import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        char[] string=sc.nextLine().toCharArray();

        Stack<Character> st=new Stack<>();
        int result=0;
        int tmp=1;
        sc.close();
        for (int i=0;i<string.length;i++){
            if (string[i]=='('){
                tmp*=2;
                st.push(string[i]);
            }
            else if (string[i]==')'){
                if (st.isEmpty() || st.peek()!='('){
                    result=0;
                    break;
                }
                if (string[i-1]=='('){
                    result+=tmp;
                }
                st.pop();
                tmp/=2;
            }
            else if (string[i]=='['){
                tmp*=3;
                st.push(string[i]);
            }
            else if (string[i]==']'){
                if (st.isEmpty() || st.peek()!='['){
                    result=0;
                    break;
                }
                if (string[i-1]=='['){
                    result+=tmp;
                }
                st.pop();
                tmp/=3;
            }
        }
        if (!st.isEmpty()){
            result=0;
        }
        System.out.println(result);
    }
}
