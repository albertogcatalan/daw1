public class ClaseExterna {
   private int n = 1;
   class ClaseInterna {
      public void metododeInterna(){
         n++;
         System.out.println("Dentro metodo interno: " + n);
      }            //  Fin metodo clase interna
   }               //  Fin clase interna
   public void incN() { n++; }
   public int daN() { return n; }
   public void metododeExterna() {
      ClaseInterna c = new ClaseInterna();   // Uso ClaseInterna
      n++;
      System.out.println("Dentro metodo externo: " + n);
      c.metododeInterna();
   }                  // Fin metodo clase externa 
}                     // Fin clase externa

