public class PruebaSobrecarga {
   public static void main (String [] args) {
     int a=34;
     int b=12;
     int c=56;
     int d=444;
     System.out.println("a = " + a + "; b = " + b + "; c = " + c);
     System.out.println("El mayor de a y b es: " + mayor(a,b));
     System.out.println("El mayor de a, b y c es: " + mayor(a,b,c));
     System.out.println("El mayor de a, b, c y d es: " + mayor(a,b,c,d));
     System.out.println("El menor de a y b es: " + menor(a,b));
     System.out.println("El menor de a, b y c es: " + menor(a,b,c));
     ordenados(a,b,c);
     
   }
   // Definicion de mayor de dos numeros enteros
   public static int mayor (int x, int y) {
     return x>y ? x : y;
   }
   // Definicion de mayor de tres numeros enteros
   public static int mayor (int x, int y, int z) {
     return mayor(mayor(x,y),z);
   }
   // Definicion de mayor de tres numeros enteros
   public static int mayor (int x, int y, int z,int w) {
     return mayor(mayor(x,y,z),w);
   }
   //Encuentra el menor de dos
   public static int menor (int x, int y){
	   return x < y ? x : y;
   }
   public static int menor (int x, int y, int z){
	   return menor(menor(x,y),z);
   }
   //Ordena los números
   public static void ordenados(int x, int y, int z){
	   int menor, medio, mayor;
	   
	   menor = menor(x,y,z);
	   mayor = mayor(x,y,z);
	   
	   if(x != menor && x != mayor){
		   medio = x;
	   }
	   else if (y != menor && y != mayor){
		   medio = y;
	   }
	   else 
		   medio = z;
	   
	   System.out.format("Los números %d %d %d ordenados son %d %d %d", x,y,z,menor,medio,mayor);
   }
   
} 