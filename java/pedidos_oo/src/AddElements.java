
public class AddElements {

	
		public static Cliente NuevoCliente()
		{
			Cliente cl=new Cliente();
			System.out.println("Cif: ");
			cl.setCif(Leer.dato());
			System.out.println("Raz�n social: ");
			cl.setRazonsocial(Leer.dato());
			System.out.println("Domicilio social: ");
			cl.setDomiciliosocial(Leer.dato());
			System.out.println("C�digo Postal: ");
			cl.setCodpostal(Leer.dato());
			System.out.println("Poblacion: ");
			cl.setPoblacion(Leer.dato());
			System.out.println("Provincia: ");
			cl.setProvincia(Leer.dato());
			System.out.println("Telefono ");
			cl.setTelefono(Leer.dato());
			System.out.println("L�mite de cr�dito: ");
			cl.setCreditlimite(Leer.datoFloat());
			
			return cl;
		}
	public static Producto NuevoProducto()
	{  Producto pd =new Producto();
		System.out.println("Clave de producto: ");
		pd.setProdid(Leer.datoInt());
		System.out.println("Descripci�n: ");
		pd.setDescripcion(Leer.dato());
		System.out.println("Precio normal: ");
		pd.setPrecionormal(Leer.datoFloat());
		System.out.println("Precio m�nimo: ");
		pd.setPreciominimo(Leer.datoFloat());
		System.out.println("Precio m�nimo: ");
		pd.setPreciominimo(Leer.datoFloat());
		System.out.println("Existencias: ");
		pd.setExistencias(Leer.datoInt());
		System.out.println("Precio m�nimo: ");
		pd.setTipoiva(Leer.datoFloat());
		
		return pd;
	}	
}
