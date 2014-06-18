public class Fecha {
	
	//atributos
  private Dia dd;
  private Mes mm;
  private Anho aa;
  
//constructor de fecha
public Fecha(int d, int m, int a) {
    this.dd = new Dia(d);
    this.mm = new Mes(m);
    this.aa = new Anho(a);  }
  public void siguienteDia() {
    dd.siguiente();  }
  
  public String toString() {
		return dd+"/"+mm+"/"+aa;
	}
  
  //clase interna dia
  private class Dia {
    private int d; 
    public Dia(int d){
      this.d = d; }
    public void siguiente() {
      d = d + 1;
      verificar();  }
    private void verificar() {
      if (d > mm.dias()) {
         d = 1;
         mm.siguiente();  }
    }
    public String toString() {
    	if (d < 10){
			return "0"+d;
		}else{
			return d+"";
		}
  		}
  }        // Fin de la clase Dia

  //clase interna mes
  private class Mes {
      private int m;
      private final int[] diasDelMes = 
        {0,31,28,31,30,31,30,31,31,30,31,30,31};
      public Mes (int m) { this.m = m; }
      public int dias() {
        int r = diasDelMes[m];
        if ((m==2)&& aa.esBisiesto()) { r = r+1; }
        return r; }
      public void siguiente() {
        m = m + 1;  verificar();  }
      private void verificar() {
        if (m>12) { m=1; aa.siguiente(); }
        }
      public String toString() {
    		if (m < 10){
    			return "0"+m;
    		}else{
    			return m+"";
    		}
      }
    }   // Fin de la clase Mes
  
  //clase interna a–o
  private class Anho {
      private int a;
      public Anho(int a) { this.a = a; }
      public void siguiente() { a=a+1; }
      public boolean esBisiesto() {
        return ((a % 4 == 0) && (a % 100 !=0) || (a % 400 == 0)); }
      public String toString() {
  		return a+"";
  		}
      
    }
 
}
