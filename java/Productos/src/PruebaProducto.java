
public class PruebaProducto {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Precio p = new Precio();
		p.setEuros(100);
		
		Producto pro = new Producto();
		pro.asignaProducto(1234, 120.4);
		System.out.println(pro);
		
		Producto pro2 = new Producto();
		pro2.asignaProducto(4557, 6658.4);
		System.out.println(pro2);
		
	}

}
