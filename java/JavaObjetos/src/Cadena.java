public class Cadena {
  public static void main (String [] args) {
     String saludo = "Hola";
     String despedida;
     despedida = "Adios";
     
     String cortesia = saludo + " y " + despedida;
    
     System.out.print(cortesia + " tiene ");
     System.out.println(cortesia.length() + " caracteres");
     
     for (int i=cortesia.length()-1 ; i>=0; i--) {
         System.out.print(cortesia.charAt(i));
         }
     
     
     System.out.println(" ");
     
     cortesia = cortesia.toUpperCase();
     for (int i=0; i<=cortesia.length()-1; i++) {
         System.out.println("Indice: " + i + " Letra: " + cortesia.charAt(i));
         } 
     
     
     
     
     }
  
}