

public class PruebaFactorial {
    public static void main (String [] args){
        System.out.println("El factorial de 10 es: " + factorial(10));   
    }
    public static int factorial (int n) {  // declaracion del metodo
        int aux = 1;                       // declaracion local
        for (int i = 2; i<=n; i++)
            aux *= i;                      //  similar a aux = aux * i
        return aux;
    }
} 
