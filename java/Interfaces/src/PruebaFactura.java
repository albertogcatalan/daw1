
public class PruebaFactura {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// inicializamos factura
		Factura mifactura = new Factura();
		
		mifactura.asignaValor(345);
		System.out.println("***Mi factura***");
		System.out.println("Con IVA: " + mifactura.conIVA());
		System.out.println("Sin IVA: " + mifactura.sinIVA());
		
		mifactura.rebaja(20);
		System.out.println("***Rebaja del 20%***");
		System.out.println("Con IVA: " + mifactura.conIVA());
		System.out.println("Sin IVA: " + mifactura.sinIVA());
		

	}

}
