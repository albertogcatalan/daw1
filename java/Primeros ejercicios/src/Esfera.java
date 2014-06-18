
public class Esfera {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int r;
		double s, v;
		final double PI=3.141592;
		r = 10;
		
		//calculamos la superficie
	    s = 4*PI*r*r;
	    //calculamos el columen
	    v = 4/3*PI*r*r*r;
	    
	    System.out.println("Dimensiones de la esfera:");
	    System.out.println("Radio = " + r + " metros");
	    System.out.println("Area = " + s + " metros cuadrados");
		System.out.println("Volumen = " + v + " metros cubicos");

	}

}
