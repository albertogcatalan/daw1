public class Carta {
   private final Valor valor;
   private final Palo palo;
   public Carta(Valor v, Palo p) {
      valor = v;
      palo = p; }
   public Palo Palo() {
      return palo; }
   public Valor Valor() {
      return valor; }
   public String toString() {
      return valor + " de " + palo;
   }
}
