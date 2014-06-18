
public class Factura extends Precio{
	private Cliente cliente;
	private String emisor;
	

	public String getEmisor() {
		return emisor;
	}

	public void setEmisor(String emisor) {
		this.emisor = emisor;
	}


	public void setCliente(Cliente cliente) {
		this.cliente = cliente;
	}
	
	public Factura(Cliente cliente, String emisor, double eur) {
		setEuros(eur);
		
		this.cliente = cliente;
		this.emisor = emisor;
	}

	public void imprimirFactura(){
		System.out.println("Cliente: " + cliente.toString());
		System.out.println("Emisor: " + emisor);
		System.out.println("Coste: " + getEuros()+"Û");
		
	}
	
}
