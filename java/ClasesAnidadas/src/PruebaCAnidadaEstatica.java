public class PruebaCAnidadaEstatica {
   public static void main(String [] args) {
      ClaseExterna a = new ClaseExterna();
      System.out.println("Inicio principal: " + a.daN());
      a.metododeExterna();
      a.incN();
      System.out.println("Fin del principal: " + a.daN());
   }                  // Fin metodo main
}
