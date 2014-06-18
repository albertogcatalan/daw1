class Base {
  int i=1;
  void inicio() {};
  void fin() {};
}
class PruebaBase {
   void prueba(Base p) {
      p.inicio();
      p.i++;
      System.out.println("Valor de i: " + p.i);
      p.fin();
  }
}
public class PruebaClaseAnonima {
   public static void main(String [] args) {
      PruebaBase a = new PruebaBase();
      System.out.println("Inicio");
      a.prueba(new Base() {
               void inicio() {System.out.println("Inicio anonima");}
               void fin() {System.out.println("Fin anonima");}
               });    // Fin llamada a prueba
      System.out.println("Fin");
   }                  // Fin metodo main
}                     // Fin PruebaClaseAnonima
