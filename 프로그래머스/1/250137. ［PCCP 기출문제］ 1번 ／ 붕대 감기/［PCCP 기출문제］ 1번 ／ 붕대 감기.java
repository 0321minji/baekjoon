import java.util.*;

class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        List<Integer> time = new ArrayList<>();
        for (int[] attack : attacks){
            time.add(attack[0]);
        }
        
        int c=0, h=health, m=bandage[0], recover=bandage[1], plus = bandage[2];

        for(int i=1; i<=time.get(time.size()-1); i++){
            if(time.contains(i)){//공격 받은 time
                c=0;
                int index=time.indexOf(i);
                h -= attacks[index][1];
                if (h<=0){
                    return -1;
                }else{ //회복 
                    c+=1;
          
                    h += recover;
                  System.out.println("qwe: "+recover);
                    if (c==m){
                        c=0;
                        h+=plus;
                    }
                    h=Math.min(h,health);
                    if(h<=0){
                        return -1;
                    }
                }
            }
            System.out.println(h);
        }
        answer=h;
        return answer;
    }
}