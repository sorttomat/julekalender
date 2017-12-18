
public class luke17 {
    public static void main(String[] args){

        int tall = 6;

        while(true) {
            if (flyttTall(tall) / 4 == tall) {
                System.out.println("Done!" + " " + tall + " " + flyttTall(tall));
                break;
            }
            tall += 10;
        }    
    }
    
    static int flyttTall(int tall) {
        String nyttTall = Integer.toString(tall);
        nyttTall = "6" + nyttTall.substring(0, nyttTall.length()-1);
        int nyttTall2 = Integer.valueOf(nyttTall);
        return nyttTall2;
    }

}