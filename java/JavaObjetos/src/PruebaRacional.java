
public class PruebaRacional {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Racional r1, r2;
		r1 = new Racional();
		r2 = new Racional();
		r1.asignar(2,3);
		r2.asignar(18,9);
		System.out.println(r1);
		System.out.println(r2);
		r1.sumar(r2);
		System.out.println(r1);
		
	}

}
