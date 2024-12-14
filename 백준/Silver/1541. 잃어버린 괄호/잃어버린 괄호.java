import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine().trim();
        List<Integer> num = new ArrayList<>();
        List<Character> op = new ArrayList<>();
        StringBuilder temp = new StringBuilder();
        // StringBuilder 로 선언한 이유 : 자바의 String은 불변 객체 => 값을 변경할때마다 새로운 문자열 객체 생성
        // StringBuilder로 가변 객체로 선언 : 문자열을 수정할 때 더 효율적 (성능 개선)

        // 숫자 연산자 구분
        for (int i=0;i<str.length();i++){
            char ch = str.charAt(i);
            if (ch=='+'||ch=='-'){
                if (temp.length()==0){
                    op.add(ch);
                } else{
                    num.add(Integer.parseInt(temp.toString()));
                    temp.setLength(0);
                    op.add(ch);
                }
            } else{
                temp.append(ch);
            }
        }
        num.add(Integer.parseInt(temp.toString()));

        // 뒤에서부터 계산
        int result = 0;
        int tempSum = 0;
        for (int i=op.size()-1;i>=0;i--){
            tempSum+=num.get(i+1);
            if (op.get(i)=='-'){
                result-=tempSum;
                tempSum=0;
            }
        }
        if (tempSum!=0){
            result+=tempSum;
        }
        result+=num.get(0);
        System.out.println(result);
        sc.close();
    }
}
