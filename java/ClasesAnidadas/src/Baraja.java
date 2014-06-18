public class Baraja {
  private static Carta[] cartas = new Carta[40];
  public Baraja() {
    int i = 0;
    for (Palo palo : Palo.values()) {
        for (Valor valor : Valor.values()) {
            cartas[i++] = new Carta(valor, palo); } }
    }
  public void mostrarBaraja() {
    for (int i=0; i<40; i++) {
         System.out.println(cartas[i].toString()); }
  }
}
