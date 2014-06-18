
public class PruebaTabla {
    public static void main (String [] args){
        tabla(4);                          // ejemplo de llamada
        tabla(7);
    }
    public static void tabla (int n) {     // de tipo void
        System.out.println("Tabla de multiplicar del numero " + n);  
        for (int i=0; i<=10; i++) {
            System.out.println(n + " x " + i + " = " + producto(n,i));            
                 }
        return;                            // No devuelve ningun valor
    }
    public static int producto (int a, int b) {
        return a*b;
    }
} 
