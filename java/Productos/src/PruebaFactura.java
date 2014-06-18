
public class PruebaFactura {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Cliente alberto = new Cliente("Alberto","78759627Z");
		
		Factura fac = new Factura(alberto, "Pepe", 100.4);
		fac.imprimirFactura();
		
	}

}
