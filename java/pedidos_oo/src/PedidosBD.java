import java.io.File;

import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;

/**
 * 
 */

/**
 * @author Profesor
 *
 */
public class PedidosBD {

	

		final static String DB4OFILENAME = System.getProperty("user.home")
				+ "/pedidos1.db4o";
		
	

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		//new File(DB4OFILENAME).delete();
		ObjectContainer db = Db4oEmbedded.openFile(Db4oEmbedded
				.newConfiguration(), DB4OFILENAME);
		Cliente cl=new Cliente("123456789X","cpifp los enlaces","Jarque de moncayo 10",
				"50012","Zaragoza","Zaragoza","976300804",90000.00F);
		db.store(cl);
		/* se pide por consola 
		Cliente cliente1=AddElements.NuevoCliente();
		db.store(cliente1);*/
		Cliente cliente2=AddElements.NuevoCliente();
		db.store(cliente2);
		
		
		Producto pd=new Producto(1,"Router",58.00F,50.00F,85,0.18F);
		db.store(pd);
		/*se pide por consola
		Producto prod1=AddElements.NuevoProducto();
		db.store(prod1);
		Producto prod2=AddElements.NuevoProducto();
		db.store(prod2);
		Producto prod3=AddElements.NuevoProducto();
		db.store(prod3);
		*/
		
		
		
		
		db.close();
		System.out.println("Datos guardados");
		  
	}

}
