import java.util.Scanner;
import java.util.Arrays;

public class Camila{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int[] idades = new int[3];
        int i=0;
        while(i<3){
            int idade = in.nextInt();
            if(idade >= 5 && idade <= 100){
                idades[i] = idade;
                i++;
            }
        }
        Arrays.sort(idades);
        System.out.println(idades[1]);
        in.close();
    }
}