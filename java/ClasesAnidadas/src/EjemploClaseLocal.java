public class EjemploClaseLocal {
   private int n = 1;
   public void metododeExterna() {
      class ClaseLocal {
         public void metododeLocal(){
            n++;
            System.out.println("Dentro metodo local: " + n);
         }            //  Fin metodo clase local
      }               //  Fin clase local
      ClaseLocal c = new ClaseLocal();     // Uso ClaseLocal
      n++;
      System.out.println("Dentro metodo externo: " + n);
      c.metododeLocal();
   }                  // Fin metodo clase externa 
   public static void main(String [] args) {
      EjemploClaseLocal a = new EjemploClaseLocal();
      System.out.println("Inicio principal: " + a.n);
      a.metododeExterna();
      a.n++;
      System.out.println("Fin del principal: " + a.n);
   }                  // Fin metodo main
}                     // Fin clase externa
