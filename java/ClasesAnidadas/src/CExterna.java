public class CExterna {
   private int n = 1;
   static class CAnidadaEstatica {
      public void metododeAnidada(CExterna e){
         e.n++;
         System.out.println("Dentro metodo c. anidada: " + e.n);
      }            //  Fin metodo clase anidada estatica
   }               //  Fin clase anidada estatica
   public void incN() { n++; }
   public int daN() { return n; }
   public void metododeExterna() {
      CAnidadaEstatica c = new CAnidadaEstatica(); // Uso anidada
      n++;
      System.out.println("Dentro metodo externo: " + n);
      c.metododeAnidada(this);
   }                  // Fin metodo clase externa 
}                     