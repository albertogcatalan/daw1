public class PruebaDia {
   Dia dia; 
   public PruebaDia(Dia dia) {
      this.dia = dia;  }
   public String toString() {
      switch (dia) {
         case LUNES:     return "lunes";            
         case MARTES:    return "martes";
         case MIERCOLES: return "miercoles";
         case JUEVES:    return "jueves";
         case VIERNES:   return "viernes";
         case SABADO:    return "sabado";
         case DOMINGO:   return "domingo";
      default:  return "";  }
   }
   public static void main(String[] args) {
      PruebaDia dia1 = new PruebaDia(Dia.LUNES);
      System.out.println(dia1.toString());
      PruebaDia dia2 = new PruebaDia(Dia.MARTES);
      System.out.println(dia2.toString());
   }
}
