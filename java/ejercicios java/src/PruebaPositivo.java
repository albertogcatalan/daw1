/** 
 *  Demostracion de la funcion esPositivo
 *  A. Garcia-Beltran - octubre, 2009
 */
public class PruebaPositivo {
    public static void main (String [] args){
        for (int i=5; i>=-5; i--) 
            System.out.println(i + " es positivo: " + esPositivo(i));   
    }
    public static boolean esPositivo(int x) {
        if (x<0) return false;
        else return true;
        // Error: retorno perdido si x es igual a cero.
    }
} 
