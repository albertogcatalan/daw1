import java.util.ArrayList;
import java.util.GregorianCalendar;

import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;


public class NuevoPedido {

	/**
	 * @param args
	 */
	final static String DB4OFILENAME = System.getProperty("user.home")
			+ "/pedidos1.db4o";
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ObjectContainer db = Db4oEmbedded.openFile(Db4oEmbedded
				.newConfiguration(), DB4OFILENAME);
		
		// creamos un pedido y agregamos los datos
		Pedido ped1 = new Pedido();
		ped1.setNumeropedido(1);
		ped1.setFechapedido(new GregorianCalendar());
		ped1.setImpuestos(78.23F);
		ped1.setBaseimponible(895.0F);
		ped1.setTotal(909.25F);
		ped1.setTotaldescuentos(5.23F);
		Cliente cliente1 = new Cliente("123456789X","cpifp los enlaces","Jarque de moncayo 10",
				"50012","Zaragoza","Zaragoza","976300804",90000.00F);
		ped1.setCliente(cliente1);
		
		LineaPedido lpedido1 = new LineaPedido();
		lpedido1.setNumerolineapedido(1);
		lpedido1.setDescuento(4.0F);
		lpedido1.setPrecioactual(20.2F);
		Producto pd=new Producto(1,"Router",58.00F,50.00F,85,0.18F);
		lpedido1.setProducto(pd);
		lpedido1.setTotallinea(2.0F);
		lpedido1.setUnidades(1);
		
		ArrayList <LineaPedido> lineas = new ArrayList <LineaPedido>();
		lineas.add(lpedido1);
		ped1.setLineaspedido(lineas);
		
		db.store(ped1);
		db.close();
	}

}
