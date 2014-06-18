
public class Ecuacion {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double a = 1;
	    double b = 0;
	    double c = -1;
	    double x1, x2;
	    x1 = (-b + Math.sqrt(b*b-4*a*c))/(2*a);
	    x2 = (-b - Math.sqrt(b*b-4*a*c))/(2*a);
	    System.out.print("Sol. de la ec. de 2º grado: ");
	    System.out.println(a + "x2 + " + b + "x + " + c);
	    System.out.println("Primera solucion x1 = " + x1);
	    System.out.println("Segunda solucion x2 = " + x2);

	}

}
