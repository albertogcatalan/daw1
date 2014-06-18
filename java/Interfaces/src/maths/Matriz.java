package maths;
public final class Matriz {   
   public static double min(double [][] m) {
      double menor = m[0][0];
      for (int i=0; i<m.length; i++) {
          for (int j=0; j<m[i].length; j++) { 
              if (menor>m[i][j]) { menor=m[i][j]; } } }
      return menor;  }
   public static double max(double [][] m) {
      double mayor = m[0][0];
      for (int i=0; i<m.length; i++) {
          for (int j=0; j<m[i].length; j++) { 
              if (mayor<m[i][j]) { mayor=m[i][j]; } } }
      return mayor;  }
   public static double sum(double [][] m) {
      double sumatorio = 0.0;
      for (int i=0; i<m.length; i++) {
          for (int j=0; j<m[i].length; j++) { 
              sumatorio+=m[i][j]; } }
      return sumatorio; }
}

