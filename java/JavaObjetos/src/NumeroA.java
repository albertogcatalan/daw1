import java.io.*;
public class NumeroA {
  public static void main (String [] args) {
    BufferedReader in = new BufferedReader ( new
                           InputStreamReader( System.in ) );
    String c="";
    int n=0;
    System.out.print("Introduce una cadena de caracteres: ");
    try { c = in.readLine(); }
    catch (Exception exc )
      { System.out.println( exc ); } 
    for (int i=0; i<c.length(); i++) {
      if ((c.charAt(i)=='a') || (c.charAt(i)=='A')) { n++; }
      }
    System.out.print("El numero de caracteres a o A es ");
    System.out.println(": " +n);
  }
}
