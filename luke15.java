import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;


class Luke15{
    public static void main(String args[]){
        List<Integer> traer = new ArrayList<Integer>(Arrays.asList(5, 4, 4, 2, 2, 8));
        Collections.sort(traer);
        int antallTraer = traer.length;
        List<Integer> lengder = new ArrayList<Integer>();
        int[] entotre = {1,2,3};
        while (antallTraer > 0){
            lengder.add(antallTraer);
            List<Integer> nyetraer = new ArrayList<Integer>();
            for (int i = 0; i < antallTraer; i ++){
                if (traer.get(i) > traer.get(0)){
                    nyetraer.add(traer.get(i) - traer.get(0));  
                } 
            }
            traer = nyetraer;
            int nyAntallTraer = traer.length;
            antallTraer = nyAntallTraer;
        }
        System.out.println(lengder);
        
    }
}